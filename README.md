# Restaurant POS system
> This is a Restaurant POS api.

## Dependencies
The base project dependencies:

- docker
- python version 3.8 +
- django 3.1.3
- PostgreSQL 
- djangorestframework 3.12.2
- redis
- celery

The complete list of dependencies can be found at backend/requirements.txt, backend/requirements-dev.txt.

## Usage
Create 3 files in main folder:
.env.dev 
```
DEBUG=1
SECRET_KEY=*YOUR_KEY*
DJANGO_ALLOWED_HOSTS=*
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=django_dev
SQL_USER=django
SQL_PASSWORD=django_pass
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
REDIS_URL=redis://redis:6379
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=email@gmail.com
EMAIL_HOST_PASSWORD=Password
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=email@gmail.com
CORS_ORIGIN_WHITELIST=front-end url
```
.env.staging
```
DEBUG=0
SECRET_KEY=you-will-never-guess
DJANGO_ALLOWED_HOSTS=*
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=hello_django_prod
SQL_USER=hello_django
SQL_PASSWORD=hello_django
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=email@gmail.com
EMAIL_HOST_PASSWORD=Password
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=email@gmail.com
CORS_ORIGIN_WHITELIST=front-end url
```
.env.staging.db
```
POSTGRES_USER=hello_django
POSTGRES_PASSWORD=hello_django
POSTGRES_DB=hello_django_prod
```
Update the file permissions locally:
```
$ chmod +x entrypoint.production.sh
$ chmod +x entrypoint.staging.sh
$ chmod +x entrypoint.sh
```

and run docker:
---
### Development:
```
# Up
$ make build-dev

# Navigate to:
# - admin http://localhost:8080/main/admin/
# - api (swagger) http://localhost:8080/main/api/v1/

# Logs
$ make logs-dev

# if you need to do something inside container
$ docker-compose exec <name of container, for example - web or frontend or db> <command, for example - python manage.py ... >
# example
$ docker-compose exec db psql --username=hello_django --dbname=hello_django_dev

# Down
$ make stop-dev
```
---
### Staging:
```
# Up
$ make build-staging

# Navigate to:
# - admin http://localhost:1337/main/admin/
# - api (swagger) http://localhost:1337/main/api/v1/

# Logs
$ make logs-staging

# if you need to do something inside container
$ docker-compose -f docker-compose.staging.yml exec <name of container, for example - web or frontend or db> <command, for example - python manage.py ... > 

# Down
$ make stop-staging
```
---