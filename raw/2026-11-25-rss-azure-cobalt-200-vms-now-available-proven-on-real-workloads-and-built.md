---
source: "https://azure.microsoft.com/en-us/blog/azure-cobalt-200-vms-now-available-proven-on-real-workloads-and-built-for-the-agentic-era/"
title: "Azure Cobalt 200 VMs now available, proven on real workloads and built for the agentic era"
author: "Rani Borkar"
date_published: "2026-11-17"
date_clipped: "2026-11-25"
category: "Azure & Cloud"
source_type: "rss"
---

# Azure Cobalt 200 VMs now available, proven on real workloads and built for the agentic era

Today at Microsoft Ignite 2026, we’re announcing the **general availability of [Azure Cobalt 200-based virtual machines (VMs)](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/cobalt-overview)**.

Cobalt 200 VMs deliver **up to 50% better performance than Cobalt 100** and are now available in 14 regions, expanding to **23 regions** by the end of 2026. Built for cloud-native, data-intensive, and agentic AI workloads, Cobalt 200 VMs will represent **a significant share of new Azure Compute capacity** beginning in 2027.

[Explore Cobalt 200 VM sizes and deployment guidance](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/cobalt-overview)

For customers like **Amadeus, Databricks, InMobi, OpenAI, and Snowflake**, Cobalt 200 VMs deliver improved performance and efficiency over Cobalt 100 VMs. As a result, customers can deliver faster search results, more responsive database queries, and run their services at higher utilization with fewer cores.

## Cobalt 200 VMs deliver up to 50% better performance than Cobalt 100

