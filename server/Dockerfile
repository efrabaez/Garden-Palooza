FROM python:3.8-slim-buster

RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean

RUN mkdir /server
COPY requirements.txt /server
WORKDIR /server
RUN pip3 install -r requirements.txt

COPY . /server

RUN chmod u+x ./entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]