FROM python:3.10

RUN apt-get update && \
    apt-get install -y && \
    pip3 install uwsgi

COPY ./src /opt/src
COPY ./uwsgi.ini /opt/src/uwsgi.ini

RUN pip3 install -r /opt/src/requirements.txt

ENV DOCKER_CONTAINER=1

EXPOSE 8000

CMD ["uwsgi", "--ini", "/opt/src/uwsgi.ini"]
