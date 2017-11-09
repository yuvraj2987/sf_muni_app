#! /usr/bin/env bash
PYTHONPATH="/app-srv/app:/test-srv/test"
echo "Running nosetest"
nosetests -v
