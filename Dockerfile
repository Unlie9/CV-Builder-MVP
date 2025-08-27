FROM python:3.13.3-slim AS base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

FROM base AS builder
RUN groupadd --gid 2000 node && useradd --uid 2000 --gid node --shell /bin/bash --create-home node

COPY pyproject.toml poetry.lock* README.md ./
RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

RUN pip install poetry \
    && rm -rf /var/lib/apt/lists/* 

WORKDIR /app
COPY --chown=node:node . ./

USER node
EXPOSE 8000

CMD ["python", "app/manage.py", "runserver", "0.0.0.0:8000"]
