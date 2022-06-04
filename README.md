# Open vSwitch test cases

## Setup OvS bridge and install test containers
./ovs-test.sh 

- assumption that user environment has two hosts  
- run ./ovs-test.sh on all targets host(s)
- Make sure update remote_ip according to remote target valid NIC IP address
```
#!/bin/sh
....
ovs-vsctl del-br yockgen-br1
ovs-vsctl add-br yockgen-br1
ovs-vsctl add-port yockgen-br1 gre0 -- set interface gre0 type=gre options:remote_ip=173.16.1.200
...
```


## Test Case 1: UDP 
- Host A   
docker exec -it yockgen01 python3 ./tools/server-udp.py 173.16.2.10 12345  
docker exec -it yockgen02 python3 ./tools/server-udp.py 173.16.2.11 12345  
- Host B   
docker exec -it yockgen01 python3 ./tools/client-udp.py 173.16.2.10 12345 'test udp'  

## Test Case 1: TCP
- Host A   
docker exec -it yockgen01 python3 ./tools/server.py 173.16.2.10 12345  
docker exec -it yockgen02 python3 ./tools/server.py 173.16.2.11 12345  
- Host B   
docker exec -it yockgen01 python3 ./tools/client.py 173.16.2.10 12345 'test tcp'  


## OvS Load Balancing (experimental, WIP)  
- ovs-ofctl del-groups yockgen-br1  
- ovs-ofctl -O openflow13 add-group yockgen-br1 "group_id=100 type=select selection_method=dp_hash bucket=output:a27bbf253fb64_l bucket=mod_nw_dst:173.16.2.11,output:0d6a1cd3ad574_l"  
- ovs-ofctl -O openflow13 add-flow yockgen-br1 "table=0,ip,nw_dst=173.16.2.0/24,actions=group:100"  

Run Test Case 1 or 2 to test everything still work as expected.  

## Rebuild container image (if needed)
docker rm -vf $(docker ps -a -q)  
docker rmi $(docker images --filter "dangling=true" -q --no-trunc)  
docker build -t yockgen/tools:latest .  
docker tag yockgen/tools yockgen/tools  
docker push yockgen/tools  

