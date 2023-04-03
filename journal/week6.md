# Week 6 — Deploying Containers

## Livestream Notes

- No free tier for fargate
- Service Connect - AppMesh and Service Map together
- You have to choose a network mode in ecs ec2 (e.g. Bridge, Default, Host, AwsVpc)
- Nats expensive $32 + cost per GB bandwidth
- ec2 ec2 resides in private subnet, so when it tries to access internet to reach cognito it can't
- eni gives your hardware an IP address

## In work notes

- Sometimes health checks do a critical database check to see if everything is working
- DO not package network debugging, utility tools into containers in the event that someone gets access to your contaienrs
 which is why we are using python scripts
- Service vs Tasks in ECS services run for ever, tasks execute and then exit
- Always protect your APIs from the outside world!


## Debugging

- Getting an error that ecs is not able to pull images from ecr
    - I have tried adding permissions
    - changed the image name in the task definition
fixed: I added the permissions to the exection role and it worked (b4 I was adding to the task role)

- I used the Load Balancer ARN instead of the target group ARN which was giving me a permisisons error

- I am using a load balancer currrently so I had to configure it so that if the host header is from my IONOS domain routes to port 444 which is cruddur

- I built my front end docker conatiner with the cruddur.com as my BACKEND URL.  This was causing an error because front end was requestiong to https://cruddur.com/api/activities and not my domain.  

- Was having a cors error, likely because im running cruddur on port 444 so I had to add that port to the front end origin.  

- I scratched using my load balancer for two different apps as it was getting too complex.  I set it up again and ran into an error because I set fronted url to "http" and it had to be "https"


## Security Notes

- 75% high or critical vulnerabilities
- 50% no limits defined
- 76% are running as root (which is bad)

**Problems with AWS Fargate**
- No visibility or infrastructure
- Ephermeral Resources makes it hard to do a traige or Forensics for detected threats
- No file/network monitoring
- Cannot runt raditional security agents in fargate
- User can ru nunverified container images
- Containers can run as root with elevated priviledges

**Amazon ECR Images Security**
- Enable scan on push to allow ecr. 
- AWS inspector uses snyk in the background

**Amazon ECS Security Best Practices**
- CLoud Control Plane - Access control (who controls container images)
- Choosing public or private ECR for images
- Use VPC Endpoints or Secuirty Groups with known sources only
- Do not put secrets passwords in containers - Use paramter store or Secrets manager
- Only use Trusted Containers from ECR with no HIGH/CRITICAL V
- Limit ability to ssh into EC2 container
- Make sure to have xray daemon installed on ec2 isntance
- Use only authorized container images