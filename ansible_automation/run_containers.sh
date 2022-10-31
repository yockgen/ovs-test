#!/bin/bash

echo "Clear previous running container"
docker rm -vf $(docker ps -a -q)

echo "Run 1st container - yockgen01"
docker run -d --name yockgen01 alpine sh -c 'while sleep 3600; do :; done'

echo "Run 2nd container - yockgen02"
docker run -d --name yockgen02 alpine sh -c 'while sleep 3600; do :; done'
