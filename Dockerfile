FROM ubuntu:latest

RUN apt update
RUN apt install iperf iputils-ping iproute2 tcpdump python3 nano -y
COPY ./tools ./tools
