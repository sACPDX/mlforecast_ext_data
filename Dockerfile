FROM python:3

WORKDIR /usr/src/mlf_ext_data_fred_api.py

COPY Pipfile ./

COPY Pipfile.lock ./

ENV PIPENV_VENV_IN_PROJECT 1

RUN pipenv install

COPY . .
