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

*To create a Linux EC2 instance for free on AWS within the Free Tier, use the following step-by-step process, selecting Amazon Linux 2023 (kernel 6.1) AMI and a free tier eligible instance type such as t2.micro or t3.micro*.



AWS Free Tier and Instance Types

AWS Free Tier provides 750 instance hours per month of t2.micro or t3.micro for the first 12 months after sign-up for new customers. Now this has been changed into $100 credit system and reduced free benefits to 6 months only.



Both t2.micro and t3.micro instances offer 2 vCPUs and 1 GB RAM, suitable for basic workloads. t3.micro may be available in regions where t2.micro is not.



**Step-by-step Setup Instructions**

1\. **Sign Up and Access the EC2 Console**

Register for a free AWS account if not already signed up.

Navigate to the AWS console and open the EC2 dashboard.



2\. **Launch a New Instance**

Click the “Launch instance” or “Launch Instances” button.



3\. **Select Amazon Machine Image (AMI)**

In the AMI selection, use the search to find Amazon Linux 2023 (kernel 6.1).

Ensure the image is from the official AWS owner and not a third-party.



4\. **Choose an Instance Type**

Select t2.micro or t3.micro, ensuring the Free Tier Eligible label is present.

Both types have 2 vCPUs and 1 GB RAM, appropriate for the free quota.



5\. **Configure Key Pair for SSH Access**

Create a new key pair if needed and download the .pem file securely; this is required for SSH access.

***You will not be able to download this key again***.



6\. **Network and Storage Settings**

Keep the default VPC/network or configure as required.



**Allow SSH (TCP, port 22) in the security group for Linux access**. If we use **allow-all,** means we do not restrict any inbound or outbound traffic coming into the Linux box and going outside the Linux box.



**Storage**: the free tier allows up to 30 GB EBS; default (8 GB) is recommended unless extra space is needed.



7\. **Review and Launch**

Confirm all settings are “Free Tier eligible” to avoid inadvertent charges.



Click “**Launch Instance**” and wait for initialization.



8\. **Connect to the Instance**

Use the key pair and public IP/hostname for SSH access, e.g.:



text

chmod 400 my-key.pem

**ssh -i my-key.pem ec2-user@<public-ip>**

The “Connect” option in the AWS console provides command details.



**Notes**

t2.micro is typically available for most new accounts, but in some regions or accounts, only t3.micro may be shown for Free Tier. Monitor the AWS Free Tier usage from the billing dashboard to avoid unexpected costs.

This procedure ensures you use AWS Free Tier resources with an official Amazon Linux 2023 AMI on an eligible instance.



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



A key pair in AWS EC2 is a set of security credentials—one public key (stored with AWS and copied onto your instance) and one private key (downloaded and stored securely by you)—that is used for authenticating SSH access to your EC2 Linux instances.



Basic Concept: EC2 Key Pairs

Public Key: Saved in AWS and placed inside your EC2 instance during launch, typically in /home/ec2-user/.ssh/authorized\_keys for Amazon Linux.



Private Key: Downloaded by you as a .pem file; must be securely stored and never shared.



Together, they enable asymmetric cryptography: only someone with the private key can open the SSH connection, and AWS never keeps a copy of your private key.



A **key pair** in AWS EC2 is a set of security credentials—one public key (stored with AWS and copied onto your instance) and one private key (downloaded and stored securely by you)—that is used for authenticating SSH access to your EC2 Linux instances.



**Basic Concept: EC2 Key Pairs**

Public Key: Saved in AWS and placed inside your EC2 instance during launch, typically in /home/ec2-user/.ssh/authorized\_keys for Amazon Linux.

(Public Key means like a LOCK we put for a home/suitcase; Private Key is like the key we hold and carry along with us in our pockets/bags along with us while we lock our home/suitcase and go away)



Private Key: Downloaded by you as a .pem file; must be securely stored and never shared.



Together, they enable asymmetric cryptography: only someone with the private key can open the SSH connection, and AWS never keeps a copy of your private key.

