## DB Design
Under docs/ there is an ERM diagram to show the DB schema

## OpenAPI spec


## Main App
This is under the app/ folder
The DB file contains the code to setup the SQLAlchemy ORM + SQLlite DB
SQLAlchemy is an ORM which allows us to use objects to represent the tables in the DB
SQLlite is our file DB - connectionless

## Seed db
If you want to seed the db, change the seed.py file in app/db
Try delete the relay.db file and from root of project run python app.db.seed