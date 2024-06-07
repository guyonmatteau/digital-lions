include ../.env
export
.PHONY: app

shell: 
	poetry shell

build:
	docker-compose build backend

run:
	docker-compose up backend

app: shell
	cd app; uvicorn main:app --host 0.0.0.0 --port 8000 --reload

format:  shell
	poetry run isort --recursive app
	poetry run black app

check.db:
	alembic check

