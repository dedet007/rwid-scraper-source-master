#!/usr/bin/env bash
docker-compose -f docker-compose-prod.yml run engine flask db upgrade
