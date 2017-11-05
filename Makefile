
config:
	docker-compose config

build:
	docker-compose build

full-build:
	docker-compose build --force-rm --no-cache

clean_images:
	bash cli/clean_images.sh

up: stop
	docker-compose up -d

stop:
	docker-compose stop
