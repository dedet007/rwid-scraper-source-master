#!/usr/bin/env bash
docker-compose -f docker-compose-dev.yml run engine flask db migrate
