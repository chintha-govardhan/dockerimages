FROM quay.io/cgrepo/ubuntu:latest

RUN apt update -y 

RUN apt install -y vim

RUN apt install -y net-tools

RUN apt install -y iproute2

RUN apt install -y tcpdump

RUN apt install -y iputils-ping

RUN apt install -y curl

RUN apt install -y nginx

RUN apt install -y pciutils

COPY startup.sh /startup.sh

CMD bash -x /startup.sh
