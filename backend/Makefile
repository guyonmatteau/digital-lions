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

lint: 
	poetry run ruff check app

format: lint
	poetry run ruff format app

db.check:
	cd app; poetry run alembic check


