import falcon
import logging
import json
from app.helper.next_bus import get_bus_data
from app.setup import APP_NAME


logger = logging.getLogger(APP_NAME)


class Agency(object):
    """
        Manage agency resource
    """
    def on_get(self, req, resp):
        """
            Get list of agencies
        """
        logger.info("get agency list")
        data = get_bus_data("agencyList")
        if data is None:
            logger.error("failed to get list for next bus")
            resp.status = falcon.HTTP_NO_CONTENT
            resp.body = ""
        else:
            resp.status = falcon.HTTP_OK
            resp.body = json.dumps(data)
    # end of method

# end of class


