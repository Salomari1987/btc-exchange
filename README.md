# btc-exchange

## SETUP
* Have Docker installed on your local device
* Build docker images using compose `docker-compose build`
* Create a file at the root of the project called local.env and set the API Key and Django Secret Key (you can go to [Djecrety](https://djecrety.ir/)) inside it:
```env
SECRET_KEY = {secret_key}
ALPHA_ADVANTAGE_API_KEY = {apikey}
```
* Provision box `make provision`
* Create a super user `docker-compose exec btcapp python manage.py createsuperuser --email admin@example.com --username admin`
* Access app at http://localhost:8000

## Help
* Type `make help` for a list of commands you can use

## Technology
* For containers and environment: Docker and Docker Compose
* For REST server: Django and DRF
* DB: Postgres
* For scheduling tasks: Celery, Celery Beat, and Redis