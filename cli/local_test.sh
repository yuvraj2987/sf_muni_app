#! /usr/bin/env bash

# Todo: Run tests from test docker-compose
echo "Test ping endpoint"
curl http://localhost:8000/ping

echo "Test agency endpoint"
curl http://localhost:8000/agency | jq .

echo "Test agency endpoint after 31s"
sleep 31
curl http://localhost:8000/agency | jq .

echo "Test routes endpoint"
curl http://localhost:8000/route | jq .

#echo "Test routes for sf-muni"
#curl http://localhost:8000/route/sf-muni

