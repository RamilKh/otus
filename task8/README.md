# Task 7. Django application

#### Build
Run `docker-compose build`

#### Start application in development mode (APPLICATION and DATABASE in localhost)
1. Prepare the database from `/dump/init.sql`.
2. Specify settings in `/app/settings/base.py`.
3. Run `python manage.py runserver`.

#### Start application in local mode (APPLICATION in docker, DATABASE in localhost)
1. Specify settings in `/app/settings/local.py`.
2. Settings to env file `/app/settings/database.env`.
3. Run `docker-compose up -d`.

#### Start application in production mode (APPLICATION and DATABASE in docker)
1. Specify settings in `/app/settings/production.py`.
2. Settings to env file `/app/settings/database.env`.
3. Run `docker-compose -f docker-compose.prod.yml up -d`.

#### Insert test data.
Run `python manage.py initdata`.

#### Commands
- Run `docker-compose down && docker-compose build && docker-compose up -d`.
- Run `docker-compose -f docker-compose.prod.yml down && sleep 2 && docker-compose build --no-cache && sleep 2 && docker-compose -f docker-compose.prod.yml up --build`.