---
source: "https://techcommunity.microsoft.com/t5/azure-architecture-blog/who-can-see-this-record-designing-reusable-access-control-lists/ba-p/4575167"
title: "Who Can See This Record? Designing Reusable Access Control Lists for Azure Microservices"
author: "ShwethaPunnam"
date_published: "2026-11-23"
date_clipped: "2026-11-24"
category: "Software Architecture"
source_type: "rss"
---

# Who Can See This Record? Designing Reusable Access Control Lists for Azure Microservices

Source: https://techcommunity.microsoft.com/t5/azure-architecture-blog/who-can-see-this-record-designing-reusable-access-control-lists/ba-p/4575167

A user signs in, opens ***/records/1042***, and receives the correct response. Then they change one character in the URL and request ***/records/1043***.

The access token is valid. The API gateway accepted it. The user has the expected application role. Yet the response contains somebody else’s data.

Nothing sophisticated happened. The API authenticated the caller but never answered the question that mattered: **Is this caller allowed to perform this action on this specific record?**

[OWASP API Security Top 10 2023](https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/) calls this broken object-level authorization (BOLA). OWASP places it at API1:2023 and recommends an object-level authorization check in every endpoint that receives an object identifier and acts on the corresponding object.

This article presents an Azure-oriented pattern for making those checks consistent across microservices: a small reusable enforcement library, a relationship-aware decision service, trusted identities for both users and workloads, explicit exceptions, and telemetry that exposes endpoints where no decision was made.

> **Terminology note:** “ACL” in this article means application-level access control over business objects. It is not Azure role-based access control (Azure RBAC), a network ACL, or an Azure Storage ACL. Those controls protect different layers and remain important, but they do not decide whether a signed-in user may update business record 1043.

## Authentication, roles, and object authorization answer different questions

Authentication answers **who is calling**. A role or scope answers **what category of operation the caller may attempt**. Object-level authorization answers **whether that caller may perform that action on that resource now**.

A role such as *Member.Read* can establish that the caller is allowed to use a read API. It cannot, by itself, prove that the caller is related to the member identified in the route, query string, or request body. The [Azure Architecture Center guidance for multitenant identity](https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/approaches/identity) makes this distinction explicit: role information can be carried in identity tokens, while resource-level authorization data can be maintained and evaluated by the application.

For object authorization, the decision normally needs more context:

| Decision input | Example |
| --- | --- |
| Subject | The signed-in user or calling workload |
| Tenant | The customer or organization boundary |
| Action | Read, create, update, approve, or delete |
| Resource type | Member, booking, claim, account, or document |
| Resource ID | One ID or a batch of IDs |
| Relationship | Owner, delegate, reviewer, organization member, or service grant |
| Environment | Optional policy inputs such as endpoint or assurance level |

A useful decision can be expressed as:

> *Can subject S, in tenant T, perform action A on every resource R under policy P?*

Including the **action** matters. A relationship that allows reading a record does not automatically authorize updating or deleting it. Including the **tenant** matters because a valid relationship must never bridge an unintended tenant boundary.

The [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) recommends least privilege, deny by default, permission validation on every request, and early definition of users, resources, operations, and trust boundaries. Those principles shape the design below.

## Reference architecture

The pattern separates identity, enforcement, policy evaluation, relationship data, and observability.

*Figure 1. Reference architecture for object-level authorization*

The responsibilities are deliberately narrow:

