#!/bin/bash

docker_id=$(sudo docker run -dp 5433:5432 -e POSTGRES_PASSWORD=$PASSWORD -e POSTGRES_USER=$USERNAME \
    -v ./sql/create_db.sql:/create_db.sql -e POSTGRES_DB=$DATABASE \
    -e DATABASE=$DATABASE -e POSTGRES_USER=$POSTGRES_USER postgres)

sleep 1.0;
sudo docker exec -it $docker_id psql -U $POSTGRES_USER -d $DATABASE -f create_db.sql
