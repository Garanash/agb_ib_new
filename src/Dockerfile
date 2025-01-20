FROM python:latest

COPY . /src
RUN pip install -r src/requirements.txt

WORKDIR /src/

CMD ["python", "main.py"]