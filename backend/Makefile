.PHONY: app

build:
	docker build -t backend:latest -f Dockerfile .

app:
	cd app; uvicorn main:app --host 0.0.0.0 --port 8000 --reload

lint: 
	poetry run black . 