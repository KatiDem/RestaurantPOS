FROM python:3.8-alpine

WORKDIR /usr/src/app

RUN apk update \
    && apk add postgresql-dev python3-dev libffi-dev openssl-dev musl-dev jpeg-dev zlib-dev libmagic gcc

RUN pip install --upgrade pip

COPY ./requirements-dev.txt /usr/src/app/requirements-dev.txt

RUN pip install -r requirements-dev.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

COPY . /usr/src/app/

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]