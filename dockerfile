FROM python:3.8-slim-buster

RUN mkdir /garden_palooza_be
COPY requirements.txt /garden_palooza_be
WORKDIR /garden_palooza_be
RUN pip3 install -r requirements.txt

COPY . /garden_palooza_be/

RUN chmod u+x ./entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]