# Dockerfile

# --- Builder image ---
FROM python:3.11-slim AS builder

WORKDIR /app

# System deps (for psycopg2 / builds)
RUN apt-get update && apt-get install -y build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml ./
RUN pip install --upgrade pip && pip install .[dev]

COPY app ./app

# --- Runtime image ---
FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

# System deps
RUN apt-get update && apt-get install -y libpq-dev && rm -rf /var/lib/apt/lists/*

# Copy installed site-packages & code from builder
COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=builder /usr/local/bin /usr/local/bin
COPY app ./app

ENV ENVIRONMENT=container

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
