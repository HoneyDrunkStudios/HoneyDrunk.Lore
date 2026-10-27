---
source: "https://learn.microsoft.com/en-us/azure/container-apps/health-probes"
title: "Health probes in Azure Container Apps"
author: "craigshoemaker"
date_published: "unknown"
category: "Azure & Cloud"
source_type: "web"
date_clipped: "2026-10-26"
---

# Health probes in Azure Container Apps

Azure Container Apps health probes let the Container Apps runtime regularly check the status of your container apps.

You can set up probes by using either TCP or HTTP(S) exclusively.

Azure Container Apps supports the following probes:

| Probe | Description |
| --- | --- |
| Startup | Checks if your application starts successfully. This check is separate from the liveness probe and runs during the initial startup phase of your application. |
| Liveness | Checks if your application is still running and responsive. |
| Readiness | Checks if a replica is ready to handle incoming requests. |

For a full list of the probe specifications supported in Azure Container Apps, see [Azure REST API specs](https://github.com/Azure/azure-rest-api-specs/blob/main/specification/app/resource-manager/Microsoft.App/ContainerApps/stable/2025-07-01/CommonDefinitions.json).

## HTTP probes

HTTP probes let you implement custom logic to check the status of application dependencies before reporting a healthy status.

Configure your health probe endpoints to respond with an HTTP status code greater than or equal to `200` and less than `400` to indicate success. Any other response code outside this range indicates a failure.

The following example shows how to implement a liveness endpoint in JavaScript.

```
const express = require('express');
const app = express();

app.get('/liveness', (req, res) => {
  let isSystemStable = false;
  
  // check for database availability
  // check filesystem structure
  //  etc.

  // set isSystemStable to true if all checks pass

  if (isSystemStable) {
    res.status(200); // Success
  } else {
    res.status(503); // Service unavailable
  }
})
```

## TCP probes

TCP probes wait to establish a connection with the server to indicate success. The probe fails if it can't establish a connection to your application.

## Restrictions

- You can add only one of each probe type per container.
- `exec` probes aren't supported.
- Port values must be integers; named ports aren't supported.
- gRPC isn't supported.

## Examples

The following code listing shows how you can define health probes for your containers.

The `...` placeholders denote omitted code. For full ARM template details, see [Container Apps ARM template API specification](https://learn.microsoft.com/en-us/azure/container-apps/azure-resource-manager-api-spec).

- [ARM template](#tabpanel_1_arm-template)
- [YAML](#tabpanel_1_yaml)

```
{
  ...
  "containers":[
    {
      "image":"nginx",
      "name":"web",
      "probes": [
        {
          "type": "Liveness",
          "httpGet": {
            "path": "/health",
            "port": 8080,
            "httpHeaders": [
              {
                "name": "Custom-Header",
                "value": "liveness probe"
              }]
          },
          "initialDelaySeconds": 7,
          "periodSeconds": 3
        },
        {
          "type": "Readiness",
          "tcpSocket": {
            "port": 8081
          },
          "initialDelaySeconds": 10,
          "periodSeconds": 3
        },
        {
          "type": "Startup",
          "httpGet": {
            "path": "/startup",
            "port": 8080,
            "httpHeaders": [
              {
                "name": "Custom-Header",
                "value": "startup probe"
              }]
          },
          "initialDelaySeconds": 3,
          "periodSeconds": 3
        }]
    }]
  ...
}
```

```
...
containers:
  - image: nginx
    name: web
    probes:
      - type: Liveness
        httpGet:
          path: "/health"
          port: 8080
          httpHeaders:
            - name: Custom-Header
              value: "liveness probe"
        initialDelaySeconds: 7
        periodSeconds: 3
      - type: Readiness
        tcpSocket:
          port: 8081
        initialDelaySeconds: 10
        periodSeconds: 3
      - type: Startup
        httpGet:
          path: "/startup"
          port: 8080
          httpHeaders:
            - name: Custom-Header
              value: "startup probe"
        initialDelaySeconds: 3
        periodSeconds: 3
...
```

The optional `failureThreshold` setting defines the number of attempts Container Apps tries to execute the probe if execution fails. Attempts that exceed the `failureThreshold` amount cause different results for each probe type.

## Default configuration

If you enable ingress, the portal automatically adds the following default probes to the main app container if you don't define each type, except for GPU workload profiles (both dedicated and consumption). The portal doesn't automatically add default probes to [sidecar containers](https://learn.microsoft.com/en-us/azure/container-apps/containers#sidecar-containers).

| Probe type | Default values |
| --- | --- |
| Startup | Protocol: TCP Port: ingress target port Timeout: 3 seconds Period: 1 second Initial delay: 1 second Success threshold: One Failure threshold: 240 |
| Liveness | Protocol: TCP Port: ingress target port |
| Readiness | Protocol: TCP Port: ingress target port Timeout: 5 seconds Period: 5 seconds Initial delay: 3 seconds Success threshold: One Failure threshold: 48 |

If you run your container app in [multiple revision mode](https://learn.microsoft.com/en-us/azure/container-apps/revisions#revision-modes), after you deploy a revision, wait until your readiness probes indicate success before you shift traffic to that revision. In single revision mode, traffic shifts automatically once the readiness probe returns a successful state.

A revision state appears as unhealthy if any of its replicas fails its readiness probe check, even if all other replicas in the revision are healthy. Container Apps restarts the replica in question until it's healthy again or the failure threshold is exceeded. If the failure threshold is exceeded, try restarting the revision, but it might mean the revision isn't configured correctly.

If your app requires a long startup time, adjust the probe settings to prevent the container from being restarted (or marked as unhealthy) before it's ready. Customizing the probe configuration helps ensure your app has enough time to start without triggering unnecessary restarts.

The following example demonstrates how to configure the liveness and readiness probes to extend the startup times.

```
"probes": [
       {
        "type": "Liveness",
        "failureThreshold": 3,
        "periodSeconds": 10,
        "successThreshold": 1,
        "tcpSocket": {
          "port": 80
        },
        "timeoutSeconds": 1
       },
       {
         "type": "Readiness",
         "failureThreshold": 48,
         "initialDelaySeconds": 3,
         "periodSeconds": 5,
         "successThreshold": 1,
         "tcpSocket": {
           "port": 80
          },
          "timeoutSeconds": 5
       }]
```

## Next steps

[Application logging](https://learn.microsoft.com/en-us/azure/container-apps/logging)
