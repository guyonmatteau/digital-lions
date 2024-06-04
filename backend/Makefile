include ../.env
export
.PHONY: app

shell: 
	poetry shell

build:
	docker build -t backend:latest -f Dockerfile .

run:
	docker run -p 8000:8000 backend:latest

app: shell
	cd app; uvicorn main:app --host 0.0.0.0 --port 8000 --reload

format:  shell
	isort --recursive app
	poetry run black app

check.db:
	alembic check

