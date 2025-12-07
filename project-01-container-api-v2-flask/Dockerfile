# Dockerfile

FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

# System deps for psycopg2
RUN apt-get update \
  && apt-get install -y build-essential libpq-dev \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY app ./app

ENV ENVIRONMENT=container

EXPOSE 8000

CMD ["python", "-m", "flask", "--app", "app.main:create_app", "run", "--host=0.0.0.0", "--port=8000"]
