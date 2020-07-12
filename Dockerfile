from python:3.8-slim

MAINTAINER Shravankumar Nagarajan

COPY . /app
WORKDIR /app

RUN apt-get update && apt-get install -y \
  subversion build-essential libssl-dev \
  libffi-dev python-dev python-pip libsasl2-dev \
  libldap2-dev

RUN pip install pipenv

RUN pipenv install --system --deploy --skip-lock

CMD ["python", "app.py"]