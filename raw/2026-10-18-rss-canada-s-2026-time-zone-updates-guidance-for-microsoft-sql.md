---
source: "https://devblogs.microsoft.com/azure-sql/canadas-2026-time-zone-updates-guidance-for-microsoft-sql"
title: "Canada’s 2026 time zone updates: guidance for Microsoft SQL"
author: "Umachandar Jayachandran"
date_published: "2026-10-15"
date_clipped: "2026-10-18"
category: "Azure & Cloud"
source_type: "rss"
---

# Canada’s 2026 time zone updates: guidance for Microsoft SQL

Affected locations in British Columbia, Alberta, and Manitoba will **not turn their clocks back at 02:00 local time on November 1, 2026**. They will remain at UTC−07:00, UTC−06:00, and UTC−05:00, respectively. 

Microsoft’s interim guidance for [British Columbia](https://techcommunity.microsoft.com/blog/dstblog/interim-guidance-for-british-columbia-time-zone-changes-2026/4544988), [Alberta](https://techcommunity.microsoft.com/blog/dstblog/interim-guidance-for-alberta-time-zone-changes-2026/4545015), and [Manitoba](https://techcommunity.microsoft.com/blog/dstblog/interim-guidance-for-manitoba-permanent-dst-2026/4562488) describes the new Windows time zones and temporary workarounds. 

**SQL Server on Windows requires the applicable Windows update—not a separate SQL Server product update.** For SQL Server on Linux, Azure SQL Database, and Azure SQL Managed Instance, the following guidance applies when the new regional time zones are not yet available in your deployment. 

**Interim guidance when the new time zone is unavailable** 

This table adapts the Windows interim guidance for SQL. Use the interim identifiers for explicit SQL conversions, SQL Database or eligible SQL Managed Instance database/session settings, mapped Linux configuration, or **new SQL Managed Instances**. The instance-level time zone setting cannot be modified for an existing SQL Managed Instance. 

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Affected area** | **Existing SQL time zone** | **Interim SQL time zone** | **Required offset from November 1** | **Final regional time zone** |
| Most of British Columbia | Pacific Standard Time | Yukon Standard Time | UTC−07:00 | British Columbia Standard Time |
| Alberta and locations covered by its guidance\* | Mountain Standard Time | Canada Central Standard Time | UTC−06:00 | Alberta Standard Time |
| Manitoba | Central Standard Time | Eastern Standard Time (Mexico) | UTC−05:00 | Manitoba Standard Time |

*\*The Alberta guidance also covers southeastern BC locations aligning with Alberta and affected Northwest Territories locations, including Yellowknife and Inuvik. Do not apply the first row to all of BC.* 

For Manitoba, the Windows workaround uses ordinary Eastern Standard Time **with automatic DST adjustments disabled**. SQL’s AT TIME ZONE does not provide the DST adjustment switch. Instead, Eastern Standard Time (Mexico) supplies UTC−05:00 without seasonal changes under its current rules. Ordinary Eastern Standard Time returns to UTC−04:00 in summer. 

Confirm that the selected identifier is available in sys.time\_zone\_info on the target deployment. These substitutes match the required current and future offsets, **not the provinces’ complete historical rules**. Do not blanket-replace historical conversions. Move to the regional definition when supported, using the appropriate product-specific method. 

**SQL Server on Windows** 

SQL Server reads installed Windows time zones from the OS registry, as documented for [sys.time\_zone\_info](https://learn.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-time-zone-info-transact-sql). 

Install the applicable Windows update. When the server’s local time must follow the affected region, select the new regional zone under **Settings > Time & language > Date & time**, following the provincial guidance linked above. 

Also update explicit AT TIME ZONE references where appropriate. Installing the update does not rewrite application SQL or make the existing shared US-and-Canada identifier equivalent to the new province-specific definition. 

**SQL Server on Linux** 

Follow [Configure the time zone for SQL Server on Linux](https://learn.microsoft.com/en-us/sql/linux/configure/time-zone?view=sql-server-ver17) for SQL Server 2022 or later. SQL Server on Linux map the Linux/IANA time zone to a Windows identifier used internally by T-SQL. 

The documented mappings for the interim choices are: 

|  |  |  |
| --- | --- | --- |
| **Affected region** | **Linux/IANA identifier** | **SQL time zone identifier** |
| Most of BC | America/Whitehorse | Yukon Standard Time |
| Alberta and aligned locations | America/Regina | Canada Central Standard Time |
| Manitoba | America/Cancun | Eastern Standard Time (Mexico) |

Configure the matching IANA zone in the SQL Server service or container’s TZ environment, or through the applicable host configuration. Ensure the setting reaches the **SQL Server process**, not only an interactive shell; restart or redeploy that process as appropriate. TZ takes precedence over /etc/localtime and the other documented configuration sources. 

Do not assume that updating Linux tzdata alone updates SQL Server’s Windows-zone definitions or mapping. For older releases, use the corresponding [SQL Server 2019](https://learn.microsoft.com/en-us/sql/linux/configure/time-zone-2019?view=sql-server-ver17) or [SQL Server 2017](https://learn.microsoft.com/en-us/sql/linux/configure/time-zone-2017?view=sql-server-ver17) documentation. 

**Azure SQL Database** 

As described in [my earlier announcement of local time zone support](https://devblogs.microsoft.com/azure-sql/announcing-the-public-preview-of-local-time-zone-support-in-azure-sql-database/), the public-preview feature allows configuration at the **database or session level**. 

For example, use the following options for Manitoba: 

```
-- Persistent database default

ALTER DATABASE SCOPED CONFIGURATION

SET TIME_ZONE = 'Eastern Standard Time (Mexico)';

-- Alternatively, override just the current connection

SET TIME ZONE 'Eastern Standard Time (Mexico)';  
```

A session override takes precedence over the database setting. SET TIME ZONE LOCAL removes the session override. 

Inside a stored procedure or dynamic SQL batch, the change is scoped to that execution. A normal GO batch separator does **not** reset a session setting. See the [SET TIME ZONE documentation](https://learn.microsoft.com/en-us/sql/t-sql/statements/set-time-zone-transact-sql?view=azuresqldb-current) for scope and usage details. 

The setting affects current-time functions such as GETDATE(), SYSDATETIME(), and SYSDATETIMEOFFSET(). It does **not** convert stored values, change explicit AT TIME ZONE expressions, or change UTC timestamps in system views. 

Once the regional identifier becomes available, replace the interim setting at the scope your application uses. SET TIME ZONE is not supported on SQL Server. 

**Azure SQL Managed Instance** 

The [instance time zone can only be selected during creation](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/timezones-overview?view=azuresql). To change the instance-level time zone itself, create a replacement instance with the required temporary or final time zone and migrate the workload. 

On SQL Managed Instances using the [Always-up-to-date update policy](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/update-policy?view=azuresql) where local time zone support is available, use ALTER DATABASE SCOPED CONFIGURATION SET TIME\_ZONE or SET TIME ZONE to apply the same interim time zones at database or session scope. These settings change the effective time zone for supported current-time functions without migrating the instance. They do not change the instance-level time zone or SQL Agent schedules; an instance-wide time zone change still requires the migration approach below. 

 

|  |  |  |
| --- | --- | --- |
| **Migration option** | **How it works** | **Trade-off and requirements** |
| [Failover group](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/failover-group-sql-mi?view=azuresql#overview) | Replicate continuously, then perform a controlled planned failover after synchronization. | More setup; generally lower cutover downtime. Instances must be in different regions and share a DNS zone. |
| [Cross-instance point-in-time restore](https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/point-in-time-restore?view=azuresql&tabs=azure-portal#restore-to-the-same-subscription) | Restore databases to a replacement instance in the same region, then cut applications over. | Simpler; generally longer downtime. Coordinate source writes and the final restore point to avoid omitting later transactions. Restore-point timestamps are interpreted as UTC. |

Recreate instance-level dependencies, including logins, objects in master, SQL Agent jobs, credentials, linked servers, certificates, and server-level configuration. Validate applications and job schedules before retiring the old instance. 

**Plan for two migrations when using an interim time zone** 

If the final regional zone is unavailable, first migrate to an instance configured with the interim zone. After the regional zone becomes available, migrate again to another instance created with that final zone. 

For a failover-group approach that returns to the original region: 

**Original MI — Region 1 → Temporary-zone MI — Region 2 → Final-zone MI — Region 1** 

The service update **does not change the selected time zone of the existing temporary instance**. Budget for both migrations and their cutovers. 

Normally, failover-group partners should use matching time zones. A deliberate mismatch for this migration requires careful validation; it is not the recommended steady-state high-availability configuration. 

If only a query or display requires adjustment, an explicit conversion can avoid changing instance-local time: 

```
SELECT SYSUTCDATETIME() AT TIME ZONE 'UTC'

    AT TIME ZONE 'Eastern Standard Time (Mexico)' AS ManitobaLocalTime;  
```

This changes the query result—not SQL Agent schedules or the instance’s GETDATE() behavior.
