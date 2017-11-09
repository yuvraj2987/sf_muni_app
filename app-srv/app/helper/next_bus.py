"""
    Utilities for call NextBus XML server
    and return json object
"""
import requests
import logging
import json
from xml.etree import ElementTree as ET
from app.setup import APP_NAME


logger = logging.getLogger(APP_NAME)

NEXT_URL = "http://webservices.nextbus.com/service/publicXMLFeed"


def get_bus_data(cmd, **kwargs):
    """
        Return json data for xml feed
        @input:
            cmd = string
            kwargs = list of arguments to command with arg name and
            value.
        @output:
            json formatted string
    """
    if cmd is None:
        return None
    if kwargs is not None:
        arg_str = "&".join(["{}={}".format(k, v)
                            for k, v in kwargs.items()])
        logger.debug("Argument str = %s", arg_str)
        cmd = "{}&{}".format(cmd, arg_str)
    # end of if
    cmd_url = "{}?command={}".format(NEXT_URL, cmd)
    logger.debug("command url %s", cmd_url)
    try:
        resp = requests.get(cmd_url)
        json_data = xml_to_json(resp.content)
        logger.debug("%s", json_data)
        return json.dumps(json_data)
    # Todo: Remove generic excpetion handler
    except Exception as e:
        logger.error("Exception while fetching data %s", str(e))
        return ""
# end of method


def xml_to_json(xml_str):
    """
        Convet xml tree to json data
    """
    root = ET.fromstring(xml_str)
    ret_data = []
    for child in root:
        ret_data.append(child.attrib)
    # end of for
    return ret_data
#

