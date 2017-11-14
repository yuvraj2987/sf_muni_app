import requests
import logging

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

# end of class
