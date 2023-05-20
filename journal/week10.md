# Week 10 — CloudFormation Part 1

## Livestream Notes
- 3 tier architecture (ex: Web tier, app tier, database tier)
- Cloudformation use smaller sections to save time when having to re provision them if they fail.


My Lucid Chart for networking:
https://lucid.app/lucidchart/a753709e-2d6f-4313-9d42-1ea87fde69fd/edit?view_items=gZWRLAi3EmBS&invitationId=inv_96c0aa6b-8f93-4f98-840e-5d4fe4755209

## Debugging

Getting these erros with cloudformation


![Errors](./assets/CFNClusterErrors.jpg)


I fixed it but I forget what the problem was :/

I misconfigured my ALB listeners so I had to fix some spelling mistakes Forward => forward & HTTPS => HTTP (for HTTP listener)


**Im getting this error** 


![Found Stinrg](https://cdn.discordapp.com/attachments/1040368636763836429/1104569721405329488/image.png)


**According to the error message, Cloudformation is interpretting inputs as strings rather than Numbers or booleans.**
- I found out that the error was because I was not importing my SecurityGroupId correctly.  Not the best error handling on the cloudformation, but nothing stackoverflow can't solve!

**Im getting error saying the backendTG has not been created yet and the solution was to export the backendTG and import into the service template.**
- I also had to change the target type to ip so that it would work with fargate

**I am setting up the front end and since I do not use route53 I have to find a solution for when I deploy the frontend cfn or just transfer my domain to route53**

- I am transfering my domain to route53, I am having trouble deleting my current acm certificate because it is in use.
SOLUTION: I found that my certificate was being usued for a custom domain in API gateway, I wish AWS showed where it was located rather than that the cert was in use with some random account for a elastic load balancer!




