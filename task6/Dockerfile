FROM python:3.7.9-buster

WORKDIR /app/

COPY Pipfile .
COPY Pipfile.lock .

ENV env 'production'
ENV PYTHONUNBUFFERED 1
RUN pip install pipenv && pipenv install --ignore-pipfile --system

COPY entrypoint.sh .
COPY app app