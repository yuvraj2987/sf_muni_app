"""
    Utilities for call NextBus XML server
    and return json object
"""
import requests
import logging
from xml.etree import ElementTree as ET
from app.setup import APP_NAME


logger = logging.getLogger(APP_NAME)

NEXT_URL = "http://webservices.nextbus.com/service/publicXMLFeed"


def get_bus_data(cmd, arg=None):
    """
        Return json data for xml feed
        @input:
            cmd = string
            args = list of arguments to command
        @output:
            json data or None
    """
    if cmd is None:
        return None
    cmd_url = "{}?command={}".format(NEXT_URL, cmd)
    logger.debug("command url %s", cmd_url)
    try:
        resp = requests.get(cmd_url)
        json_data = xml_to_json(resp.content)
        logger.debug("next api data=%s", str(json_data))
        return json_data
    # Todo: Remove generic excpetion handler
    except Exception as e:
        logger.error("Exception while fetching data %s", str(e))
        return None

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
