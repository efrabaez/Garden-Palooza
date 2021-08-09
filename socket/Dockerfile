FROM python:3.8-slim-buster

RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean

RUN mkdir /socket-server
COPY requirements.txt /socket-server
WORKDIR /socket-server
RUN pip3 install -r requirements.txt

COPY . /socket-server

RUN chmod u+x ./entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]