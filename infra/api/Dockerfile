FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

ARG ROOT_APP=/app

COPY services/notifications/requirements.txt $ROOT_APP/requirements.txt

WORKDIR $ROOT_APP

RUN pip install -r requirements.txt

COPY services/notifications/src $ROOT_APP/

CMD uvicorn main:app --port 8000 --host 0.0.0.0
