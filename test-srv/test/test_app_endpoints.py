import requests
import logging
from falcon import HTTP_OK, HTTP_NO_CONTENT

_logger = logging.getLogger(__name__)


class TestApp(object):
    """
        Test App endpoints
    """
    def setup(self):
        self.app = "app:8000"

    def test_ping(self):
        ping_url = "http://{}/ping".format(self.app)
        resp = requests.get(ping_url)
        _logger.debug("Response status code %d", resp.status_code)
        assert resp.status_code == 200

    def test_agency_list(self):
        url = "http://{}/agency".format(self.app)
        resp = requests.get(url)
        _logger.debug("Test status code")
        assert resp.status_code == 200
        _logger.debug("Test content type")
        _logger.debug("actual %s", resp.headers.get("content-type", ""))
        assert resp.headers.get('content-type', "") == "application/json"
        _logger.debug("Test data")
        data = resp.json()
        assert type(data) == list
        item = data[0]
        has_fields = [k in ["tag", "title", "shortTitle"]
                      for k in item]
        has_field = reduce(lambda x, y: y and x, has_fields)
        assert has_field



# end of class
