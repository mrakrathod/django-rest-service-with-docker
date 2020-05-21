FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
RUN apk update && pip install -U pip && apk add bash
WORKDIR /app
COPY . /app
COPY requirements.txt /app
COPY . .
RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps musl-dev gcc postgresql-dev && \
    python -m pip install -r requirements.txt --no-cache-dir
