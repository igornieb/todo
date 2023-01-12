FROM python:3.9-apline3.13
LABEL mainteiner="igor niebylski"

ENV PYTHONBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./api /todo/api
COPY ./core /todo/core
COPY ./static /todo/static
COPY ./templates /todo/templates
COPY ./media /todo/media
COPY manage.py /todo/manage.py

WORKDIR /todo
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home todo \





