FROM python:3.12-slim

LABEL maintainer="aminattaei2000@gmail.com"

ENV PYTHONUPBUFFERD=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN sed -i 's/http:\/\/[a-z-A-Z0-9]*.[a-z-A-Z0-9]*.*.com/http:\/\/ir.ubuntu.sindad.cloud/g' /etc/apt/sources.list \
    && apt-get update -y \
    && apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        python3-dev \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install -i https://mirror-pypi.runflare.com/simple --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

COPY . /app/
