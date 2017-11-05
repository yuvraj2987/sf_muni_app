import falcon
from app.helper.next_bus import get_bus_data


class Agency(object):
    """
        Manage agency resource
    """
    def on_get(self, req, resp):
        """
            Get list of agencies
        """
        data = get_bus_data("agencyList")
        if data is None:
            resp.status = falcon.HTTP_NO_CONTENT
            resp.body = ""
        else:
            resp.status = falcon.HTTP_OK
            resp.body = data
    # end of method

# end of class




