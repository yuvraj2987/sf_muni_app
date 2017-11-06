"""
    Setup app before it starts
"""

import logging

APP_NAME = "Sf_Muni_App"


def configure_logger():
    """
        Configure logger to be used by app
    """
    logger = logging.getLogger(APP_NAME)
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s|"
                                  + "%(name)s| %(levelname)-2s|"
                                  + "%(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
# end of configure_logger method

