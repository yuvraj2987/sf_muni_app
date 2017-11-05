#! /usr/bin/env bash
echo "Clean intermediate images.."
docker rmi $(docker images | grep "^<none>" | awk "{print \$3}")
