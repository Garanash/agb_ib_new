FROM python:latest

ADD main.py /app/
ADD database.db /app/
COPY /core /app/core
COPY /models /app/models
COPY /search /app/search
COPY /templates /app/templates
ADD requirements.txt /app/
RUN pip install -r app/requirements.txt

WORKDIR /app/