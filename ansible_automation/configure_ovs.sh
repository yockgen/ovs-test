ovs-vsctl del-br yockgen-br1
ovs-vsctl add-br yockgen-br1

ovs-docker add-port yockgen-br1 eth1 yockgen01 --ipaddress=173.16.1.10/24
ovs-docker add-port yockgen-br1 eth1 yockgen02 --ipaddress=173.16.1.11/24

docker exec -it yockgen01 ip a
docker exec -it yockgen02 ip a
