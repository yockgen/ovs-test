# Open vSwitch test case

## Setup 
./ovs-test.sh 

## ovs-test
docker exec -it yockgen01 python3 ./tools/server-udp.py 173.16.2.10 12345  
docker exec -it yockgen02 python3 ./tools/server-udp.py 173.16.2.11 12345  
docker exec -it yockgen01 python3 ./tools/client-udp.py 173.16.2.10 12345 'test yockgen'  

## Rebuild container image
docker rm -vf $(docker ps -a -q)  
docker rmi $(docker images --filter "dangling=true" -q --no-trunc)  
docker build -t yockgen/tools:latest .  
docker tag yockgen/tools yockgen/tools  
docker push yockgen/tools  

