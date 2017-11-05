#! /usr/bin/env python3
import falcon
import logging
from app.setup import APP_NAME, configure_logger
from app.resources.basic import Ping, Hello
from app.resources.agency import Agency

configure_logger()
logger = logging.getLogger(APP_NAME)
logger.info("Setup Falcon app")
app = falcon.API()
# list of routes
app.add_route("/", Hello())
app.add_route("/ping", Ping())
app.add_route("/agency", Agency())
