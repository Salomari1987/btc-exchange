# btc-exchange

## SETUP
* Have Docker installed on your local device
* Build docker images using compose `docker-compose build`
* Create a file at the root of the project called local.env and set the API Key and Django Secret Key (you can go to [Djecrety](https://djecrety.ir/)) inside it:
```env
SECRET_KEY = {secret_key}
ALPHA_ADVANTAGE_API_KEY = {apikey}
```
* Bring container up using `docker-compose up -d`
* Run migrations `docker-compose exec btcapp python manage.py migrate`
* Create a super user `docker-compose exec btcapp python manage.py createsuperuser --email admin@example.com --username admin`
* Access app at http://localhost:8000