import falcon
import logging
import json
from app.helper.next_bus import get_bus_data
from app.setup import APP_NAME
from app.storage import RedisClient


logger = logging.getLogger(APP_NAME)


class Agency(object):
    """
        Manage agency resource
    """
    _redis = RedisClient()

    def on_get(self, req, resp):
        """
            Get list of agencies
        """
        logger.info("get agency list")
        logger.debug("request path %s", req.path)
        if self._redis.exists(req.path):
            logger.info("%s key found in cache", req.path)
            data = self._redis.get(req.path)
        else:
            logger.info("%s key not found in cache", req.path)
            data = get_bus_data("agencyList")
            if data is not None:
                logger.info("%s key inserted into cache", req.path)
                self._redis.set(req.path, json.dumps(data))
        #
        if data is None:
            logger.error("failed to get list for next bus")
            resp.status = falcon.HTTP_NO_CONTENT
            resp.body = ""
        else:
            resp.status = falcon.HTTP_OK
            resp.body = json.dumps(data)
    # end of method

# end of class
