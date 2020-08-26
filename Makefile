makemigrations:
	docker-compose exec btcapp python manage.py makemigrations

migrate:
	docker-compose exec btcapp python manage.py migrate

install-%:
	docker-compose exec btcapp pip install $* && docker-compose exec btcapp pip freeze > requirements.txt

update-db:
	make makemigrations
	make migrate

build-force:
	docker-compose build --no-cache

build:
	docker-compose build

up:
	docker-compose up -d

run:
	make build
	make up

bash:
	docker-compose exec btcapp bash

provision-app:
	make build-force
	make run
	make migrate