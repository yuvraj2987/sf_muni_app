#! /usr/bin/env bash
#
#   Starts docker-compose.test and get return code for sf_muni_test container
# ------------------------------------------------
echo "Start docker tests..."
docker-compose -f dockerfiles/docker-compose.test.yml up -d
TEST_RESULT=$(docker wait sf_muni_test)
echo "Test result, $TEST_RESULT"

if [ "$TEST_RESULT" -ne 0 ];
then
    echo "Test failed..."
    docker logs sf_muni_test
else
    echo "Test passed...."
fi
echo "Stop docker test containers"
docker-compose -f dockerfiles/docker-compose.test.yml stop
sleep 5
docker ps -aq --no-trunc | xargs docker rm
exit $TEST_RESULT
