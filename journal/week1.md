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
8:07