FROM --platform=linux/amd64 python:3.11.5-slim

ARG POETRY_VERSION=1.6.1

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry==$POETRY_VERSION
RUN poetry config virtualenvs.create false \
    && poetry install --without test --no-root --no-interaction

COPY app ./

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=30s \
    CMD curl -f http://localhost:8000/health/ || exit 1

RUN groupadd -r api && useradd --no-log-init -r -g api api
USER api

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
