import falcon


class Ping(object):
    """
        Simple ping endpoint
    """
    def on_get(self, req, resp):
        """ HTTP GET """
        resp.status = falcon.HTTP_200
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
