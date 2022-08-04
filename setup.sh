#!/usr/bin/env bash

sudo docker network create --driver bridge local_network_1 || true
#docker-compose -f docker-compose-redash.yml run --rm server create_db