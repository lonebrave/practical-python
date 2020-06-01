FROM python:alpine

LABEL maintainer Nick Hasser <nick.hasser@gmail.com>t

RUN apk update && \
    apk add bash git vim && \
    rm -rf /var/lib/apt/lists/* && \
    rm /var/cache/apk/*

WORKDIR ./

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD /bin/bash