1. **Microsoft Entra ID** issues identities and claims for users and workloads.
2. **Azure API Management** can validate the incoming token before forwarding the request. The API must still enforce its own authorization policy; token validation is not an object-level decision. The [validate-jwt policy](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy) can enforce token existence and validity and can validate properties such as issuer, audience, and required claims. For Microsoft Entra tokens, API Management also provides [validate-azure-ad-token](https://learn.microsoft.com/en-us/azure/api-management/validate-azure-ad-token-policy).
3. **The endpoint** knows which business objects the operation will access. This is why the final check belongs inside the service, close to the business logic.
4. **The reusable library** is the policy enforcement point. It extracts the trusted subject and tenant context, builds a normalized authorization request, calls the evaluator, fails closed, and records the outcome.
5. **The relationship or policy service** is the policy decision point. It evaluates authoritative relationships and returns a decision. It does not trust resource ownership supplied by the client.
6. **Azure Monitor Application Insights and Log Analytics** make missing, denied, skipped, and failed checks visible.

This separation also keeps the library small. The library enforces the decision; it does not become a second database of relationships.

### Model direct and inherited access

An application ACL can be stored as relationship tuples rather than hard-coded endpoint conditions.

For example:

> (user:alice) -[owns]-> (member:1042)
>
> (user:bob) -[delegate\_for]-> (member:1042)
>
> (member:1042) -[belongs\_to]-> (organization:contoso)

A policy can allow Alice to read member 1042 through the **direct owns relationship**, allow Bob through **delegate\_for**, and **allow both to read an organization-level resource** when the approved relationship chain reaches organization:contoso. This is relationship-based access control: the endpoint asks about the final resource and action, while the evaluator resolves direct or inherited relationships from authoritative data.

Keep relationship creation and removal under the business system that owns that lifecycle. The authorization service should not infer a relationship merely because a client supplied two matching identifiers, and the enforcement library should not copy relationship data into local configuration.

## Make the secure call the easy call

If every team implements object authorization from scratch, small differences accumulate: inconsistent tenant checks, one-at-a-time network calls, ambiguous batch behavior, and endpoints that forget the check entirely.

A reusable API should make the safe path short and the dangerous path difficult. The following C# shape is intentionally small:

```
public enum AccessAction
{
    Read,
    Create,
    Update,
    Delete,
    Approve
}
public enum EntityType
{
    Member,
    Booking,
    Organization
}
public interface IObjectAuthorizationClient
{
    Task AuthorizeAllAsync(AccessAction action, EntityType resourceType, IReadOnlyCollection<string> resourceIds, CancellationToken cancellationToken = default);
    Task AuthorizeAllAsync(AccessAction action, EntityType resourceType, Func<CancellationToken, Task<IReadOnlyCollection<string>>> resourceIdsFactory, CancellationToken cancellationToken = default);
}
```

The caller does **not** pass a subject ID or tenant ID. The library obtains them from the server’s validated identity context. This removes an easy source of confused-deputy and parameter-substitution bugs.

A handler remains straightforward:

```
public sealed class GetBalancesHandler
{
    private readonly IObjectAuthorizationClient authorization;
    private readonly IBalanceRepository balances;

    public GetBalancesHandler(IObjectAuthorizationClient authorization, IBalanceRepository balances)
    {
        this.authorization = authorization;
        this.balances = balances;
    }

    public async Task<IReadOnlyCollection<Balance>> HandleAsync(GetBalances request, CancellationToken cancellationToken)
    {
        await this.authorization.AuthorizeAllAsync(
            AccessAction.Read,
            EntityType.Member,
            request.MemberIds,
            cancellationToken);

        return await this.balances.GetAsync(request.MemberIds, cancellationToken);
    }
}
```

The authorization check runs **before** the protected data is loaded or changed.

### Four implementation choices carry most of the value

1. **Deny by default.** An unknown resource type, missing tenant context, malformed identity, evaluation timeout, or unexpected response must never turn into an allow decision.
2. **Use all-of semantics for a batch.** AuthorizeAllAsync allows the operation only when every target is authorized. If partial results are a valid business requirement, expose that as a differently named API and contract; do not silently drop denied items from a method that implies full success.
3. **Evaluate in bulk.** Send the caller, action, resource type, tenant, and complete ID set in one request. This avoids an N+1 authorization pattern and ensures the evaluator sees the batch as one decision.
4. **Load IDs lazily when discovery is expensive.** Some handlers must query another store to discover target IDs. A factory overload avoids that work when a preceding decision makes the lookup unnecessary. The library should invoke the factory at most once and only after validating the identity context.

A local self-access optimization can be useful, but only when the resource type, tenant, action, and identifier semantics make it provably equivalent to the normal policy. “The token subject equals the route ID” is not a general solution to BOLA; OWASP explicitly notes that comparing a token user ID with a request parameter addresses only a limited subset of cases.

## Model the decision explicitly

Avoid a Boolean-only contract when you need operational clarity. An evaluator response should distinguish an evaluated denial from a system failure.

```
public enum AuthorizationDecision { Allow, Deny, Error }
public sealed record AuthorizationResult(AuthorizationDecision Decision, string PolicyVersion, string ReasonCode, string CorrelationId);
```

Keep ReasonCode low-cardinality and safe for telemetry, for example relationship\_missing, tenant\_mismatch, service\_grant\_missing, or evaluator\_unavailable. Do not place access tokens, raw object data, or unrestricted identifiers in logs.

In this design:

- Allow lets the handler continue.
- Deny stops the operation and normally maps to *HTTP 403 Forbidden*.
- Error also stops the operation. It is recorded separately so an unavailable decision service is not mistaken for a policy denial. A service can map that condition to *503 Service Unavailable* while still failing closed and returning no protected data.

For highly sensitive APIs, decide consistently whether a missing or inaccessible record returns *403 or 404*. The key architectural requirement is that the response must not disclose protected information through inconsistent status codes, messages, or timing.

## User calls and workload calls need different identities

Service-to-service authorization is where otherwise sound designs often acquire a bypass.

Consider a booking flow. A user calls a Rules service. The Rules service then calls a Records service to find conflicting bookings. Sometimes Rules is acting for the user; at other times it performs a broader system operation that the user could not perform directly.

Those are two different security modes and should be represented by two different tokens.

When a downstream API should enforce the user’s permissions, use the [OAuth 2.0 on-behalf-of flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow). Microsoft describes OBO as delegation: a middle-tier API obtains a downstream access token that carries the user’s identity and delegated permissions through the request chain.

*Figure 2. Acting on behalf of the user with the OBO flow*

The downstream service validates a token intended for its own audience and applies the same object-level policy it would apply to a direct user request.

### Mode 2: perform work as the service

When the caller is performing its own approved workload operation, use an app-only identity such as a [managed identity for Azure resources](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview). Managed identities let Azure workloads obtain Microsoft Entra tokens without application code managing credentials. Microsoft Entra [app roles](https://learn.microsoft.com/en-us/entra/identity-platform/howto-add-app-roles-in-apps) can also be assigned to another application’s service principal or to a managed identity, allowing the target API to authorize the workload from validated token claims.

The target service should apply a narrow service grant such as:

```
{
  "principal": "<managed-identity-or-service-principal-object-id>",
  "audience": "api://records-api",
  "actions": [ "bookings.read-for-conflict-check" ],
  "resourceTypes": [ "Booking" ],
  "routeTemplates": [ "GET /api/bookings/conflicts" ],
  "owner": "records-api-team",
  "expiresOn": "<review-date>"
}
```

This is not an anonymous skip. It is an authorization decision for a validated workload identity.

## Make “no object check required” explicit

Some endpoints genuinely do not operate on caller-specific objects. A reference-data endpoint might return a fixed list of countries, for example. Other endpoints might enforce a specialized authorization policy outside the shared library.

Silence is a poor representation of that decision because silence also describes a forgotten check. Require explicit endpoint metadata and a reason:

```
[SuppressObjectAuthorization("Returns static reference data and accepts no caller-controlled object ID.")]
[HttpGet("api/reference/countries")] 
public IActionResult GetCountries() => Ok(this.countries);
```

Treat suppression as a reviewed decision, not a convenience:

- Require a non-empty justification.
- Record the endpoint, owner, reviewer, and review date.
- Reject vague reasons such as “not needed.”
- Prefer a specialized named policy when an endpoint does perform sensitive object access.
- Add a startup or CI test that inventories every endpoint and verifies that it has shared authorization, a specialized policy, or an approved suppression.

This turns a missing check from an invisible omission into a test failure or telemetry signal.

## Observe authorization coverage, not only denials

A security control is difficult to trust if you can measure failures but cannot detect where the control never ran.

Initialize an authorization outcome for every authenticated request. Middleware can begin with NotApplied; the library or suppression filter then replaces it with the final result.

| Outcome | Meaning | Operational response |
| --- | --- | --- |
| Allowed | Policy ran and allowed the action | Normal baseline |
| Denied | Policy ran and rejected the action | Investigate unusual increases and repeated probes |
| ServiceGrant | A validated workload used a narrow service grant | Confirm the principal, action, route, owner, and expiry |
| Suppressed | An approved declaration says object authorization is not applicable | Review reasons and age periodically |
| NotApplied | An authenticated request completed without an object-authorization decision | Treat as a coverage defect |
| Error | The authorization dependency or policy evaluation failed | Alert; fail closed and restore the dependency |

Record the outcome as an application-defined property on request telemetry. In workspace-based Application Insights, the AppRequests table exposes application-defined properties in the dynamic Properties column, as documented in the [Azure Monitor Logs AppRequests reference](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/apprequests).

The following KQL summarizes request volume and route coverage by result:

```
AppRequests
| where TimeGenerated > ago(7d)
| extend
    AclResult = tostring(Properties["AclResult"]),
    RouteTemplate = tostring(Properties["RouteTemplate"]),
    ServiceName = tostring(Properties["ServiceName"])
| where isnotempty(AclResult)
| summarize
    Requests = sum(ItemCount),
    DistinctRoutes = dcount(RouteTemplate)
    by ServiceName, AclResult
| order by ServiceName asc, Requests desc
```

To find coverage gaps:

```
AppRequests
| where TimeGenerated > ago(24h)
| extend
    AclResult = tostring(Properties["AclResult"]),
    RouteTemplate = tostring(Properties["RouteTemplate"]),
    ServiceName = tostring(Properties["ServiceName"])
| where AclResult == "NotApplied"
| summarize
    Requests = sum(ItemCount),
    LastSeen = max(TimeGenerated)
    by ServiceName, RouteTemplate
| order by Requests desc
```

## Test the decision matrix, not only the happy path

Authorization defects often hide in combinations. Build a reusable contract-test suite for every service that consumes the library.

At minimum, cover:

| Scenario | Expected result |
| --- | --- |
| Caller owns the resource in the active tenant | Allow |
| Caller has the required delegated relationship | Allow |
| Relationship exists in another tenant | Deny |
| Caller has the relationship but not the requested action | Deny |
| Batch contains one unauthorized ID | Deny the full all-of request |
| Subject or tenant context is missing | Error or unauthenticated response; never allow |
| Relationship service is unavailable | Error and fail closed |
| Workload token matches the exact service grant | ServiceGrant |
| Workload token has the wrong audience, action, or route | Deny |
| Suppression has a valid explicit reason | Suppressed |
| Authenticated endpoint makes no decision | NotApplied and CI/runtime detection |

Also test the trust boundary:

- A client-supplied identity header cannot override validated claims.
- Tokens for another audience are rejected.
- Expired or incorrectly issued tokens are rejected.
- A user token cannot activate a workload service grant.
- A workload token cannot silently become a delegated user token.
- A route change does not accidentally broaden an existing grant.

Run these tests in pull requests and after policy configuration changes. OWASP’s BOLA guidance specifically recommends tests that evaluate the authorization mechanism and block deployment when those tests fail.

## Trade-offs and alternatives

No authorization architecture is free.

### Shared library plus relationship service

**Strengths**

- Consistent enforcement API across services.
- Decisions use authoritative business relationships.
- Bulk and lazy evaluation control unnecessary calls.
- Coverage markers make omissions visible.
- Teams keep business-specific relationship data outside the library.

**Costs**

- A network dependency for non-local decisions.
- Versioning and adoption work across service teams.
- Operational ownership for policy, service grants, and telemetry.
- Careful caching is required if relationships change frequently. A cached allow must never outlive the risk tolerance for revoked access.

### Gateway-only authorization

A gateway is valuable for token validation, coarse scopes, quotas, and common edge policies. It usually does not know every business object that a handler will load, particularly when IDs are derived from a request body or database query. Therefore, gateway authorization complements but does not replace in-service object authorization.

### Token-only roles

Roles and scopes are efficient for broad capabilities. They become awkward when access depends on per-object relationships, tenant membership, or changing ownership. Use token claims as decision inputs, not as a substitute for resource policy.

## Architecture review checklist

Before approving an object-authorization design, ask:

- Is the user or workload identity cryptographically validated for the target API?
- Is tenant context validated on every object decision?
- Does the decision include the action, resource type, and every target ID?
- Is the default outcome deny?
- Are batch semantics explicit?
- Does an evaluator outage fail closed without being misreported as a normal denial?
- Are workload calls represented by managed identities or service principals instead of self-asserted headers?
- Are service grants narrow, owned, logged, and time-bounded?
- Must every endpoint declare shared authorization, a specialized policy, or a justified suppression?
- Can Azure Monitor identify authenticated routes where no decision occurred?
- Do logs avoid tokens, sensitive payloads, and high-cardinality resource IDs?
- Do tests cover cross-tenant access, mixed batches, token substitution, and dependency failure?

If any answer is unclear, the authorization boundary is unclear too.

## Closing thoughts

An access-control library has two sets of customers: the people whose data it protects and the developers who must use it correctly.

The design earns trust when the secure call is the shortest call, identities are validated rather than asserted, relationship decisions are authoritative, exceptions are narrow and visible, failures are closed, and missing checks appear in a dashboard or build failure before they appear in an incident report.

Authentication gets the caller to the door. Object-level authorization decides which records they may touch once they are inside.

## References

- [OWASP API1:2023 — Broken Object Level Authorization](https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/)
- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
- [Azure Architecture Center — Architectural approaches for identity in multitenant solutions](https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/approaches/identity)
- [Azure API Management — Validate JWT](https://learn.microsoft.com/en-us/azure/api-management/validate-jwt-policy)
- [Azure API Management — Validate Microsoft Entra tokens](https://learn.microsoft.com/en-us/azure/api-management/validate-azure-ad-token-policy)
- [Microsoft Entra ID — Managed identities for Azure resources](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview)
- [Microsoft identity platform — OAuth 2.0 On-Behalf-Of flow](https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth2-on-behalf-of-flow)
- [Microsoft identity platform — Add app roles and receive them in tokens](https://learn.microsoft.com/en-us/entra/identity-platform/howto-add-app-roles-in-apps)
- [Azure Monitor — Application Insights telemetry data model](https://learn.microsoft.com/en-us/azure/azure-monitor/app/data-model-complete)
- [Azure Monitor Logs — AppRequests table](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/apprequests)
