---
source: "https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030"
title: "Hardening OpenClaw on AKS: Mitigating Container Escapes with Kata microVM Isolation"
author: "Microsoft Tech Community"
date_published: "2026-04-30"
date_clipped: "2026-06-02"
category: "Azure & Cloud"
source_type: "rss"
---

# Hardening OpenClaw on AKS: Mitigating Container Escapes with Kata microVM Isolation

Source: https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030

# Hardening OpenClaw on AKS: Mitigating Container Escapes with Kata microVM Isolation | Microsoft Community Hub

Open Side Menu

[Skip to content](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030#main-content)[![Image 1: Brand Logo](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/themes/customTheme1/favicon-1730836271365.png?time=1730836274203)](https://techcommunity.microsoft.com/)

[Tech Community](https://techcommunity.microsoft.com/)[Community Hubs](https://techcommunity.microsoft.com/Directory)

[Products](https://techcommunity.microsoft.com/)

[Topics](https://techcommunity.microsoft.com/)

[Blogs](https://techcommunity.microsoft.com/Blogs)

[Events](https://techcommunity.microsoft.com/Events)

[Skills Hub](https://techcommunity.microsoft.com/category/skills-hub)

[Community](https://techcommunity.microsoft.com/)

[Register](https://techcommunity.microsoft.com/t5/s/gxcuf89792/auth/oidcss/sso_login_redirect/provider/default?referer=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fcoreinfrastructureandsecurityblog%2Fhardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati%2F4516030)[Sign In](https://techcommunity.microsoft.com/t5/s/gxcuf89792/auth/oidcss/sso_login_redirect/provider/default?referer=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fcoreinfrastructureandsecurityblog%2Fhardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati%2F4516030)

1.   [Microsoft Community Hub](https://techcommunity.microsoft.com/)

3.   [Communities](https://techcommunity.microsoft.com/category/communities)[Products](https://techcommunity.microsoft.com/category/products-services)[Microsoft Security](https://techcommunity.microsoft.com/category/microsoft-security)  

5.   [Core Infrastructure and Security](https://techcommunity.microsoft.com/category/cis)

7.   [Core Infrastructure and Security Blog](https://techcommunity.microsoft.com/category/cis/blog/coreinfrastructureandsecurityblog)

## Blog Post

![Image 2](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NTE2MDMwLWNEUVVldg?revision=1&image-dimensions=2000x2000&constrain-image=true)

Core Infrastructure and Security Blog 

13 MIN READ

# Hardening OpenClaw on AKS: Mitigating Container Escapes with Kata microVM Isolation

[![Image 3: jianshn's avatar](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/dS0zMTI2NDY4LTFxcGtiRA?image-coordinates=0%2C0%2C576%2C576&image-dimensions=50x50)](https://techcommunity.microsoft.com/users/jianshn/3126468)

[jianshn](https://techcommunity.microsoft.com/users/jianshn/3126468)

![Image 4: Icon for Microsoft rank](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/cmstNC05WEo0blc?image-dimensions=100x16&constrain-image=true)Microsoft

Apr 29, 2026

## What is OpenClaw, and what security challenges does it pose with container escapes?

OpenClaw is an open-source autonomous AI agent designed for power users and developers to automate tasks, such as managing emails, files, and scheduling via chat apps like WhatsApp or Telegram.

While OpenClaw functions as a powerful autonomous assistant, its **runtime model** creates a massive security paradox: to be truly useful, the agent requires broad permissions to your filesystem and APIs, yet this "God Mode" access often lacks the rigorous **containerized isolation** typical of enterprise workloads. Because many users run the framework natively rather than within a hardened sandbox, the primary **security challenge** is that a single malicious "Skill" or an indirect prompt injection can escalate into full system compromise. This structural vulnerability, exemplified by high-profile exploits like **CVE-2026-25253**, transforms the agent from a helpful tool into a high-risk entry point for lateral movement and data exfiltration within a private network.

**Why container escapes matter in OpenClaw-style deployments**: because containers share the host kernel, a successful container escape turns a single compromised container into a host compromise (or at least a compromise of other co-located workloads). This is especially important when OpenClaw runs code from many tenants, many teams, or varying trust levels on the same worker nodes. That soft isolation is often **permeable** due to the following structural and configuration-based weaknesses:

*   **Shared-kernel attack surface**: the container boundary is not a hypervisor boundary. Kernel vulnerabilities (e.g., privilege escalation bugs) can allow a process in a container to gain host-level privileges.
*   **Excessive privileges / misconfiguration**: running with _--privileged_, broad Linux capabilities, hostPath mounts, access to the Docker socket, or device passthrough (e.g., /dev/kvm, /dev/fuse) can provide direct paths to host control.
*   **Filesystem and namespace boundary breaks**: mount namespace confusion, writable host mounts, or mistakes in chroot/pivot_root handling can expose host files and credentials.
*   **Supply-chain and image risk**: a malicious image or dependency can execute within the container and then attempt escalation/escape.
*   **Blast radius**: once the host is compromised, attackers can access node-level secrets (service account tokens, registry creds), tamper with the runtime, sniff traffic, or pivot to other containers and the broader cluster.

In short, OpenClaw’s security challenge is not that containers are inherently insecure, but that the isolation boundary is thinner than a VM boundary. When the threat model includes adversarial code execution, a “container-only” isolation strategy often requires additional hardening or a stronger sandbox.

## What are MicroVMs and Kata Containers, and how do they help mitigate OpenClaw container-escape risks?

**MicroVMs** are lightweight virtual machines optimized for running short-lived or container-like workloads with much lower overhead than traditional VMs. They use hardware virtualization (via a hypervisor such as KVM) but keep the device model and boot path minimal, reducing startup time and the overall attack surface compared to a full general-purpose VM.

**Kata Containers** is an “OCI-compatible containers in a VM” approach: it runs each container (or pod sandbox) inside a dedicated microVM by default (implementation varies by runtime/config). To the orchestration layer (e.g., Kubernetes), it still looks like a container runtime, but isolation is provided by a hypervisor boundary rather than only namespaces/cgroups.

*   **Stronger isolation boundary**: a container escape that relies on Linux kernel exploitation is far less likely to directly compromise the host, because the workload’s “host” kernel is typically the guest kernel inside the microVM.
*   **Reduced blast radius**: compromise is contained to the microVM/pod sandbox; lateral movement to other workloads on the same node becomes significantly harder.
*   **Smaller and more controllable attack surface**: minimal device models, tighter default privileges, and fewer host mounts/devices exposed to the workload.
*   **Defense-in-depth with container controls**: you still can (and should) apply seccomp, capabilities dropping, read-only root filesystems, and LSMs inside the guest, but the hypervisor boundary becomes an additional layer.
*   **Better fit for hostile multi-tenant workloads**: when OpenClaw executes third-party jobs/plugins, Kata-style sandboxing aligns better with an adversarial threat model.

## Solution overview

Figure 1 illustrates a Kubernetes-based sandboxing architecture for running OpenClaw workloads with stronger isolation. The design keeps the developer experience and packaging model of containers (OCI images, Kubernetes scheduling) while ensuring that untrusted agent code executes inside a microVM boundary using Kata Containers. This reduces the likelihood that a container escape can compromise the underlying node or other co-located workloads.

**Key components**: (1) **Application gateway**for HTTPS traffic to the backend, (2) **Kubernetes** as the orchestration, scheduling and policy enforcement plane, (3) a **container runtime** (e.g., containerd) configured with a **Kata Containers runtime class**, (4) **KVM-backed microVMs** that provide the isolation boundary for each untrusted workload and (5) **Azure files**for persistent storage which allows scaling of OpenClaw.

![Image 5](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NTE2MDMwLVdreFV2eQ?image-dimensions=940x416&revision=1)
_Figure 1: Solution architecture diagram_

**End-to-end flow**:

1.   **Traffic Entry via Application Gateway**: Incoming user requests (e.g., from WhatsApp or Discord) first hit the **Azure Application Gateway**.
2.   **Orchestration in AKS**: The traffic is routed into an **Azure Kubernetes Service (AKS)** cluster, which manages the lifecycle of the OpenClaw agent and its associated "Skills."
3.   **Hardened Execution via Kata Containers**: Instead of running in standard shared-kernel containers, the **OpenClaw agent**runs inside **Kata Containers**. This provides a dedicated lightweight VM for the agent, creating a hardware-level isolation boundary that prevents "container escapes" from compromising the host.
4.   **Stateful Storage in Azure Files**: The agent interacts with **Azure Files** to read and write persistent data, such as conversation history, configuration files, and downloaded assets, ensuring data remains available even if the container is restarted.

**Security posture**: by shifting isolation from “shared-kernel containers” to “containers inside microVMs,” the architecture limits the blast radius of kernel-level exploits and common escape paths. Even if an attacker achieves code execution within an OpenClaw container, they must additionally break the microVM/hypervisor boundary to affect the node or neighboring workloads, providing a strong defense-in-depth improvement over standard container alone.

## Implement the solution

This section describes how to deploy the solution architecture.

In this post, you’ll perform the following tasks:

*   Create a Kata VM-isolated AKS node pool
*   Mount a NFS persistent storage
*   Create the application ConfigMap
*   Deploy the OpenClaw gateway
*   Expose the gateway internally
*   Set up TLS termination
*   Route external traffic through the Azure application gateway for containers.

Ensure that you have the following prerequisites deployed before moving to the next section:

*   An [AKS cluster](https://learn.microsoft.com/en-us/azure/aks/learn/quick-kubernetes-deploy-cli) provisioned in Azure
*   An Azure NFS [File Share](https://learn.microsoft.com/en-us/azure/storage/files/create-file-share?tabs=azure-portal) with private link enabled.
*   An [Application gateway for containers](https://learn.microsoft.com/en-us/azure/application-gateway/for-containers/quickstart-create-application-gateway-for-containers-managed-by-alb-controller?tabs=new-subnet-aks-vnet) managed by ALB controller
*   Kubectl configured and pointing to the cluster
*   Az CLI authenticated with the correct subscription

## Initialise environment variables

In your Linux terminal, export these variables with your own values. They will be used in later commands.

```none
export cluster_name=<CLUSTER_NAME>
export resource_group=<RESOURCE_GROUP>
```

## Create the AKS Node Pool with Kata VM Isolation

The OpenClaw gateway pods require Kata VM isolation (runtimeClassName: kata-vm-isolation). You must create a dedicated AKS node pool that supports this runtime before deploying any workloads.

Use the Azure CLI to add a node pool with the Kata VM isolation workload runtime to your existing AKS cluster:

```none
az aks nodepool add \
  --resource-group $resource_group \
  --cluster-name $cluster_name \
  --name katanp \
  --node-count 2 \
  --node-vm-size Standard_D4s_v3 \
  --os-sku AzureLinux \
  --workload-runtime KataMshvVmIsolation \
  --labels agentpool=katanp
```

****Important:**** The `--workload-runtime KataMshvVmIsolation` flag enables the `kata-vm-isolation` runtime class on the node pool. The VM size must support nested virtualization (D-series v3/v5, E-series v3/v5, etc.).

## Create NFS Persistent Volume

The deployment uses an Azure Files NFS share for persistent workspace storage. The PersistentVolume must exist before the PVC can bind to it. Replace volumeHandle and volumeAttributes with your own Azure Files values.

```none
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: PersistentVolume
metadata:
  name: openclaw-nfs-pv
spec:
  capacity:
    storage: 100Gi
  accessModes:
    - ReadWriteMany
  persistentVolumeReclaimPolicy: Retain
  mountOptions:
    - sec=sys
    - noresvport
    - actimeo=30
  csi:
    driver: file.csi.azure.com
    volumeHandle: <resource-group>#<storage-account>#<share-name>
    volumeAttributes:
      resourceGroup: <resource-group>
      shareName: <share-name>
      protocol: nfs
      server: <storage-account>.privatelink.file.core.windows.net
EOF
```

Verify that the persistent volume is created.

```none
kubectl get pv openclaw-nfs-pv
```
![Image 6](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NTE2MDMwLVpkN0Focw?image-dimensions=940x71&revision=1)
_Figure 2: Persistent volume_

## Create the NFS PersistentVolumeClaim

The PVC binds to the PV created. The deployment references this PVC by name (`pvc-openclaw-nfs`).

```none
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  # The name of the PVC
  name: pvc-openclaw-nfs
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      # The real storage capacity in the claim
      storage: 50Gi
  # This field must be the same as the storage class name in StorageClass
  storageClassName: ""
  volumeName: openclaw-nfs-pv
EOF
```

Verify that the persistent volume claim is created successfully. The status should show bound.

![Image 7](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NTE2MDMwLUwyOUZadQ?image-dimensions=999x46&revision=1)
_Figure 3: Persistent Volume Claim_

## Create the ConfigMap

The ConfigMap provides the openclaw.json configuration file to the gateway pods. It configures allowed CORS origins for the control UI and the gateway token. Replace the allowed origins with your own ALB frontend URL. The ConfigMap also stores the gateway auth token, so **DO NOT** hardcode your token here. Always keep it as a variable rather than storing it in plain text so that, if attackers gain access to this file, they cannot see the OpenClaw gateway auth token.

```none
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: ConfigMap
metadata:
  name: openclaw-config
data:
  openclaw.json: |
    {
      "gateway": {
        "auth": {
          "token": "${AUTH_TOKEN}"
        },
        "controlUi": {
          "allowedOrigins": [
            "https://<YOUR ALB FRONTEND URL>.alb.azure.com"
          ]
        }
      }
    }
EOF
```

## Create the Auth Token Secret

The OpenClaw gateway requires an authentication token to secure access. The deployment references a Kubernetes Secret named openclaw-auth-token and injects it into the container as the AUTH_TOKEN environment variable via secretKeyRef.

Generate a random token (or use an existing one) and create the kubernetes secret.

```none
# Generate a random 32-byte hex token
AUTH_TOKEN=$(openssl rand -hex 32)
echo "$AUTH_TOKEN"   # save this — you'll need it to authenticate with the gateway

kubectl create secret generic openclaw-auth-token \
  --from-literal=token="$AUTH_TOKEN"
```

If the secret does not exist when the deployment is applied, pods will fail with `CreateContainerConfigError`.

## Deploy the OpenClaw Gateway

This is the main application deployment. It depends on all previous steps:

- **Kata node pool**(pods require runtimeClassName: kata-vm-isolation and nodeSelector: agentpool=katanp)

- **PVC**(pvc-openclaw-nfs for persistent workspace data)

- **ConfigMap**(openclaw-config for openclaw.json)

Key details:

- Runs **2 replicas**with a rolling update strategy

- Uses an **init container**to copy the config file to a writable volume

- Exposes port **18789**

- Includes liveness and readiness probes on /health

- Resource requests: 500m CPU, 512Mi memory

- Resource limits: 2 CPU, 2Gi memory

```none
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: openclaw-gateway
spec:
  replicas: 2
  selector:
    matchLabels:
      app: openclaw-gateway
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1
      maxSurge: 1
  template:
    metadata:
      labels:
        app: openclaw-gateway
    spec:
      runtimeClassName: kata-vm-isolation
      nodeSelector:
        agentpool: katanp
      securityContext:
        fsGroup: 1000
      initContainers:
        - name: copy-openclaw-config
          image: alpine/openclaw:latest
          env:
            - name: HOME
              value: /writable
          command:
            - sh
            - -c
            - |
              cp /config/openclaw.json /writable/openclaw.json \
              && chown 1000:1000 /writable/openclaw.json \
              && echo "--- Config file contents ---" \
              && cat /writable/openclaw.json
          volumeMounts:
            - name: openclaw-config-volume
              mountPath: /config
            - name: openclaw-writable
              mountPath: /writable
      containers:
        - name: gateway
          image: alpine/openclaw:latest
          ports:
            - containerPort: 18789
          env:
            - name: NODE_OPTIONS
              value: "--max-old-space-size=4096"
            - name: AUTH_TOKEN
              valueFrom:
                secretKeyRef:
                  name: openclaw-auth-token
                  key: token
          # Start gateway the way the tutorial indicates
          command: ["openclaw", "gateway"]
          args: ["run", "--allow-unconfigured", "--bind", "lan"]
          volumeMounts:
            - name: openclaw-writable
              mountPath: /home/node/.openclaw
            - name: openclaw-data
              mountPath: /home/node/workspace
              subPath: workspace
          resources:
            requests:
              cpu: "500m"
              memory: "2Gi"
            limits:
              cpu: "1000m"
              memory: "4Gi"
          livenessProbe:
            httpGet:
              path: /health
              port: 18789
            initialDelaySeconds: 60
            periodSeconds: 15
            failureThreshold: 3
          readinessProbe:
            httpGet:
              path: /health
              port: 18789
            initialDelaySeconds: 10
            periodSeconds: 5
      volumes:
        - name: openclaw-data
          persistentVolumeClaim:
            claimName: pvc-openclaw-nfs
        - name: openclaw-config-volume
          configMap:
            name: openclaw-config
            items:
              - key: openclaw.json
                path: openclaw.json
        - name: openclaw-writable
          emptyDir: {}
---
apiVersion: v1
kind: Service
metadata:
  name: openclaw-gateway-service
spec:
  type: ClusterIP
  selector:
    app: openclaw-gateway
  ports:
    - protocol: TCP
      port: 18789
      targetPort: 18789
EOF
```

Verify that the deployment succeeds. Wait until all pods show `Running` and `READY 2/2`.

```none
kubectl get deployment openclaw-gateway
kubectl get pods -l app=openclaw-gateway
```
![Image 8](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NTE2MDMwLUdTUGVJYg?image-dimensions=940x383&revision=1)
_Figure 4: OpenClaw deployment_

## Create the TLS secret (for HTTPS)

The Application Gateway for Containers references a TLS secret (gateway-tls-secret) for HTTPS termination. This blog post uses a self-signed certificate; in a production environment, use a certificate signed by a certificate authority.Replace `<path-to-tls-cert>` and `<path-to-tls-key>` with paths to your TLS certificate and private key files.

```none
kubectl create secret tls gateway-tls-secret \
  --cert=<path-to-tls-cert> \
  --key=<path-to-tls-key>
```

## Create the Gateway

The Gateway resource defines the HTTPS listener on the Azure Application Load Balancer (ALB). Update the **`alb.network.azure.com/application-gateway-id**` annotation to match your ALB traffic controller resource ID. You will also need to reference the gateway-tls-secret to enable HTTPS.

```none
cat <<EOF | kubectl apply -f -
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: https
  annotations:
    alb.network.azure.com/application-gateway-id: /subscriptions/<subscription id>/resourceGroups/mc_openclaw_openclaw-cluster_centralus/providers/Microsoft.ServiceNetworking/trafficControllers/<alb id>
    alb.networking.azure.io/alb-namespace: default
    alb.networking.azure.io/alb-name: alb-openclaw
spec:
  gatewayClassName: azure-alb-external
  listeners:
    - name: https
      protocol: HTTPS
      port: 443
      allowedRoutes:
        namespaces:
          from: All
      tls:
        mode: Terminate
        certificateRefs:
        - kind: Secret
          group: ""
          name: gateway-tls-secret
EOF
```

```none
kubectl get gateway https
```

Wait until the Gateway shows a `Programmed=True` condition.

## Create the HTTPRoute

The HTTPRoute connects the Gateway to the backend Service. It routes all traffic (`/` prefix) from the HTTPS Gateway to `openclaw-gateway-service` on port 18789.

```none
cat <<EOF | kubectl apply -f -
kind: HTTPRoute
apiVersion: gateway.networking.k8s.io/v1
metadata:
  name: http-route
spec:
  parentRefs:
    - name: https
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /  
    backendRefs:
    - name: openclaw-gateway-service
      kind: Service
      namespace: default
      port: 18789
EOF
```

## Test OpenClaw application

Get the external endpoint.

```none
kubectl get gateway https -o jsonpath='{.status.addresses[0].value}'
```

Paste the endpoint into your browser to reach the OpenClaw application. If you are using a self-signed certificate, you will see a “Not secure” warning; click _Advanced_ to proceed. In a production environment with a certificate signed by a certificate authority, you should not see that warning.

![Image 9](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NTE2MDMwLWZsZ2lmbw?image-dimensions=697x999&revision=1)
_Figure 5: OpenClaw Authentication_

Paste in your Gateway Token (the auth token created earlier). You will notice that even though the token is valid, it throws back a “pairing required” error. Pairing is required in OpenClaw whenever a new device, browser profile, or CLI client attempts to connect to the gateway for the first time, ensuring only authorized clients can control the AI agent.

```none
POD=$(kubectl get pod -l app=openclaw-gateway -o jsonpath='{.items[0].metadata.name}')
POD2=$(kubectl get pod -l app=openclaw-gateway -o jsonpath='{.items[1].metadata.name}')
TOKEN=$(kubectl get secret openclaw-auth-token -o jsonpath='{.data.token}' | base64 -d)

kubectl exec "$POD" -c gateway -- openclaw devices approve --latest --token "$TOKEN"
kubectl exec "$POD2" -c gateway -- openclaw devices approve --latest --token "$TOKEN"
```

You should see a message like the one in the image below. You can now open the OpenClaw application and start using it.

![Image 10](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NTE2MDMwLVBVVGN1Sg?image-dimensions=940x56&revision=1)
_Figure 6: OpenClaw pairing success message_

![Image 11](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00NTE2MDMwLUJuNnpDMQ?image-dimensions=940x670&revision=1)
_Figure 7: OpenClaw Application_

You have successfully deployed OpenClaw within a microVM hosted on Azure Kubernetes Service.

## Test microVM kernel isolation

From within the OpenClaw pod, try to read the host’s root filesystem via /proc/1/root. You should see an error like: ls: cannot access '/proc/1/root/etc/kubernetes': No such file or directory.

```none
kubectl exec -it "$POD" -c gateway -- ls /proc/1/root/etc/kubernetes 2>&1
```

In a standard container deployment, PID 1 inside the container is still running on the**host kernel**, so traversing/proc/1/root/exposes the host's root filesystem — including sensitive paths like/etc/kubernetes(which holds kubelet credentials). With Kata VM isolation, the picture is completely different. When we run ls /proc/1/root/etc/kubernetes from inside the OpenClaw pod, it returns**"No such file or directory"**. This is because PID 1 is no longer a process on the host — it's running inside a dedicated**guest VM with its own kernel**. The/proc/1/root/path leads to the microVM's root filesystem, not the host's, and that microVM has no knowledge of the node's Kubernetes configuration or machine identity. The host is simply invisible. This is the core security guarantee of Kata Containers: even if an attacker achieves a full container escape, there is nothing to escape _to_ — they land inside a lightweight VM boundary, not on the shared host, making lateral movement to other pods or the node itself impossible.

## Conclusion

This post discussed why running OpenClaw workloads in standard containers can be risky when the workload includes untrusted or semi-trusted code: containers share the host Linux kernel, so a single container escape or privileged misconfiguration can expand into node-level compromise and a much larger blast radius. To address this, we introduced microVM-based sandboxing with Kata Containers on Azure Kubernetes Service (AKS) and walked through an implementation approach (a node pool with Kata VM isolation, storage, gateway deployment, and ingress). Finally, we validated the isolation properties by demonstrating that common host-visibility techniques (for example, probing _/proc/1/root_) no longer reveal host paths when the workload runs inside a microVM.

*   **Separate kernel boundary**: Kata runs the container inside a microVM, so the workload executes against a guest kernel rather than the shared host kernel—kernel exploits and escape attempts don’t directly translate into host control.
*   **Host filesystem is no longer “in scope”**: paths that often leak host context in standard containers (for example, traversals via _/proc_) resolve inside the microVM’s filesystem, not the node’s root filesystem.
*   **Reduced blast radius per workload**: each sandbox has its own VM boundary, making it much harder to pivot from one compromised workload to other pods/containers on the same node.
*   **Stronger default device and privilege separation**: the hypervisor boundary and minimal virtual device model limit exposure to host devices and privileged interfaces that commonly enable breakouts.
*   **Defense-in-depth still applies**: you can keep container hardening (seccomp, capability dropping, read-only filesystems, restricted mounts) while gaining an additional isolation layer that is independent of Linux namespaces/cgroups.

Overall, this post helps you deploy OpenClaw on AKS with Kata microVM isolation so you can run agent workloads with a significantly reduced risk of host-kernel compromise from container escape techniques.

Published Apr 29, 2026

Version 1.0

[azure kubernetes service](https://techcommunity.microsoft.com/tag/azure%20kubernetes%20service?nodeId=board%3ACoreInfrastructureandSecurityBlog)

[containers](https://techcommunity.microsoft.com/tag/containers?nodeId=board%3ACoreInfrastructureandSecurityBlog)

[Kata container](https://techcommunity.microsoft.com/tag/kata%20container?nodeId=board%3ACoreInfrastructureandSecurityBlog)

[microVM](https://techcommunity.microsoft.com/tag/microvm?nodeId=board%3ACoreInfrastructureandSecurityBlog)

[OpenClaw](https://techcommunity.microsoft.com/tag/openclaw?nodeId=board%3ACoreInfrastructureandSecurityBlog)

[security](https://techcommunity.microsoft.com/tag/security?nodeId=board%3ACoreInfrastructureandSecurityBlog)

Like

Comment

[![Image 12: jianshn's avatar](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/dS0zMTI2NDY4LTFxcGtiRA?image-coordinates=0%2C0%2C576%2C576&image-dimensions=80x80)](https://techcommunity.microsoft.com/users/jianshn/3126468)

[jianshn](https://techcommunity.microsoft.com/users/jianshn/3126468)

![Image 13: Icon for Microsoft rank](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/cmstNC05WEo0blc?image-dimensions=100x16&constrain-image=true)Microsoft

Joined July 29, 2025

Send Message

[View Profile](https://techcommunity.microsoft.com/users/jianshn/3126468)

[](https://techcommunity.microsoft.com/category/cis/blog/coreinfrastructureandsecurityblog)

[Core Infrastructure and Security Blog](https://techcommunity.microsoft.com/category/cis/blog/coreinfrastructureandsecurityblog)

Follow this blog board to get notified when there's new activity

Enjoying the article? Sign in to share your thoughts.

Sign in

### Share this page

*   [](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fcoreinfrastructureandsecurityblog%2Fhardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati%2F4516030)
*   [](https://www.facebook.com/share.php?u=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fcoreinfrastructureandsecurityblog%2Fhardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati%2F4516030&t=Hardening%20OpenClaw%20on%20AKS%3A%20Mitigating%20Container%20Escapes%20with%20Kata%20microVM%20Isolation%20%7C%20Microsoft%20Community%20Hub)
*   [](https://twitter.com/share?text=Hardening%20OpenClaw%20on%20AKS%3A%20Mitigating%20Container%20Escapes%20with%20Kata%20microVM%20Isolation%20%7C%20Microsoft%20Community%20Hub&url=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fcoreinfrastructureandsecurityblog%2Fhardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati%2F4516030)
*   [](https://www.reddit.com/submit?url=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fcoreinfrastructureandsecurityblog%2Fhardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati%2F4516030&title=Hardening%20OpenClaw%20on%20AKS%3A%20Mitigating%20Container%20Escapes%20with%20Kata%20microVM%20Isolation%20%7C%20Microsoft%20Community%20Hub)
*   [](https://bsky.app/intent/compose?text=Hardening%20OpenClaw%20on%20AKS%3A%20Mitigating%20Container%20Escapes%20with%20Kata%20microVM%20Isolation%20%7C%20Microsoft%20Community%20Hub%21%20%F0%9F%A6%8B%0Ahttps%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fcoreinfrastructureandsecurityblog%2Fhardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati%2F4516030)
*   [](https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/Community)
*   [](mailto:?body=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fcoreinfrastructureandsecurityblog%2Fhardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati%2F4516030)

What's new

*   [Surface Pro](https://www.microsoft.com/surface/devices/surface-pro)
*   [Surface Laptop](https://www.microsoft.com/surface/devices/surface-laptop)
*   [Surface Laptop Studio 2](https://www.microsoft.com/d/Surface-Laptop-Studio-2/8rqr54krf1dz)
*   [Copilot for organizations](https://www.microsoft.com/microsoft-copilot/organizations?icid=DSM_Footer_CopilotOrganizations)
*   [Copilot for personal use](https://www.microsoft.com/microsoft-copilot/for-individuals?form=MY02PT&OCID=GE_web_Copilot_Free_868g3t5nj)
*   [AI in Windows](https://www.microsoft.com/windows/ai-features?icid=DSM_Footer_WhatsNew_AIinWindows)
*   [Explore Microsoft products](https://www.microsoft.com/microsoft-products-and-apps)
*   [Windows 11 apps](https://www.microsoft.com/windows/apps-for-windows?icid=DSM_Footer_WhatsNew_Windows11apps)

Microsoft Store

*   [Account profile](https://account.microsoft.com/)
*   [Download Center](https://www.microsoft.com/download)
*   [Microsoft Store support](https://go.microsoft.com/fwlink/?linkid=2139749)
*   [Returns](https://go.microsoft.com/fwlink/p/?LinkID=824764&clcid=0x809)
*   [Order tracking](https://www.microsoft.com/store/b/order-tracking)
*   [Certified Refurbished](https://www.microsoft.com/store/b/certified-refurbished-products)
*   [Microsoft Store Promise](https://www.microsoft.com/store/b/why-microsoft-store?icid=footer_why-msft-store_7102020)
*   [Flexible Payments](https://www.microsoft.com/store/b/payment-financing-options?icid=footer_financing_vcc)

Education

*   [Microsoft in education](https://www.microsoft.com/education)
*   [Devices for education](https://www.microsoft.com/education/devices/overview)
*   [Microsoft Teams for Education](https://www.microsoft.com/education/products/teams)
*   [Microsoft 365 Education](https://www.microsoft.com/education/products/microsoft-365)
*   [How to buy for your school](https://www.microsoft.com/education/how-to-buy)
*   [Educator training and development](https://education.microsoft.com/)
*   [Deals for students and parents](https://www.microsoft.com/store/b/education)
*   [AI for education](https://www.microsoft.com/education/ai-in-education)

Business

*   [Microsoft AI](https://www.microsoft.com/ai?icid=DSM_Footer_AI)
*   [Microsoft Security](https://www.microsoft.com/security)
*   [Dynamics 365](https://www.microsoft.com/dynamics-365)
*   [Microsoft 365](https://www.microsoft.com/microsoft-365/business)
*   [Microsoft Power Platform](https://www.microsoft.com/power-platform)
*   [Microsoft Teams](https://www.microsoft.com/microsoft-teams/group-chat-software)
*   [Microsoft 365 Copilot](https://www.microsoft.com/microsoft-365-copilot?icid=DSM_Footer_Microsoft365Copilot)
*   [Small Business](https://www.microsoft.com/store/b/business?icid=CNavBusinessStore)

Developer & IT

*   [Azure](https://azure.microsoft.com/)
*   [Microsoft Developer](https://developer.microsoft.com/)
*   [Microsoft Learn](https://learn.microsoft.com/)
*   [Support for AI marketplace apps](https://www.microsoft.com/software-development-companies/offers-benefits/isv-success?icid=DSM_Footer_SupportAIMarketplace&ocid=cmm3atxvn98)
*   [Microsoft Tech Community](https://techcommunity.microsoft.com/)
*   [Microsoft Marketplace](https://marketplace.microsoft.com/?icid=DSM_Footer_Marketplace&ocid=cmm3atxvn98)
*   [Marketplace Rewards](https://www.microsoft.com/software-development-companies/offers-benefits/marketplace-rewards?icid=DSM_Footer_MarketplaceRewards&ocid=cmm3atxvn98)
*   [Visual Studio](https://visualstudio.microsoft.com/)

Company

*   [Careers](https://careers.microsoft.com/)
*   [About Microsoft](https://www.microsoft.com/about)
*   [Company news](https://news.microsoft.com/source/?icid=DSM_Footer_Company_CompanyNews)
*   [Privacy at Microsoft](https://www.microsoft.com/privacy?icid=DSM_Footer_Company_Privacy)
*   [Investors](https://www.microsoft.com/investor/default.aspx)
*   [Diversity and inclusion](https://www.microsoft.com/diversity/default?icid=DSM_Footer_Company_Diversity)
*   [Accessibility](https://www.microsoft.com/accessibility)
*   [Sustainability](https://www.microsoft.com/sustainability/)

[Your Privacy Choices](https://aka.ms/yourcaliforniaprivacychoices)[Consumer Health Privacy](https://go.microsoft.com/fwlink/?linkid=2259814)

*   [Sitemap](https://www.microsoft.com/en-us/sitemap1.aspx)
*   [Contact Microsoft](https://support.microsoft.com/contactus)
*   [Privacy](https://go.microsoft.com/fwlink/?LinkId=521839)
*   [Manage cookies](javascript:manageConsent();)
*   [Terms of use](https://go.microsoft.com/fwlink/?LinkID=206977)
*   [Trademarks](https://go.microsoft.com/fwlink/?linkid=2196228)
*   [Safety & eco](https://go.microsoft.com/fwlink/?linkid=2196227)
*   [Recycling](https://www.microsoft.com/legal/compliance/recycling)
*   [About our ads](https://choice.microsoft.com/)
*   © Microsoft 2026

*   [![Image 14: Share to LinkedIn](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/social-share-linkedin.svg?time=1743177821000)Share on LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fcoreinfrastructureandsecurityblog%2Fhardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati%2F4516030)
*   [![Image 15: Share to Facebook](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/social-share-facebook.svg?time=1743177821000)Share on Facebook](https://www.facebook.com/share.php?u=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fcoreinfrastructureandsecurityblog%2Fhardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati%2F4516030&t=Hardening%20OpenClaw%20on%20AKS%3A%20Mitigating%20Container%20Escapes%20with%20Kata%20microVM%20Isolation%20%7C%20Microsoft%20Community%20Hub)
*   [![Image 16: Share to X](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/social-share-x.svg?time=1743177821000)Share on X](https://twitter.com/share?text=Hardening%20OpenClaw%20on%20AKS%3A%20Mitigating%20Container%20Escapes%20with%20Kata%20microVM%20Isolation%20%7C%20Microsoft%20Community%20Hub&url=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fcoreinfrastructureandsecurityblog%2Fhardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati%2F4516030)
*   [![Image 17: Share to Reddit](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/social-share-reddit.svg?time=1743177821000)Share on Reddit](https://www.reddit.com/submit?url=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fcoreinfrastructureandsecurityblog%2Fhardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati%2F4516030&title=Hardening%20OpenClaw%20on%20AKS%3A%20Mitigating%20Container%20Escapes%20with%20Kata%20microVM%20Isolation%20%7C%20Microsoft%20Community%20Hub)
*   [![Image 18: Share to Blue Sky](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/bluesky-brands.svg?time=1743697028000)Share on Bluesky](https://bsky.app/intent/compose?text=Hardening%20OpenClaw%20on%20AKS%3A%20Mitigating%20Container%20Escapes%20with%20Kata%20microVM%20Isolation%20%7C%20Microsoft%20Community%20Hub%21%20%F0%9F%A6%8B%0Ahttps%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fcoreinfrastructureandsecurityblog%2Fhardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati%2F4516030)
*   [![Image 19: Subscribe to RSS](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/rss.svg?time=1743177821000)Share on RSS](https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/Community)
*   [![Image 20: Share to Email](https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/social-share-email.svg?time=1743177821000)Share on Email](mailto:?body=https%3A%2F%2Ftechcommunity.microsoft.com%2Fblog%2Fcoreinfrastructureandsecurityblog%2Fhardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati%2F4516030)

"}},"componentScriptGroups({\"componentId\":\"custom.widget.SocialSharing\"})":{"__typename":"ComponentScriptGroups","scriptGroups":{"__typename":"ComponentScriptGroupsDefinition","afterInteractive":{"__typename":"PageScriptGroupDefinition","group":"AFTER_INTERACTIVE","scriptIds":[]},"lazyOnLoad":{"__typename":"PageScriptGroupDefinition","group":"LAZY_ON_LOAD","scriptIds":[]}},"componentScripts":[]},"component({\"componentId\":\"custom.widget.MicrosoftFooter\"})":{"__typename":"Component","render({\"context\":{\"component\":{\"entities\":[],\"props\":{}},\"page\":{\"entities\":[\"message:4516030\"],\"name\":\"BlogMessagePage\",\"props\":{},\"url\":\"https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030\"}}})":{"__typename":"ComponentRenderResult","html":"

*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/surface/devices/surface-pro\" data-m=\"{"cN":"Footer_WhatsNew_SurfacePro_nav","id":"n1c1c1c1m1r1a2","sN":1,"aN":"c1c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/surface/devices/surface-laptop\" data-m=\"{"cN":"Footer_WhatsNew_SurfaceLaptop_nav","id":"n2c1c1c1m1r1a2","sN":2,"aN":"c1c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/d/Surface-Laptop-Studio-2/8rqr54krf1dz\" data-m=\"{"cN":"Footer_WhatsNew_SurfaceLaptopStudio2_nav","id":"n3c1c1c1m1r1a2","sN":3,"aN":"c1c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/microsoft-copilot/organizations?icid=DSM_Footer_CopilotOrganizations\" data-m=\"{"cN":"Footer_WhatsNew_CopilotOrganizations_nav","id":"n4c1c1c1m1r1a2","sN":4,"aN":"c1c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/microsoft-copilot/for-individuals?form=MY02PT&OCID=GE_web_Copilot_Free_868g3t5nj\" data-m=\"{"cN":"Footer_WhatsNew_CopilotPersonal_nav","id":"n5c1c1c1m1r1a2","sN":5,"aN":"c1c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/windows/ai-features?icid=DSM_Footer_WhatsNew_AIinWindows\" data-m=\"{"cN":"Footer_WhatsNew_AIinWindows_nav","id":"n6c1c1c1m1r1a2","sN":6,"aN":"c1c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/microsoft-products-and-apps\" data-m=\"{"cN":"Footer_WhatsNew_ExploreMicrosoftProducts_nav","id":"n7c1c1c1m1r1a2","sN":7,"aN":"c1c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/windows/apps-for-windows?icid=DSM_Footer_WhatsNew_Windows11apps\" data-m=\"{"cN":"Footer_WhatsNew_Windows11Apps_nav","id":"n8c1c1c1m1r1a2","sN":8,"aN":"c1c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)

*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://account.microsoft.com/\" data-m=\"{"cN":"Footer_StoreandSupport_AccountProfile_nav","id":"n1c2c1c1m1r1a2","sN":1,"aN":"c2c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/download\" data-m=\"{"cN":"Footer_StoreandSupport_DownloadCenter_nav","id":"n2c2c1c1m1r1a2","sN":2,"aN":"c2c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://go.microsoft.com/fwlink/?linkid=2139749\" data-m=\"{"cN":"Footer_StoreandSupport_SalesAndSupport_nav","id":"n3c2c1c1m1r1a2","sN":3,"aN":"c2c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" id=\"footer-returns\" href=\"https://go.microsoft.com/fwlink/p/?LinkID=824764&clcid=0x809\" data-m=\"{"cN":"Footer_StoreandSupport_Returns_nav","id":"n4c2c1c1m1r1a2","sN":4,"aN":"c2c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/store/b/order-tracking\" data-m=\"{"cN":"Footer_StoreandSupport_OrderTracking_nav","id":"n5c2c1c1m1r1a2","sN":5,"aN":"c2c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/store/b/certified-refurbished-products\" data-m=\"{"cN":"Footer_StoreandSupport_CertifiedRefurbished_nav","id":"n6c2c1c1m1r1a2","sN":6,"aN":"c2c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/store/b/why-microsoft-store?icid=footer_why-msft-store_7102020\" data-m=\"{"cN":"Footer_StoreandSupport_MicrosoftPromise_nav","id":"n7c2c1c1m1r1a2","sN":7,"aN":"c2c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/store/b/payment-financing-options?icid=footer_financing_vcc\" data-m=\"{"cN":"Footer_StoreandSupport_Financing_nav","id":"n8c2c1c1m1r1a2","sN":8,"aN":"c2c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)

*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/education\" data-m=\"{"cN":"Footer_Education_MicrosoftInEducation_nav","id":"n1c3c1c1m1r1a2","sN":1,"aN":"c3c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/education/devices/overview\" data-m=\"{"cN":"Footer_Education_DevicesforEducation_nav","id":"n2c3c1c1m1r1a2","sN":2,"aN":"c3c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/education/products/teams\" data-m=\"{"cN":"Footer_Education_MicrosoftTeamsforEducation_nav","id":"n3c3c1c1m1r1a2","sN":3,"aN":"c3c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/education/products/microsoft-365\" data-m=\"{"cN":"Footer_Education_Microsoft365Education_nav","id":"n4c3c1c1m1r1a2","sN":4,"aN":"c3c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/education/how-to-buy\" data-m=\"{"cN":"Footer_Education_HowToBuy_nav","id":"n5c3c1c1m1r1a2","sN":5,"aN":"c3c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://education.microsoft.com/\" data-m=\"{"cN":"Footer_Education_EducatorTrainingDevelopment_nav","id":"n6c3c1c1m1r1a2","sN":6,"aN":"c3c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/store/b/education\" data-m=\"{"cN":"Footer_Education_DealsForStudentsandParents_nav","id":"n7c3c1c1m1r1a2","sN":7,"aN":"c3c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/education/ai-in-education\" data-m=\"{"cN":"Footer_Education_AIinEducation_nav","id":"n8c3c1c1m1r1a2","sN":8,"aN":"c3c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)

*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/ai?icid=DSM_Footer_AI\" data-m=\"{"cN":"Footer_Business_MicrosoftAI_nav","id":"n1c4c1c1m1r1a2","sN":1,"aN":"c4c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/security\" data-m=\"{"cN":"Footer_Business_MicrosoftSecurity_nav","id":"n2c4c1c1m1r1a2","sN":2,"aN":"c4c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/dynamics-365\" data-m=\"{"cN":"Footer_Business_MicrosoftDynamics365_nav","id":"n3c4c1c1m1r1a2","sN":3,"aN":"c4c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/microsoft-365/business\" data-m=\"{"cN":"Footer_Business_Microsoft365_nav","id":"n4c4c1c1m1r1a2","sN":4,"aN":"c4c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/power-platform\" data-m=\"{"cN":"Footer_Business_MicrosoftPowerPlatform_nav","id":"n5c4c1c1m1r1a2","sN":5,"aN":"c4c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/microsoft-teams/group-chat-software\" data-m=\"{"cN":"Footer_Business_MicrosoftTeams_nav","id":"n6c4c1c1m1r1a2","sN":6,"aN":"c4c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/microsoft-365-copilot?icid=DSM_Footer_Microsoft365Copilot\" data-m=\"{"cN":"Footer_Business_Microsoft365Copilot_nav","id":"n7c4c1c1m1r1a2","sN":7,"aN":"c4c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/store/b/business?icid=CNavBusinessStore\" data-m=\"{"cN":"Footer_Business_SmallBusiness_nav","id":"n8c4c1c1m1r1a2","sN":8,"aN":"c4c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)

*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://azure.microsoft.com/\" data-m=\"{"cN":"Footer_Enterprise_MicrosoftAzure_nav","id":"n1c5c1c1m1r1a2","sN":1,"aN":"c5c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://developer.microsoft.com/\" data-m=\"{"cN":"Footer_Developer_DeveloperCenter_nav","id":"n2c5c1c1m1r1a2","sN":2,"aN":"c5c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://learn.microsoft.com/\" data-m=\"{"cN":"Footer_DeveloperAndIT_MicrosoftLearn_nav","id":"n3c5c1c1m1r1a2","sN":3,"aN":"c5c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/software-development-companies/offers-benefits/isv-success?icid=DSM_Footer_SupportAIMarketplace&ocid=cmm3atxvn98\" data-m=\"{"cN":"Footer_DeveloperAndIT_SupportAIMarketplace_nav","id":"n4c5c1c1m1r1a2","sN":4,"aN":"c5c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://techcommunity.microsoft.com/\" data-m=\"{"cN":"Footer_DeveloperAndIT_MicrosoftTechCommunity_nav","id":"n5c5c1c1m1r1a2","sN":5,"aN":"c5c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://marketplace.microsoft.com/?icid=DSM_Footer_Marketplace&ocid=cmm3atxvn98\" data-m=\"{"cN":"Footer_DeveloperAndIT_Marketplace_nav","id":"n6c5c1c1m1r1a2","sN":6,"aN":"c5c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/software-development-companies/offers-benefits/marketplace-rewards?icid=DSM_Footer_MarketplaceRewards&ocid=cmm3atxvn98\" data-m=\"{"cN":"Footer_DeveloperAndIT_MarketplaceRewards_nav","id":"n7c5c1c1m1r1a2","sN":7,"aN":"c5c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://visualstudio.microsoft.com/\" data-m=\"{"cN":"Footer_Developer_MicrosoftVisualStudio_nav","id":"n8c5c1c1m1r1a2","sN":8,"aN":"c5c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)

*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://careers.microsoft.com/\" data-m=\"{"cN":"Footer_Company_Careers_nav","id":"n1c6c1c1m1r1a2","sN":1,"aN":"c6c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/about\" data-m=\"{"cN":"Footer_Company_AboutMicrosoft_nav","id":"n2c6c1c1m1r1a2","sN":2,"aN":"c6c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://news.microsoft.com/source/?icid=DSM_Footer_Company_CompanyNews\" data-m=\"{"cN":"Footer_Company_CompanyNews_nav","id":"n3c6c1c1m1r1a2","sN":3,"aN":"c6c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/privacy?icid=DSM_Footer_Company_Privacy\" data-m=\"{"cN":"Footer_Company_PrivacyAtMicrosoft_nav","id":"n4c6c1c1m1r1a2","sN":4,"aN":"c6c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/investor/default.aspx\" data-m=\"{"cN":"Footer_Company_Investors_nav","id":"n5c6c1c1m1r1a2","sN":5,"aN":"c6c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/diversity/default?icid=DSM_Footer_Company_Diversity\" data-m=\"{"cN":"Footer_Company_DiversityAndInclusion_nav","id":"n6c6c1c1m1r1a2","sN":6,"aN":"c6c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/accessibility\" data-m=\"{"cN":"Footer_Company_Accessibility_nav","id":"n7c6c1c1m1r1a2","sN":7,"aN":"c6c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)
*   [</li:i18n>\" class=\"c-uhff-link\" href=\"https://www.microsoft.com/sustainability/\" data-m=\"{"cN":"Footer_Company_Sustainability_nav","id":"n8c6c1c1m1r1a2","sN":8,"aN":"c6c1c1m1r1a2"}\">](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)

[](https://techcommunity.microsoft.com/%22https://aka.ms/yourcaliforniaprivacychoices/%22)[](https://techcommunity.microsoft.com/%22https://go.microsoft.com/fwlink/?linkid=2259814\%22)

*   [](https://techcommunity.microsoft.com/%22https://www.microsoft.com/en-us/sitemap1.aspx/%22)
*   [](https://techcommunity.microsoft.com/%22https://support.microsoft.com/contactus/%22)
*   [](https://techcommunity.microsoft.com/%22https://go.microsoft.com/fwlink/?LinkId=521839\%22)
*   [](https://techcommunity.microsoft.com/%22javascript:manageConsent();/%22)
*   [](https://techcommunity.microsoft.com/%22https://go.microsoft.com/fwlink/?LinkID=206977\%22)
*   [](https://techcommunity.microsoft.com/%22https://go.microsoft.com/fwlink/?linkid=2196228\%22)
*   [](https://techcommunity.microsoft.com/%22https://go.microsoft.com/fwlink/?linkid=2196227\%22)
*   [](https://techcommunity.microsoft.com/%22https://www.microsoft.com/legal/compliance/recycling/%22)
*   [](https://techcommunity.microsoft.com/%22https://choice.microsoft.com/%22)
*   © 

*   [![Image 21: \"<li:i18n](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)</li:i18n>\" src=\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/social-share-linkedin.svg?time=1743177821000\">](https://techcommunity.microsoft.com/%22https://www.linkedin.com/sharing/share-offsite/?url=page.url\%22)
*   [![Image 22: \"<li:i18n](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)</li:i18n>\" src=\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/social-share-facebook.svg?time=1743177821000\">](https://techcommunity.microsoft.com/%22https://www.facebook.com/share.php?u=page.url&t=page-name\%22)
*   [![Image 23: \"<li:i18n](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)</li:i18n>\" src=\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/social-share-x.svg?time=1743177821000\">](https://techcommunity.microsoft.com/%22https://twitter.com/share?text=page-name&url=page.url\%22)
*   [![Image 24: \"<li:i18n](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)</li:i18n>\" src=\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/social-share-reddit.svg?time=1743177821000\">](https://techcommunity.microsoft.com/%22https://www.reddit.com/submit?url=page.url&title=page-name\%22)
*   [![Image 25: \"<li:i18n](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)</li:i18n>\" src=\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/bluesky-brands.svg?time=1743697028000\">](https://techcommunity.microsoft.com/%22https://bsky.app/intent/compose?text=page-name%21%20%F0%9F%A6%8B%0Apage.url\%22)
*   [![Image 26: \"<li:i18n](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)</li:i18n>\" src=\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/rss.svg?time=1743177821000\">](https://techcommunity.microsoft.com/%22/t5/s/gxcuf89792/rss/Community/%22)
*   [![Image 27: \"<li:i18n](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/hardening-openclaw-on-aks-mitigating-container-escapes-with-kata-microvm-isolati/4516030)</li:i18n>\" src=\"https://techcommunity.microsoft.com/t5/s/gxcuf89792/m_assets/components/MicrosoftFooter/assets/social-share-email.svg?time=1743177821000\">](https://techcommunity.microsoft.com/%22mailto:?body=page.url\%22)

"}},"componentScriptGroups({\"componentId\":\"custom.widget.MicrosoftFooter\"})":{"__typename":"ComponentScriptGroups","scriptGroups":{"__typename":"ComponentScriptGroupsDefinition","afterInteractive":{"__typename":"PageScriptGroupDefinition","group":"AFTER_INTERACTIVE","scriptIds":[]},"lazyOnLoad":{"__typename":"PageScriptGroupDefinition","group":"LAZY_ON_LOAD","scriptIds":[]}},"componentScripts":[]},"cachedText({\"lastModified\":\"1780328570731\",\"locale\":\"en-US\",\"namespaces\":[\"components/community/NavbarDropdownToggle\"]})":[{"__ref":"CachedAsset:text:en_US-components/community/NavbarDropdownToggle-1780328570731"}],"cachedText({\"lastModified\":\"1780328570731\",\"locale\":\"en-US\",\"namespaces\":[\"components/messages/MessageCoverImage\"]})":[{"__ref":"CachedAsset:text:en_US-components/messages/MessageCoverImage-1780328570731"}],"cachedText({\"lastModified\":\"1780328570731\",\"locale\":\"en-US\",\"namespaces\":[\"shared/client/components/nodes/NodeTitle\"]})":[{"__ref":"CachedAsset:text:en_US-shared/client/components/nodes/NodeTitle-1780328570731"}],"cachedText({\"lastModified\":\"1780328570731\",\"locale\":\"en-US\",\"namespaces\":[\"components/messages/MessageTimeToRead\"]})":[{"__ref":"CachedAsset:text:en_US-components/messages/MessageTimeToRead-1780328570731"}],"cachedText({\"lastModified\":\"1780328570731\",\"locale\":\"en-US\",\"namespaces\":[\"components/messages/MessageSubject\"]})":[{"__ref":"CachedAsset:text:en_US-components/messages/MessageSubject-1780328570731"}],"cachedText({\"lastModified\":\"1780328570731\",\"locale\":\"en-US\",\"namespaces\":[\"components/users/UserLink\"]})":[{"__ref":"CachedAsset:text:en_US-components/users/UserLink-1780328570731"}],"cachedText({\"lastModified\":\"1780328570731\",\"locale\":\"en-US\",\"namespaces\":[\"shared/client/components/users/UserRank\"]})":[{"__ref":"CachedAsset:text:en_US-shared/client/components/users/UserRank-1780328570731"}],"cachedText({\"lastModified\":\"1780328570731\",\"locale\":\"en-US\",\"namespaces\":[\"components/messages/MessageTime\"]})":[{"__ref":"CachedAsset:text:en_US-components/messages/MessageTime-1780328570731"}],"cachedText({\"lastModified\":\"1780328570731\",\"locale\":\"en-US\",\"namespaces\":[\"components/messages/MessageBody\"]})":[{"__ref":"CachedAsset:text:en_US-components/messages/MessageBody-1780328570731"}],"cachedText({\"lastModified\":
