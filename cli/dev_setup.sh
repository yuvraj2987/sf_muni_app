#! /usr/bin/env bash
#
# Setup dev virtualenv
#

echo "Create virtual env"
python3 -m venv .virtualenv

echo "Source virtual env"
source .virtual/bin/env

echo "Install app requirements"
pip install -r app-srv/requirements.txt
