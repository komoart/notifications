FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1

ARG ROOT_APP=/app/

RUN apt-get update && \
    apt-get install -y postgresql-client && \
    apt-get clean

RUN mkdir -p $ROOT_APP/static && \
    mkdir $ROOT_APP/media

COPY services/app_admin/requirements.txt $ROOT_APP/requirements.txt

WORKDIR $ROOT_APP

RUN pip install -r requirements.txt

COPY services/app_admin/entrypoint.sh $ROOT_APP/entrypoint.sh
COPY services/app_admin/gunicorn.conf.py $ROOT_APP/gunicorn.conf.py
COPY services/app_admin/src $ROOT_APP

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
