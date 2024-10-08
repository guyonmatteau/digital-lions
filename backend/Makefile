include ../.env
export
.PHONY: shell build run app tests lint format 

SERVICE=backend

shell: 
	poetry shell

build:
	docker compose build ${SERVICE}

run:
	docker compose up ${SERVICE}

deploy:
	cd ..; railway up --service ${SERVICE}-dev --detach --environment dev

app: shell
	cd app; uvicorn main:app --host 0.0.0.0 --port 8000 --reload

test:
	poetry run python -m pytest tests --disable-warnings -vvv --cov=app --cov-report=term-missing tests

testpdb:
	poetry run python -m pytest -vvv --pdb

lint: 
	poetry run ruff check app

format: lint
	poetry run black app
	poetry run ruff format app

# Railway database service vars
TCP_PROXY=monorail.proxy.rlwy.net:19362
HTTP_HOST=postgres.railway.internal:5432
# POSTGRES_DATABASE_URL_PROD=$(shell railway variables -k | grep POSTGRES_DATABASE_URL | sed "s@$HTTP_HOST@$TCP_PROXY@g")

db.check:
	cd app; poetry run alembic check

