#! /usr/bin/env python3
import falcon

app = falcon.API()


class Ping(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = "pong"

# end of class

app.add_route("/", Ping())
