---
source: "https://aws.amazon.com/blogs/aws/aws-glue-6-0-now-available-with-30-lower-price-and-full-apache-iceberg-v3-support"
title: "AWS Glue 6.0 now available with 30% lower price and full Apache Iceberg v3 support (3 minute read)"
author: "unknown"
date_published: "2026-08-24"
date_clipped: "2026-08-26"
category: "DevOps & CI/CD"
source_type: "rss"
discovered_via: "https://tldr.tech/devops/2026-08-24"
source_role: "primary-via-tldr"
---

# AWS Glue 6.0 now available with 30% lower price and full Apache Iceberg v3 support (3 minute read)

Source: https://aws.amazon.com/blogs/aws/aws-glue-6-0-now-available-with-30-lower-price-and-full-apache-iceberg-v3-support

AWS Glue 6.0 now available with 30% lower price and full Apache Iceberg v3 support
by Channy Yun (윤석찬) on 21 AUG 2026 in Analytics , AWS Glue , Launch , News Permalink Comments Share
Today, we are announcing the general availability of AWS Glue 6.0 , delivering 30% lower pricing than previous AWS Glue versions and introducing full support for Apache Iceberg v3 features. AWS Glue 6.0 is built on a fully modernized runtime, Apache Spark 4.1, Python 3.13, and Scala 2.13, delivering faster performance.
With this release, AWS Glue provides the most complete Iceberg v3 implementation on any fully serverless managed Spark service, along with new capabilities that simplify ETL authoring, improve PySpark performance, and enable real-time streaming with single-digit millisecond latency.
What is new in AWS Glue 6.0
AWS Glue 6.0 delivers the complete Apache Iceberg v3 specification, built on Iceberg 1.11.0. The headline feature is the VARIANT data type with shredding support, which achieves faster query read performance compared to traditional string data type columns for semi-structured data.
With VARIANT shredding, you can store and query JSON, logs, and event data without flattening schemas, eliminating duplicate data copies, custom parsing code, and pipeline breakage when schemas change. This capability transforms how teams handle semi-structured data at scale.
Additional Iceberg v3 capabilities include:
Geometry and Geography data types : Enable native spatial processing for GIS analytics, location intelligence, and geospatial data pipelines directly on managed Spark.
Nanosecond-precision timestamps : Support IoT sensor data, scientific computing, and high-frequency financial workloads that require precision beyond standard milliseconds.
Unknown type handling : Process data with unexpected or evolving schemas without pipeline failures, providing resilience against upstream schema changes.
AWS Glue 6.0 also includes most significant upgrade in Spark 4.1, the modern runtime engine:
Spark declarative pipelines : Spark Declarative Pipelines introduces a simplified approach to ETL authoring. Data engineers declare transformations, specifying what data should look like, while the engine automatically determines execution order and optimization. This reduces the complexity of pipeline development and eliminates manual orchestration overhead.
Arrow-native Python UDFs and UDTFs : AWS Glue 6.0 introduces Arrow-native execution for Python User-Defined Functions (UDFs) and User-Defined Table Functions (UDTFs). This eliminates serialization overhead between Python and the JVM, improving PySpark performance for complex transformations.
Real-time streaming mode : For stateless streaming use cases, AWS Glue 6.0 introduces a real-time streaming mode that achieves single-digit millisecond latency. Built on Spark 4.1’s Real-Time Mode with Glue-optimized execution, this capability supports real-time event processing, low-latency data transformation pipelines, and time-sensitive data routing.
Getting started with AWS Glue 6.0
No API changes are required to use AWS Glue 6.0. You can select the new version using the existing --glue-version parameter in the create-job or update-job APIs through  AWS Command Line Interface (AWS CLI) ,  AWS SDK , AWS Glue Studio , Amazon SageMaker Unified Studio , and your preferred IDE.
To get started with AWS Glue 6.0 jobs in the AWS Glue Studio console , open the AWS Glue job and on the Job Details tab, choose the version Glue 6.0 – Supports Spark 4.1, Scala 2, Python 3 . You can create new AWS Glue jobs on AWS Glue 6.0 to get the benefit from the improvements, or migrate your existing AWS Glue jobs.
To start using AWS Glue 6.0 on an AWS Glue Studio notebook or an interactive session through a Jupyter notebook, set 6.0 in the %glue_version magic. You can also upgrade existing jobs to Glue 6.0 using the Spark upgrade agent on AWS Glue Studio or use the auto-upgrade feature in their existing Glue jobs to automatically upgrade them to Glue 6.0.
To learn more, visit the AWS Glue 6.0 version detail and Migrating AWS Glue for Spark jobs to AWS Glue version 6.0 in the AWS documentation.
Now available
AWS Glue 6.0 is generally available today in all AWS Regions where AWS Glue operates. For Regional availability and a future roadmap, visit the AWS Capabilities by Region . If you want to call APIs, search documentation, find regional availability, and check troubleshooting about this new feature, try using the AWS MCP Server and plugins with your preferred AI tool.
You pay an hourly rate, billed by the second, for crawlers (discovering data) and extract, transform, and load (ETL) jobs (processing and loading data). For the AWS Glue Data Catalog, you pay a simplified monthly fee for storing and accessing the metadata. The first million objects stored are free, and the first million accesses are free. To learn more, visit AWS Glue Pricing page .
Give it a try in the AWS Glue Studio console , and send feedback to AWS re:Post for AWS Glue or through your usual AWS support contacts.
— Channy
Channy Yun (윤석찬)
Channy is a Lead Blogger of AWS News Blog and Principal Developer Advocate for AWS Cloud. As an open web enthusiast and blogger at heart, he loves community-driven learning and sharing of technology.
Loading comments…
