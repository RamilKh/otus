# Task 6. Start application in docker using docker-compose

#### Build
Run `docker-compose build`

#### Start application in local mode
1. Prepare the database from `/dump/init.sql`.
2. Specify settings in `/app/settings/local.py`.
3. Run `docker-compose up -d`

#### Start application in production mode
Run `docker-compose -f docker-compose.prod.yml up -d`

#### Insert data for authentication (on application) in first time.
Dump in `/dump/data.sql`.