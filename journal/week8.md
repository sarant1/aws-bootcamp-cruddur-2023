# Week 8 — Serverless Image Processing

AWS CDK (Cloud Development Kit) IaaC

kinda like CloudFormation!
but it allows you to use any language to provision infrastrucutre!

- Constructs - L1, L0 where your taking the basic cloudformation template and interacting with it directly
    - There are different levels of constructs!
    - Basically like building blocks of code that you can pull in to basically provision some infrastructure.
    - L1 More primitive and customizable
    - L3 Less customizable and more general

## Debugging

- I am getting this error on my /bin/serverless/upload saying that aws command not found, but I do have aws cli installed and it works when I type it manually.
    SOLUTION: I was using PATH as a variable in my bash script which was overwritting the PATH of my aws binaries (duh...)
- I had two spelling errors I had to change FolderInput => folderInput and BCUKET_NAME => BUCKET_NAME


- I am getting an error props.activities.map is not a function in ActivityFeed
    SOLUTION: FOLLOW THE VIDEO, In Implement Users Profile page I followed along a fixed the same erros andrew did.

- I am getting some issues with my devcontainers local environment not port forwarding, they are forwarding to port localhost:3001 and localhost:4568 instead of the ones they are supposed to. 
    TMPSOLUTION: change docker compose ports to match new mapped ports

- I was getting an error because I did schema load public.schema information into my postgres db. 
    SOLUTION: ./bin/db/schema_load