FROM ubuntu:latest

ARG DEBIAN_FRONTEND=noninteractive

ARG DPDK_BRANCH=v21.02

ARG PKTGEN_BRANCH=pktgen-21.02.0

ENV DPDK_BRANCH v21.02
ENV PKTGEN_BRANCH pktgen-21.02.0

RUN apt-get update -y

RUN apt-get install -y lua5.3 liblua5.3-dev libconfig-dev libjson-c-dev libcurl4-openssl-dev libsystemd-dev libssl-dev

RUN apt-get install -y libpcap-dev libnuma-dev

RUN apt-get install -y python3 python3-pip python3-setuptools python3-wheel

RUN apt-get install -y git wget unzip

RUN pip3 install meson

RUN apt-get install -y python3-pyelftools

COPY build.sh /root/

RUN chmod +x /root/build.sh

RUN bash -x /root/build.sh $DPDK_BRANCH $PKTGEN_BRANCH
