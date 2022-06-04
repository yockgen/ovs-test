#!/bin/sh

ovs-vsctl del-br yockgen-br1
ovs-vsctl add-br yockgen-br1
ovs-vsctl add-port yockgen-br1 gre0 -- set interface gre0 type=gre options:remote_ip=173.16.1.200

docker rm -vf $(docker ps -a -q)

docker run -d --name yockgen01 yockgen/tools sh -c 'while sleep 3600; do :; done'
ovs-docker add-port yockgen-br1 eth1 yockgen01 --ipaddress=173.16.1.10/16
docker exec -it yockgen01 ip a

docker run -d --name yockgen02 yockgen/tools  sh -c 'while sleep 3600; do :; done'
ovs-docker add-port yockgen-br1 eth1 yockgen02 --ipaddress=173.16.1.11/16
docker exec -it yockgen02 ip a

