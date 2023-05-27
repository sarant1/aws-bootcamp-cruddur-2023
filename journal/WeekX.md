# Week X — Final Week !


## Debugging

Issue: After adding inbound rules to RDS to accept Post Confirmation, it still was timing out.
- Solution: Add outbound rules to lambda function

Issue: For some reason my replies are not pushing under my activites ( they are being pushed as a activity themeself )
- Solution: I noticed the following error:

![Alt text](./assets/image.png)


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