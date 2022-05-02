FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt update && apt install -y libpq-dev python-dev postgresql postgresql-contrib
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
