# TODO : 
PROJECT_NAME	:=	test

all:
	docker compose -p $(PROJECT_NAME) up

up-build:
	docker compose -p $(PROJECT_NAME) up --build

down:
	docker compose down

re: down all

frontend-it:
	docker exec -it $(PROJECT_NAME)-frontend-1 bash

backend-it:
	docker exec -it $(PROJECT_NAME)-backend-1 bash

# psql -d test_db -U user
# show database : \l
# show tabel    : \dt
# select * from sample;
db-it:
	docker exec -it $(PROJECT_NAME)-postgres-1 bash

.PHONY: all up-build down re frontend-it backend-it db-it
