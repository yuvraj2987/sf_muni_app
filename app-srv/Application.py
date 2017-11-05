#! /usr/bin/env python3
import falcon
from app.resources.basic import Ping, Hello

app = falcon.API()


# list of routes
app.add_route("/", Hello())
app.add_route("/ping", Ping())
