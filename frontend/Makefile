include .env
export

.PHONY: build run format

build:
	docker build -t frontend:latest .

run:
	docker run -p 5173:5173 frontend:latest

format:
	npx prettier --write src

lint: format
	npx eslint src

app:
	npm run dev

precommit: 
	pre-commit run --all-files

