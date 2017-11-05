#! /usr/bin/env bash
echo "Starting application...."
PYTHONPATH="./app"
gunicorn -b 0.0.0.0:8000 Application:app
