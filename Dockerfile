FROM python:3.11.4-slim-buster
LABEL authors="lalkeen"
ENV PYTHONUNBUFFERED=1

WORKDIR ./

RUN pip install --upgrade pip
COPY ./requirements.txt .
COPY ./requirements-dev.txt .
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt
COPY . .
