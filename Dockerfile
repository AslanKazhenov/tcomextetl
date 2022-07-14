FROM python:3.9-slim-buster


COPY requirements.txt /tmp/

RUN mkdir /code /data /temp /config

WORKDIR /code

COPY tasks /code/tasks
COPY tcomextetl /code/tcomextetl
COPY misc /code/misc
COPY settings.py /code/

COPY conf/luigi.cfg /etc/luigi/luigi.cfg

ENV PYTHONPATH="/code/:/code/tasks/:${PATH}"
ENV DATA_PATH="/data"
ENV TEMP_PATH="/temp"


RUN mkdir /var/lib/luigi

RUN pip install -r /tmp/requirements.txt

EXPOSE 8082
