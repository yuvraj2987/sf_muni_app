
config:
	docker-compose config

build:
	docker-compose build

full-build:
	docker-compose build --force-rm --no-cache

up:
	docker-compose up -d
