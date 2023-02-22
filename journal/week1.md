# Week 1 — App Containerization

## **Stream Notes**

### **Why should we containerize?**
- Makes your app more portable?
- Allows you not to destroy your environment
- Allows all apps to have the **same environment** regardless of their operating system
### linuxserver.io has a lot of sample environments (Good for reference)
### Dockerhub Github for docker images, there are many different types of docker 

### **Docker Commands:**
- WORKDIR Entrypoint for the container for ()
- COPY {FromMyOS} {toContainer} e.g.(COPY . .)

### Extra all linux distros use the same linux kernal

## **Spend Notes**
- #### Im using my local machine as my environment as I feel more comfortable
- #### Cloud9 uses t2.micro to run, so its free as long as your under free tier limit for ec2


## **Security Notes** ## 

### Container Security
- Protecting applications hosted on computer services like containers

### Why care about container security?
- Containers are widely used because of its convenience
- If breached by hacker, its possible that only 1 part of your app is affected
- Containers allow you to launch machines quickly

### Why security requires practice ?
- Complexity with containers
- When using different versions like ECS, there is different levels of management

### Docker components
- Docker Client
- Docker Server
    - Registry
    - Docker Daemon

### Best Practices
- Keep host and docker updated
- Docker should run in non-root user mode ((preventscontainer escape method)
- Only have required files in the container 
- The smaller the size of container the better
- Private container registry is safer
- Limit long term storage for docker containers
- Ensure all code is tested for vulnerablities
- More...

### Snyk OpenSource Security
- Service to help with security and container security
- You can test code directly on github


### AWS Secret Manager
- Store secrets not all AWS services have access to secrets manager
- You could also use **Hashicorp Vault** as a alternative
- 40cents per month per secret and 0.05 per API call
- Key/Value with encryption key
- Automatic rotation is good

### AWS Inpsector / Clair
- Integrated with ECS/ECR
- Find by vulnerablitiy, Instance, AMI, and a lot more..

#### Generally managed services are better and easier
#### Automation to provision conatiners at scale with speed

## **Configuration** 
### - I set up gitpod with aws cli so that I could follow instructions easier
### - Created a table and an item to ensure dynamodb is working
### - I had to set up security keys after noticing I accidentely commited them in my repo



