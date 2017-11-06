"""
    Storage classes
"""
import logging
import redis
import hashlib
from app.setup import APP_NAME

logger = logging.getLogger(APP_NAME)

class RedisClient(object):
    """
        Wrapper around redis client
    """
    _conn = None

    def __init__(self):
        pass

    @classmethod
    def setup(cls, host, port, db=0):
        """
            Configure redis connections
        """
        cls._conn = redis.StrictRedis(host=host, port=port, db=db)
    # end of method

    @staticmethod
    def _get_hash(key):
        """
            Return hash value of key
        """
        return hashlib.sha1(bytes(key, "utf-8")).hexdigest()

    def set(self, key, val):
        """
            Use sha1 to get hash of key and set value
        """
        key_hash = self._get_hash(key)
        logger.debug("%s key hash is %s", key, key_hash)
        return self._conn.set(key_hash, val)

    def get(self, key):
        """
            Get value of key from redis
        """
        key_hash = self._get_hash(key)
        logger.debug("Fetch %s key with hash %s", key, key_hash)
        return self._conn.get(key_hash)

    def exists(self, key):
        """
            Checks if key exists in redis
        """
        key_hash = self._get_hash(key)
        return self._conn.exists(key_hash)
# end of class
