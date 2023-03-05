# Week 3 — Decentralized Authentication

### Summary:
I had to remake my cognito user pool so that I could add preferred_username required attribute.  Had to rewatch livestream so that I could set up the new cognito pool with preferred_username attribute.  Now I am making my 3rd cognito user pool because I also had use name and email checked on creation.  For some reason my JWT token is not being passed to my backend.  I had a spelling mistake, headers != hheaders.

### Exploring JWT Notes:

Why would we use lots of code from a third party source rather than the AWS SDK (Which is much shorter)?
In order to get user information using AWS SDK we would have to hit the cognito API to grab that information.  In our case, the information is client side so we do not have to reach out to cognito to grab that information.  We do not know exactly what is happening when the SDK gets a user information, in our case, we know exactly how it works and what is going on in the background.

- Try and use AWS libraries when you can because they are supported by AWS, however community libraries are ok if you can understand them and they are well written
- We could run the JWT library and auth in a sidecar but this would require us to split the resources even more because we are using ec2 ecs.
- We could use API gateway authorizers that sit in front of our flask APIs.  This might be easier but cost might come in to question.  If we are getting millions and millions of requests, 