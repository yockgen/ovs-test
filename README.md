# Open vSwitch test case

## Setup OvS bridge and installed test containers
./ovs-test.sh 

- assumption that user environment has two hosts  
- run ./ovs-test.sh on all targets host(s)
- Make sure change remote_ip according to host NIC IP address (not local IP but remote target host IP)
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


## Rebuild container image (if needed)
docker rm -vf $(docker ps -a -q)  
docker rmi $(docker images --filter "dangling=true" -q --no-trunc)  
docker build -t yockgen/tools:latest .  
docker tag yockgen/tools yockgen/tools  
docker push yockgen/tools  

