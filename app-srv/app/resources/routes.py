"""
    Handles requests for routes with agency parameter
"""
import falcon
import logging
import json
from app.helper.next_bus import get_bus_data
from app.setup import APP_NAME
from app.storage import RedisClient

logger = logging.getLogger(APP_NAME)


class Routes(object):
    """
        Handlers routes resources
    """
    _redis = RedisClient()

    def on_get(self, req, resp, agency=""):
        """ HTTP GET """
        logger.info("Get route for %s", agency)
        data = get_bus_data("routeList", a=agency)
        if data is None:
            logger.error("failed to get data")
            resp.status = falcon.HTTP_NO_CONTENT
            resp.body = ""
        else:
            resp.status = falcon.HTTP_OK
            resp.body = data
    # end of method
