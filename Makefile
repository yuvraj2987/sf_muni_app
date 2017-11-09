
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
	docker-compose rm -f -s

logs:
	docker-compose logs -f

exec:
	docker exec -ti sf_muni_app bash

test-up:
	docker-compose -f dockerfiles/docker-compose.test.yml up -d

test-build:
	docker-compose -f dockerfiles/docker-compose.test.yml build
