# Week 0 — Billing and Architecture

Spend Notes { - Pricing varies between regions

    Billing Resource(FREE):
        Bills:
            - You can check month by month resources used and cost
        Free Tier:
            - Allows you to monitor your Free tier usage
        Billing preferences:
            - Allows you to set an email address to send billing alerts to

    CloudWatch Alarm (FREE Tier up to 10):
        - Region has to be set to N. Virginia
        - Allows you to set a more customized alarm, You use SNS to send alert (10 alarms free in Free Tier)
    Cost Allocation Tags (important in real world)(FREE):
        - You can set tags to resources and then track the total cost of all the resoures that utilize that tag
    Cost Explorer (FREE):
        - Allows you to  view data on spend via graphs and filters
    AWS Calculator (FREE):
        - Calculates amount for 730 hours, The actual cost will depend on month and total amount of hours

}

Security Notes {
Cyber security goal: - Inform a business on any tech risk that a business may be exposed to - Make sure the business is INFORMED on the RISK
What is cloud security ? - Protecting data within a app hosted on the Cloud
Why should we care? - AWS account gets compromised => could have huge impact if not properly set up
Automation => good! - helps prevent human error
HACKERS! - starting to get into cloud and using AI for hacking

    AWS Organizations (FREE):
        - account segregation is the highest level of segration example, this allows the seperations of environments
        - Helps you manage billing, security, and managing.
        - Leave management account seperate from any resources

    AWS CloudTrail ($$):
        - MOST things will be reported to Cloud Trail
        - monitoring data (ensuring it is in the right place)
        - You can store trail data in S3 ($$)
        - Data Events Config($$)
        - Insight Events Config($$)
    IAM (FREE):
        - Enable MFA for all Human Users
        - 3 Kinds of users:
            - AWS IAM User
            - System Users, can be attached to a system
            - Federated Users, SAML
        - IAM Roles vs IAM Policy:
            - IAM Policy can be attached to a group of users, individual, admin role
            - Essentially a policy is attached to a role, resource,etc to give it permissions

    AWS Organizations and SCP(Service Control Policy):
        - Use SCP to give permmissions to users within an organization (TIP: Use least privilege model)
            - Examples: prevent users from leaving an organization
        - You Attach SCP to organizational accounts
    AWS GuardDuty ($$):
        - Threat detection service for AWS

    TOP 5 Cloud Security Practices!:
        1. Data Protection & Residency in accordance to Security Policy
            - The data should be stored in the country that it makes sense to be stored in
        2. IAM with Least Privilege
            - Give users just enough permissions to do their job
        3. Governance & Compliance of AWS Services being used
            - Understand local laws and regulation with data (Global vs Regional)
        4. Shared Responsiblity of Threat Detection
            - AWS can show what can be done, your job is to implement and do what can be done
        5. Incident Response Plans to include Cloud
            - Continue to update incident response

}
