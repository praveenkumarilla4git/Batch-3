**Steps to create Linux box in AWS account free tier**:

After root email login into AWS console make sure you change region to US North Virginia.

we can take near by region to reduce latency but we need to take US North Virginia as this is the first region AWS has launched and brings new services to this region only at first so the cost will be less compared to other regions

region = **us-east-1**



**What is an AWS Region**?

An AWS Region is a distinct geographic area that contains multiple isolated locations known as Availability Zones (AZs). Each Region provides a separate and independent infrastructure deployment with its own power, cooling, and network connectivity. AWS currently operates multiple Regions worldwide, such as US East (N. Virginia), Europe (Frankfurt), Asia Pacific (Mumbai), etc.



**Key points**:

Represents a broad geographical area.

Comprises multiple Availability Zones.

Designed for geographic separation for compliance, fault tolerance, and data residency.

Customers select a Region where their cloud resources are hosted.

Regions are isolated from each other to reduce the risk of a large-scale failure.

Each AWS Region has at least **3** Availability Zones.



**What is an AWS Availability Zone (AZ)**?

An AWS Availability Zone is one or more discrete data centers within an AWS Region, each with independent power, network, and cooling, designed to be isolated from failures in other AZs within the same Region. Availability Zones are connected with **low-latency**, **high-bandwidth networking**, **allowing synchronous replication** for fault tolerance and **high availability**.



**Key points**:

Smaller physical locations within a Region.

Each AZ has independent infrastructure to avoid correlated failures.

Typically located kilometers apart within the same Region.

Supports fault isolation, either AZ failure or zone maintenance does not affect others.

Enables customers to design highly available, fault-tolerant applications by distributing.



**Steps to create a Linux EC2 instance for free and in free tier**:

EC2 --> Elastic Compute Cloud

Browse AMI

Select --> Amazon Linux 2023 kernel - 6.1 AMI

select t3.micro or t2.micro --> free tier eligible

t3.micro --> 2 CPU, 1 GB RAM 



**Authentication**

==============

what you know? --> Username and Password

what you have? --> Username, RSA/OTP/Google Authenticator/Microsoft Authenticator

what you are? --> finger prints, retina, palm, etc.



One-Factor Authentication --> 2-Factor Authentication --> Multi Factor Authentication

