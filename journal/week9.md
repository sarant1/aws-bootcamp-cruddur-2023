# Week 9 — CI/CD with CodePipeline, CodeBuild and CodeDeploy

## Debugging
- After following andrews videos, I had to add a policy to my CodeBuild Role to give it access to read and write from ECR to pull the python image.

FINISH week 8 & 9 (hopefully)


## Security Notes

- Continious Integrations / Continous Deployment/Continous Delivery
- Source Code Repo - All the code that is needed to build the application
- CodeCommit, CodeBuild, CodePipeline, CodeDeploy

Why CI/CD Pipeline ?

Security

- Checks for secrets
- Look for security risks in new bug
- OWASP Open Web Application Security Project

**Security Best Practices**
- Be aware of compliance standards, make sure services are available in that region
- Amazon Organizations SCP- restrict access to changes in a CI/CD pipeline, you would not want the wrong person to access prod CI/CD
- CloudTrail - Watch for malicious activities
- GuardDuty is enabled for monitoring suspicious DNS comms (crypto mining, etc)
- Use AWS config rules 

- Access Control for IAM roles.
- Security of endpoints of the CI/CD pipeline ( are there any public endpoints that are vulnerable ? )