import falcon
import logging
from app.setup import APP_NAME

logger = logging.getLogger(APP_NAME)


class Ping(object):
    """
        Simple ping endpoint
    """
    def on_get(self, req, resp):
        """ HTTP GET """
        logger.debug("Ping get request")
        resp.status = falcon.HTTP_OK
        resp.body = "pong"
# end of class


class Hello(object):
    """
        Simple root url endpoint
    """
    def on_get(self, req, resp):
        """ HTTP GET """
        resp.status = falcon.HTTP_200
        resp.body = "Welcome to SF MUNI Rest app"
# end of class
