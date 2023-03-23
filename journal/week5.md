# Week 5 — DynamoDB and Serverless Caching


### Live Stream
- DyanomoDb for live messaging!
- No joins in DyanmoDB?
- Partition Key for Message Group to see all messages not the individual message
- Partition keys can be completely unrelated, so its common to use a generic title for a single table design
- If your not sorting or using the certain data for a purpose, you can just store it all extra data in a json document
- We are going to need two different Message Groups one for each person messaging eachother
- My user uuid is from cognito(session) or Postgres.


### Debugging struggles !
- It seems I lost my journaling to this point due to it not being commited :/
- Spent a few hours debugging a @ in my request, If I just would of watched the next minute of the video I wouldn't of wasted this time
- 
