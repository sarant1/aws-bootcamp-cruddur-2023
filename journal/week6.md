# Week 6 — Deploying Containers

## Livestream Notes

- No free tier for fargate
- Service Connect - AppMesh and Service Map together
- You have to choose a network mode in ecs ec2 (e.g. Bridge, Default, Host, AwsVpc)
- Nats expensive $32 + cost per GB bandwidth
- ec2 ec2 resides in private subnet, so when it tries to access internet to reach cognito it can't
- eni gives your hardware an IP address