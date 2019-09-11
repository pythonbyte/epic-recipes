FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN mkdir /code

WORKDIR /code

ADD . /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt