FROM python:latest

ADD main.py /src/
ADD __init__.py /src/
ADD database.db /src/
COPY /core /src/core

COPY /search /src/search
COPY /templates /src/templates
COPY /auth /src/auth
ADD requirements.txt /src/
RUN pip install -r src/requirements.txt

WORKDIR /src/