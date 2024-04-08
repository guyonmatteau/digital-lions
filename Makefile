include .env
export 
.PHONY: app backend frontend

backend:
	docker-compose up --build backend

frontend:
	docker-compose up --build frontend

app:
	python -m streamlit run app/main.py --server.port 80
