FROM python:3.9

RUN apt-get update
RUN apt-get install -y vim

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt

COPY . /app

CMD [ "/bin/bash" ]