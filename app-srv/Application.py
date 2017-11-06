#! /usr/bin/env python3
import falcon
import logging
from app.setup import APP_NAME, configure_logger
from app.resources.basic import Ping, Hello
from app.resources.agency import Agency
from app.storage import RedisClient

configure_logger()
logger = logging.getLogger(APP_NAME)
logger.info("Setup Falcon app")
logger.info("Configure redis client")
RedisClient.setup("redis", 6379)
app = falcon.API()
# list of routes
app.add_route("/", Hello())
app.add_route("/ping", Ping())
app.add_route("/agency", Agency())
