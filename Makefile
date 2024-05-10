include .env
export 
.PHONY: app backend frontend

backend:
	docker-compose up --build backend

frontend:
	docker-compose up --build frontend

db: 
	docker-compose up --build db


