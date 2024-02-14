.PHONY: app

app:
	cd app; uvicorn main:app --host 0.0.0.0 --port 8000 --reload

lint: 
	poetry run black . 
