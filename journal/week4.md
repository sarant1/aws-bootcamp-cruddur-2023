# Week 4 — Postgres and RDS


## Debugging
It seems that crud features is working but it is not inserting data into database.  After some time I realized I forgot a () on conn.commit and then after that I finally got an error that helped me reach a solution.  For some reason the handle being passed from the front end was not in the seed data so when SQL was using that handle to find a uuid, it couldnt find it becuase the handle did not exist and since UUID is set to NOT NULL.  It threw an error.  Learned a lot here about how everything works!