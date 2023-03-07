# Week 3 — Decentralized Authentication

### Summary:
I had to remake my cognito user pool so that I could add preferred_username required attribute.  Had to rewatch livestream so that I could set up the new cognito pool with preferred_username attribute.  Now I am making my 3rd cognito user pool because I also had use name and email checked on creation.  For some reason my JWT token is not being passed to my backend.  I had a spelling mistake, headers != hheaders.

### Exploring JWT Notes:

Why would we use lots of code from a third party source rather than the AWS SDK (Which is much shorter)?
- In order to get user information using AWS SDK we would have to hit the cognito API to grab that information.  In our case, the information is client side so we do not have to reach out to cognito to grab that information.  We do not know exactly what is happening when the SDK gets a user information, in our case, we know exactly how it works and what is going on in the background.

- Try and use AWS libraries when you can because they are supported by AWS, however community libraries are ok if you can understand them and they are well written
- We could run the JWT library and auth in a sidecar but this would require us to split the resources even more because we are using ec2 ecs.
- We could use API gateway authorizers that sit in front of our flask APIs.  This might be easier but cost might come in to question.  If we are getting millions and millions of requests.
- Our current solution is the most tightly coupled 
- Sidecar method is less coupled
- Lambda with api gateway is the least coupled 
- Always check all routes to see which solution will be the best solutionS

## Security Notes
**What is SAML(Security Assertion Markup Language) or Single Sign on?**
- Allows you have a single point of entry into any app that you use.  One Credential, Multiple Apps.  Example FaceID for multiple apps on iphone

**What is OPEN ID connect?**
- Using Facebook, Amazon, Apple, Etc to login to apps

**What is OAuth 2.0?**
- You can authorize Linkedin to post on Twitter.  Linkedin needs Authorization to push to Twitter feed.

**What is decentralized Authentication?**
- Allows you to store your Username and Password in one location.  If your smart, use different passwords.  Risk tolerance is important when determining what password and where it is stored.

**What is Amazon Cognito?**
- Provides authentication and store for usernames and passwords. 
- User pool is for authorization for app information
- Identity Pool is for access to AWS resources.

**Why you use Cognito?**
- Good for extending to other AWS resources
- Scalable
- Your customers customers data would be stored in amazon rather than your on prem db

**User LifeCycle Management**
- You join a company, someone makes you a account for the job.
- Changing user roles
- Offboarding users when they leave.  

**Token Lifecycle Management**
- Token that is usually short lived
- Gives temporary credentials

**Amazon Cognito - Security Best Practices - AWS**
- Limit what services have access to your user pool.
- AWS WAF limit requests per time to prevent attacks
- Make sure cognito is compliant with local standards
- Use Cloudtrail to log suspicious changes in cognito
- Encryption in Transit for API Calls



