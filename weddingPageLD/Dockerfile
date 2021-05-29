FROM python:3-alpine

WORKDIR /usr/src/app

RUN pip install --upgrade pip 
RUN apk update && apk add musl-dev libffi-dev gcc
RUN ls -la ./
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt
RUN pip install uwsgi

EXPOSE 8000

COPY . /usr/src/app

EXPOSE 8000
ENV PORT=8000

CMD ["/usr/src/app/runner.sh"]
