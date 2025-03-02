---
title: Cost estimation to run frequently scheduled job
created: 2025-03-02
updated: 2025-03-02T15:57
---
# Purpose of this estimate
There are task in life that require automation and given home network can be unreliable. it is better to do it in the cloud.

There would always be task that can't be done within 15 minutes and logically doesn't make sense to be split into multiple lambda steps. Example include large scale selenium (complicated robot process automation), pyspark, dbt.

Hence it is important to estimate the cost of having a virtual private server (vps).


# takeaway
The max yearly cost for the 3 options below is 150 USD.

# raw estimate output

https://calculator.aws/#/estimate?id=84fc301c1dbea0a9545eaf0ddd41ca6faf0a5c5e


Estimate summary
| Upfront cost | Monthly cost       | Total 12 months cost    | Currency |
| :----------- | :----------------- | :---------------------- | :------- |
| 70.96        | 14.190000000000001 | 241.24                  | USD      |
|              |                    | * Includes upfront cost |          |


Detailed Estimate
| Group hierarchy | Region                | Description       | Service    | Upfront | Monthly   | First 12 months total | Currency | Status | Configuration summary       |
| :-------------- | :-------------------- | :---------------- | :--------- | :------ | :-------- | :-------------------- | :------- | :----- | :-------------------------- |
| My Estimate     | Asia Pacific (Sydney) | minimal on demand | Amazon EC2 | 0       | 3.869     | 46.43                 | USD      |        | "Tenancy (Shared Instances) |, Operating system (Linux), Workload (Consistent, Number of instances: 1), Advance EC2 instance (t4g.nano), Pricing strategy (On-Demand Utilization: 100 %Utilized/Month), Enable monitoring (disabled), DT Inbound: Not selected (0 TB per month), DT Outbound: Not selected (0 TB per month), DT Intra-Region: (0 TB per month)"
| My Estimate     | Asia Pacific (Sydney) | mininal upfront   | Amazon EC2 | 70.956  | 0         | 70.96                 | USD      |        | "Tenancy (Shared Instances) |, Operating system (Linux), Workload (Consistent, Number of instances: 1), Advance EC2 instance (t4g.nano), Pricing strategy ( 3yr  All Upfront), Enable monitoring (disabled), DT Inbound: Not selected (0 TB per month), DT Outbound: Not selected (0 TB per month), DT Intra-Region: (0 TB per month)"
| My Estimate     | Asia Pacific (Sydney) | 8g 2cpu 4h/d      | Amazon EC2 | 0       | 10.317333 | 123.81                | USD      |        | "Tenancy (Shared Instances) |, Operating system (Linux), Workload (Consistent, Number of instances: 1), Advance EC2 instance (t4g.large), Pricing strategy (On-Demand Utilization: 4 Hours/Day), Enable monitoring (disabled), DT Inbound: Not selected (0 TB per month), DT Outbound: Not selected (0 TB per month), DT Intra-Region: (0 TB per month)"



Acknowledgement
"* AWS Pricing Calculator provides only an estimate of your AWS fees and doesn't include any taxes that might apply. Your actual fees depend on a variety of factors, including your actual usage of AWS services."



The idea FOR THE LARGE instance is that one can run dbt jobs within it, because dbt env can exceed:
  lambda package limit 
  15 min runtime limit
  lambda instance memory limit
also the 

ECR has 50GB always free for containers, plenty for hobby use

ECS on EC2 is free.


