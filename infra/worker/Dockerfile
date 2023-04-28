FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

ARG ROOT_APP=/app

COPY services/worker/requirements.txt $ROOT_APP/requirements.txt

WORKDIR $ROOT_APP

RUN pip install -r requirements.txt

COPY services/worker/src $ROOT_APP/

CMD python main.py