[Read the blog ›](https://azure.microsoft.com/en-us/blog/new-azure-cobalt-200-vms-deliver-50-performance-improvement-fully-optimized-for-modern-agentic-ai-workloads/)

Cobalt 200’s performance and efficiency gains reflect our systems approach to infrastructure design, which co-optimizes silicon, software, networking, power, and rack infrastructure. Cobalt 200 VMs are also designed for agentic AI workflows, including agent sandboxes, file search, code compilation, and tool execution, where higher per-core performance can help reduce latency.

As customer need for high-performance and low-latency compute increases, we’re adding new virtual machine types to bring the price-performance benefits of Cobalt to additional workloads:

- Mpsv4 for high memory workloads.
- Lpsv5 for workloads needing fast access to large datasets.

With [Microsoft Azure Boost](https://azure.microsoft.com/en-us/products/virtual-machines/boost) included in every Cobalt 200 VM, customers get the latest accelerated network and remote storage performance in [Microsoft Azure](http://azure.microsoft.com).

## Proven on critical customer workloads

Our benchmarking for Cobalt 200 VMs showed significant performance increases for a wide variety of workloads. We observed up to 1.5 times increased performance for web serving workloads, up to 1.6 times for Java-based workloads, up to 1.5 times for AI agent tool execution workloads, and 1.9 times for database workloads over Cobalt 100.

We’ve seen these results translate into real-world improvements as our customers bring [Cobalt 200 VMs](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/cobalt-overview) to their own workloads.

See what customers are saying about Cobalt 200 VMs
> Cobalt has helped us sustain ChatGPT’s growth. Cobalt 100 gave us more CPU capacity when we needed it. By the time we tested Cobalt 200, our services already ran on ARM, so we could compare the same ChatGPT workloads on both generations. We saw higher throughput and lower latency on Cobalt 200. That means we can serve more users with the same number of cores, and they spend less time waiting for ChatGPT to start responding.
>
> —**Vadim Filanovsky, Member of Technical Staff, OpenAI**

> Genie, the data-smart AI coworker, puts answers in front of business users in plain language, and those answers depend on fast, efficient compute underneath. Azure Cobalt helps us deliver that. Azure Databricks serverless compute on Cobalt starts faster and runs more efficiently, so customers spend less time waiting and more time acting on their data. Cobalt 200 raises the bar again, and as we bring more of Azure Databricks onto it, Genie questions, SQL queries, and data pipelines get faster.
>
> **—Vinod Marur, SVP Engineering, Databricks**

> Snowflake has grown with Arm on Azure, from the first Arm-based v5 VMs to Cobalt 100 and now Cobalt 200. Each generation has brought real performance and efficiency gains for our workloads, and those gains help us give our customers an even better experience. We’re proud to partner with Microsoft on what comes next for Cobalt and excited to see Cobalt 200 reach general availability.
>
> **—Murray Stokely, Distinguished Engineer, Snowflake**

> Performance at scale is at the heart of how Amadeus serves the travel industry. In our benchmark lab, Azure Cobalt 200 improved flight search throughput by more than 30% compared with Cobalt 100, a performance gain that exceeded our expectations.
>
> **—Luc Choubert, VP Engineering, Amadeus**

> We tested our ad-serving workloads on Cobalt 200 and saw clear performance and efficiency improvements. In addition to traditional workload patterns, we run high-throughput local neural network inference using SIMD, with each 32-core machine processing approximately 50,000 inferences per second. At the scale of a large fleet, these per-machine efficiency gains compound significantly, making Cobalt 200 particularly compelling for our workloads.
>
> **—Sudheer Bhat, Principal Engineer, InMobi**

Partner endorsements
> Microsoft’s continued investment in Cobalt demonstrates the value of building cloud infrastructure on Arm. Our collaboration on Cobalt 200 brings together Arm Neoverse CSS V3 and Microsoft’s custom silicon innovation to deliver the high performance and efficiency needed for everything from enterprise applications to agentic AI.
>
> —Mohamed Awad, EVP, Cloud AI, Arm

> Cobalt 200 VMs bring the performance and efficiency that agentic AI and data workloads need in production. Ubuntu supports Arm as a first-class architecture, so teams deploy Ubuntu on Cobalt 200 VMs the way they already do across Azure. Ubuntu Pro keeps those systems patched and supported for the long term. On Ubuntu 26.04 LTS, that includes Kernel Livepatch, which applies high and critical kernel fixes on Arm-based VMs without a reboot.
>
> —Cindy Goldberg, VP, Cloud and Silicon Partnerships, Canonical

## Improving efficiency at Microsoft scale

Microsoft products and services, including [Azure Database for PostgreSQL](https://azure.microsoft.com/en-us/products/postgresql/), [Azure DevOps](https://azure.microsoft.com/en-us/products/devops), [Azure SQL](https://azure.microsoft.com/en-us/products/azure-sql), [Microsoft 365](https://www.microsoft.com/en-us/microsoft-365/what-is-microsoft-365), [XBOX](https://www.xbox.com/en-US/), and more, run on Cobalt VMs for increased performance, improved efficiency, and cost savings at scale.

### Accelerating cloud database workloads

Cobalt 200 was designed to deliver high-performance for database workloads, and at Microsoft Build 2026, we announced the availability of [Azure Database for PostgreSQL on Cobalt 200](https://techcommunity.microsoft.com/blog/adforpostgresql/more-power-more-resilience-better-value-azure-database-for-postgresql-at-ignite-/4573613). Cobalt 200 VMs provide scalable performance, memory capacity, and local storage needed to accelerate Azure Database for PostgreSQL.

### Advancing custom silicon development

Microsoft’s silicon engineers run EDA workloads for design verification, physical implementation, and sign-off, and they benchmarked many of those workloads on Cobalt 200 VMs. The team reported [increased performance and efficiency with Cobalt 200](https://aka.ms/cobalt200-eda), with performance between 1.3 and 4.15 times over Cobalt 100. The increased performance allows the team to run more test cases in the same amount of time, supporting the development of more advanced Maia and Cobalt silicon.

### Speeding up developer workflows

Every second counts when developers are waiting on a build. [Cobalt 200 VMs](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/cobalt-overview) allow GitHub Actions larger Arm runners to finish jobs noticeably faster than on Cobalt 100. Across the millions of workflows run every day, those gains add up to faster feedback for developers and more efficient use of compute.

### Gaming

XBOX evaluated [Cobalt 200 VMs](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fazure%2Fvirtual-machines%2Fsizes%2Fcobalt-overview&data=05%7C02%7Cv-kristingal%40microsoft.com%7C16b82a26282643de164b08df441881e1%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C639304544213941519%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=mT%2FxRGoFa7TMfFVerxtFfQKuJqshIsnJB7wXTIKJyDY%3D&reserved=0) on its web service and caching layer, the behind-the-scenes building blocks that help players sign in, see what their friends are playing and jump into games more quickly. Running natively on Arm, XBOX achieved improved performance and efficiency compared to their current infrastructure, a jump that matters in gaming for delivering fast and reliable gameplay.

### Scaling media processing

The media processing service running video for [Microsoft Teams](https://www.microsoft.com/en-us/microsoft-teams/group-chat-software) observed 1.65 times the performance on Cobalt 200 compared with Cobalt 100, allowing them to further optimize their capacity needs to serve customers. Testing also showed linear scaling across Cobalt 200 physical cores, with vCPU utilization reaching up to 90% while serving traffic.

## Compute designed for agents, powered by custom systems

Modern AI applications have evolved from simple inference-based chat interfaces to complex reasoning and agentic systems requiring high-performance compute infrastructure paired with AI acceleration. Cobalt 200 is optimized from the lowest levels of the silicon to the overall rack and system architecture for the demands of agentic compute.

![Azure Cobalt 200 server board](https://azure.microsoft.com/en-us/blog/wp-content/uploads/2026/11/Azure-Cobalt-200-image-03-1024x576.jpg)

Azure Cobalt 200 server board

At the center of every [Cobalt 200 VM](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/cobalt-overview) is the Cobalt 200 system-on-chip (SoC). Built on TSMC’s advanced 3nm process technology to deliver optimal performance and efficiency, the Cobalt 200 SoC brings together 132 Arm Neoverse V3 cores, with a multi-chipset architecture, and advanced packaging.

- **Compute**: Each vCPU is a full physical core, with 3MB of private L2 cache, and 192 MB of system-level cache, helping provide consistent performance under load while keeping recently accessed data close to the core.
- **Memory**: Cobalt 200 features a custom memory controller with 12 channels of DDR5 and enables memory encryption by default with negligible latency.
- **Networking and storage**: Cobalt 200 VMs include the latest version of Azure Boost, moving networking and storage processing off the host, delivering up to 15% higher network bandwidth, 20% higher remote storage IOPS, and 10% higher remote storage throughput compared with Cobalt 100.
- **Security**: Every Cobalt 200 server includes the [Azure Integrated HSM](https://learn.microsoft.com/en-us/azure/security/fundamentals/azure-integrated-hardware-security-module-overview) which protects the server hardware from unauthorized intrusion and enables protected encryption key storage for hosted workloads.
- **Acceleration**: Integrated compression and cryptography accelerators enable Microsoft workloads to reduce CPU consumption by offloading common tasks to specialized low-power silicon. On-chip accelerators will help reduce Azure SQL backup times by up to 2.5 times while minimizing disruption to the live workload.

## Expanding choice and control

**Predictable performance or peak performance**. [Cobalt 200 VMs](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/cobalt-overview) support two processor modes.

1. **Deterministic Mode** runs cores at a consistent 3.2 GHz.
2. **Opportunistic Mode** can boost cores up to 3.6 GHz when power and thermal headroom allow—delivering up to 12% more performance at the expense of some frequency variability.

Different customers have different needs. **Deterministic Mode** suits distributed data and analytics clusters which run at the pace of their slowest node, and services with tight performance targets. **Opportunistic Mode** suits web and API services, transaction processing, and media workloads, where speed matters more than consistency.

Use the ProcessorMode setting to choose deterministic or opportunistic mode when you create a VM or later through the Azure portal, [Microsoft Azure CLI](https://learn.microsoft.com/en-us/cli/azure/what-is-azure-cli?view=azure-cli-latest), [PowerShell](https://learn.microsoft.com/en-us/powershell/), or [Azure Resource Manager](https://azure.microsoft.com/en-us/get-started/azure-portal/resource-manager) and Biceptemplates.

## Cobalt 200 VM sizes and workload options

**More shapes for more workloads**. [Cobalt 200 VMs](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/cobalt-overview) are available in five VM series, across general purpose, memory-optimized, high-memory, and storage-optimized families. Cobalt 200 adds two new VM families for Arm-based compute on Azure:

- **High-memory Mpsv4**—with 16 GiB of memory per vCPU for large in-memory databases, ERP systems, large caches, and memory-intensive analytics.
- **Storage-optimized Lpsv5**—with large local NVMe storage and up to 23 TB per VM for data staging, search and indexing, and databases that need fast local storage.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **VM series** | **vCPUs** | **Memory per vCPU** | **Max memory** | **Local NVMe storage** | **Max network bandwidth** | **Max remote storage throughput** | **Best-fit workloads** |
| **General purpose: Dplsv7 and Dpldsv7** | 1 to 128 | 2 GiB | 256 GiB | Dpldsv7: up to 7,040 GiB | Up to 85 Gbps | Up to 70 Gbps | Microservices, small databases, caches, gaming servers, media encoding, and other non-memory-intensive scale-out workloads |
| **General purpose: Dpsv7 and Dpdsv7** | 1 to 128 | 4 GiB | 512 GiB | Dpdsv7: up to 7,040 GiB | Up to 85 Gbps | Up to 70 Gbps | Web and application servers, agentic AI services (agent orchestration, tool sandboxes), small to medium databases, caches, and scale-out enterprise workloads. |
| **Memory optimized: Epsv7 and Epdsv7** | 1 to 128 | 8 GiB | 1,024 GiB | Epdsv7: up to 7,040 GiB | Up to 85 Gbps | Up to 70 Gbps | Large relational and NoSQL databases, in-memory caches (Redis, Memcached), vector search and agent memory stores for agentic AI, real-time analytics, memory-intensive EDA |
| **(New) High-memory optimized: Mpsv4 and Mpdsv4** | 1 to 84,128 | 16 GiB | 1,388 GiB | Mpdsv4: up to 7,040 GiB | Up to 85 Gbps | Up to 70 Gbps | Large in-memory databases, ERP systems, caching layers, large-scale vector search for agentic AI, memory-intensive analytics |
| **(New) Storage optimized: Lpsv5** | 1 to 128 | 8 GiB | 1,024 GiB | Every size, up to 23 TB | Up to 85 Gbps | Up to 70 Gbps | AI training data preparation and staging, databases needing local storage, big data analytics, search and index engines |

**Regional availability**: Cobalt 200 VMs are generally available today in 14 Azure regions: Australia East, Canada Central, Central US, East US, East US 2, Indonesia Central, Italy North, Korea Central, South Central US, Spain Central, Sweden Central, UK South, West US 2, and West US 3. Availability will expand to 23 regions by the end of 2026.

For the latest regional availability, see [Products Available by Region](https://aka.ms/product-by-region).

![Servers](https://azure.microsoft.com/en-us/blog/wp-content/uploads/2026/11/Cobalt-1024x576.webp)

## Get started with Azure Cobalt 200 VMs

Cobalt 200 is the next chapter of Arm-based compute on Azure, delivering our highest-performing and leading price-performance general purpose VMs.

Getting started is simple—workloads already running on Cobalt 100 can easily move to [Cobalt 200 VMs](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/cobalt-overview) where they need the additional performance, larger VM sizes, or new VM families.

The Arm software ecosystem has matured alongside our infrastructure. Cobalt 200 VMs are supported by popular Linux distributions, [Azure Kubernetes Service](https://azure.microsoft.com/en-us/products/kubernetes-service) (AKS), and multiple deployment and containerization frameworks.

Cobalt 200 currently supports the following operating systems:

|  |  |  |
| --- | --- | --- |
| AlmaLinux | Oracle Linux | SUSE Linux Enterprise Server |
| Azure Linux | Red Hat Enterprise Linux | Ubuntu |
| Debian | Rocky Linux | Windows 11 Client |

You can deploy Cobalt 200 VMs with the Azure portal, SDKs, APIs, PowerShell, and the Azure CLI, and use them with Virtual Machine Scale Sets and as AKS node pools.

## Build with Cobalt today

- Learn about Cobalt 200 VM [sizes and deployment guidance](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/cobalt-overview).
- Learn about [Azure Compute VM pricing](https://azure.microsoft.com/en-us/pricing).
- Watch our Microsoft Ignite 2026 session BRK440. [Cobalt 200: Delivering Azure’s best performance and efficiency](https://aka.ms/BRK440).
- Learn more about Microsoft Azure infrastructure, [from silicon to systems](http://aka.ms/silicontosystems).
- Learn about [Arm64-based computing in the cloud](https://aka.ms/Cobalt200VMs-GA-Arm) from Arm.
  - Linux server software for Arm, with recommended versions, in the [Software Ecosystem Dashboard for Arm](https://developer.arm.com/ecosystem-dashboard/linux).
  - Windows server software for Arm, with recommended versions, in the [Software Ecosystem Dashboard for Arm](https://developer.arm.com/ecosystem-dashboard/windows).
- Learn about [Linux readiness for Cobalt 200](https://aka.ms/Cobalt200VMs-GA-Canonical) from Canonical.
- For additional questions, contact [Azure support](https://azure.microsoft.com/support) or your Microsoft account team.
