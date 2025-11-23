FROM python:3.13-slim

WORKDIR /app
COPY ./src /app
COPY ./src/requirements.txt /app
RUN pip install -r requirements.txt

CMD ["python", "main.py"]