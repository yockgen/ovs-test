# ovs-test
docker exec -it yockgen01 python3 ./tools/server-udp.py 173.16.2.10 12345  
docker exec -it yockgen02 python3 ./tools/server-udp.py 173.16.2.11 12345  
docker exec -it yockgen01 python3 ./tools/client-udp.py 173.16.2.10 12345 'test yockgen'  
