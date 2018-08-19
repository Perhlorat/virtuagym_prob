FROM alpine

# Initialize
RUN mkdir -p /service
WORKDIR /service
COPY  requirements/base.txt /service

# Setup
RUN apk update
RUN apk upgrade
RUN apk add bash
RUN apk add --update python3 python3-dev postgresql-client postgresql-dev build-base gettext
RUN pip3 install --upgrade pip
RUN pip3 install -r base.txt

# Clean
RUN apk del -r python3-dev postgresql

# Prepare
COPY . /service