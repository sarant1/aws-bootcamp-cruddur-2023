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