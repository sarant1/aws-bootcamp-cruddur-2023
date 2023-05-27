# Week X — Final Week !


## Debugging

Issue: After adding inbound rules to RDS to accept Post Confirmation, it still was timing out.
- Solution: Add outbound rules to lambda function

Issue: After finishing the cicd pipeline I noticed that the frontend was not passing the token to the backend.
- Solution: Using the sync tool, I had to simply build and sync my website.  

Issue: My create activities were posting to the db but I was getting a 422 error.
- Solution: For some reason I had my model['errors'] defaulting to {} and not None so it was returning the error.  I switched the default values of model and it fixed !

### Learning Git

I was trying to use git cli and struggling so I decided to look up some commands.  I was confused on the difference between git pull and fetch and git merge.

git pull <remote> = git fetch <remote> && git merge <remote>/<branch>

```bash
git pull origin master
```
or

```bash
git fetch origin
git merge origin/master
```