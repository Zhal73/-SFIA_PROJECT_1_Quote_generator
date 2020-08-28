#! /bin/bash

docker-compose build
docker login
docker push zhal73/service1
docker push zhal73/service2
docker push zhal73/service3
docker push zhal73/service4
docker stack deploy --compose-file docker-compose.yaml myappstack
