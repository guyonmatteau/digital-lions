include ../.env
export
.PHONY: app

build:
	docker build -t backend:latest -f Dockerfile .

run:
	docker run -p 8000:8000 backend:latest

app:
	poetry shell
	cd app; uvicorn main:app --host 0.0.0.0 --port 8000 --reload

lint: 
	poetry run black . 
