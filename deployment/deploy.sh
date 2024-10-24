#!/bin/bash
docker compose \
    -f docker-compose.yml \
    -f ./compose-files/docker-compose.backend.yml \
    -f ./compose-files/docker-compose.nginx.yml \
    -f ./compose-files/docker-compose.db.yml \
    "$@";