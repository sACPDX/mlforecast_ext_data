FROM python:3

WORKDIR /usr/src/mlforecast

COPY Pipfile ./

COPY Pipfile.lock ./

ENV PIPENV_VENV_IN_PROJECT 1

RUN pipenv install

COPY . .
