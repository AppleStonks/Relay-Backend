## DB Design
Under docs/ there is an ERM diagram to show the DB schema

## OpenAPI spec
In the openapi/ folder are the API specs which are used to generate the folder `generated-apis-models`
This folder contains the code for the server APIs and the models for what these APIs recieve and send

## Main App
This is under the app/ folder
The DB file contains the code to setup the SQLAlchemy ORM + SQLlite DB
SQLAlchemy is an ORM which allows us to use objects to represent the tables in the DB
SQLlite is our file DB - connectionless

