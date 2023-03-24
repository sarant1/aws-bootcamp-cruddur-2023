# Week 5 — DynamoDB and Serverless Caching


## **Live Stream**
- DyanomoDb for live messaging!
- No joins in DyanmoDB?
- Partition Key for Message Group to see all messages not the individual message
- Partition keys can be completely unrelated, so its common to use a generic title for a single table design
- If your not sorting or using the certain data for a purpose, you can just store it all extra data in a json document
- We are going to need two different Message Groups one for each person messaging eachother
- My user uuid is from cognito(session) or Postgres.


## **Debugging struggles !**
- It seems I lost my journaling to this point due to it not being commited :/
- Spent a few hours debugging a @ in my request, If I just would of watched the next minute of the video I wouldn't of wasted this time

## **Security Notes**

**GENERAL**
- Why Non-relational DBs?..  Millions per second, Consistant performance!
- Use cases:
    - Banking and Finance (Fraud Detection, user transactions)
    - Gaming (Leaderboards, Player data stores, Game states)
    - Software and internet (Meta data caches, Ride Tracking stores, Relationship, graph data stores)
    - Ad tech ( user profile stores, metadata stores, popular item cache)
    - Retail (shopping carts, workflow engines, customer profiles)
    - Media & Entertainment (User data stores, media metadata stores, digital rights management stores)
- Managed service, Amazon takes care of infrastructure and what it is standing on
- Methods for accessing DynamoDB
    - Old way to access was going from ec2 -> Router -> Internet Gateway -> Internet -> DynamoDB
    - Better way ec2 -> nat gateway -> DynamoDB
    - Best way ec2 -> router -> vpc endpoint -> DynamoDB
- DynamoDB Accelerator- Creates DAX clusters that has a cache between DynamoDB and EC2 (ec2-> cache -> dynamodb)

**SECURITY BEST PRACTICES**
- Make sure your in the correct region
- Deletion Protection should be on in production
- Encrpytion key should be considered for your use case
- Tagging is good
- DAX Operate within a VPC
- Two Sides: Amazon Side vs Client Side
- Use VPC Endpoint or Privatelink to prevent your VPC from having to go to the internet to access dynamodb
- Compliance - Choose correct region for data and make sure it is compliant for regional security standards
- Use Amazon Organization SCP to manage Table deletion, table creation, region lock, etc
- Use CloudTrail and make alarms to trigger malicious activity
- use AWS Config rules for account and region
- Client side encryption for DynamoDB ( AWS Recommended )
- Sensative data is better stored in RDS
- Avoid IAM Users/Group, use Iam Role or Cognito Identity Pool (if you are creaating users, limit the amount of them)
- Limit access to only what they need (e.g. access to certain tables)
- DAX Service Role should have Read Only Access to DynamoDB ( if possible )
- Site to Site VPN or Direct Connect


