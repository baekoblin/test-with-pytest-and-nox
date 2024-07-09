# test_logging.py

import logging

def test_logging():
    logger = logging.getLogger(__name__)
    logger.info("This is a log message")
    assert True
