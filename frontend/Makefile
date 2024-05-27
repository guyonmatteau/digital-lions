include .envrc
export

.PHONY: build run format

build:
	docker build -t frontend:latest .

run:
	docker run -p 5173:5173 frontend:latest

format:
	npx prettier --write .

lint: format
	npx eslint .

dev:
	set -o allexport && source .env
	npm run dev


