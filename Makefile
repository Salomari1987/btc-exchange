help: ## Display this help message
	@echo "Please use \`make <target>' where <target> is one of"
	@perl -nle'print $& if m{^[\.a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'


makemigrations: ## Create migrations
	docker-compose exec btcapp python manage.py makemigrations

migrate: ## Migrate database
	docker-compose exec btcapp python manage.py migrate

install-%: ## type the python/pip package you would like to install after the dash e.g. install-django
	docker-compose exec btcapp pip install $* && docker-compose exec btcapp pip freeze > requirements.txt

update-db: ## update database
	make makemigrations
	make migrate

build-force: ## force build the docker containers without checking cache
	docker-compose build --no-cache

build: ## normal build for docker containers
	docker-compose build

up: ## bring docker container up
	docker-compose up -d

run: ## build a run container
	make build
	make up

shell %: ## access container bash
	docker-compose exec $* bash

provision: ## build the images and containers, this should be your entry point to the application one first run
	make build-force
	make up
	make migrate
	make schedule-jobs

stop: ## stop the docker containers
	make reset-jobs
	docker-compose stop

eject: ## stop the containers and delete them along with volumes
	docker-compose down

restart: ## Restart containers
	docker-compose restart

logs %: ## Display logs
	docker-compose logs $*