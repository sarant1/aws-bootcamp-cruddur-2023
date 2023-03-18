# Week 4 — Postgres and RDS


## Debugging
It seems that crud features is working but it is not inserting data into database.  After some time I realized I forgot a () on conn.commit and then after that I finally got an error that helped me reach a solution.  For some reason the handle being passed from the front end was not in the seed data so when SQL was using that handle to find a uuid, it couldnt find it becuase the handle did not exist and since UUID is set to NOT NULL.  It threw an error.  Learned a lot here about how everything works!

I had a bug that I spent a long time trying to fix and I was getting a key error from the front end.  After many hours I realized I was querying an array for the object query which was why when I posted the CRUD, it would not display on the activity feed and the front end could not read the data correctly.

## Security Notes

- Security best practices are very important as sensitive data could be stored like credit cards, health info, etc.
- Most DBs are Relational SQL or Un-Relational No-SQL
- Strong relationship between each column and each row in Relational
- In NoSQL data is not really shaped in any way
- All usernames and passwords are stored on a database somewhere
- Make sure data is stored in the correct region
- Deletion Protection - have it on!
- Enable Multi-Az
- When setting up Inbound rules, you would want the inbound IP to the database to be the IP Address range for the organization or the VPN of the organization.
- Generally you would not want the database to be publicly accessable.  You would want it to be accessable by resources within your VPC so privatly.
- Use CloudTrail to monitor and trigger alerts on your DB
- Have Amazon GuardDuty in the account and the region.
- Have encryption in Transist as well as in rest
- Authentication use IAM, or kerberos etc (not the default)

## Local Environment

Currently attempting to set up the local environment but it via Devcontainers but Having issues installing devcontainer.  It says the devcontainer is already symlinked but it is still not working.  



