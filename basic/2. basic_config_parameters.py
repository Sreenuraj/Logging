"""
For reference:
https://docs.python.org/3/library/logging.html#logrecord-attributes
https://docs.python.org/3/library/time.html#time.strftime
"""
import logging

logging.basicConfig(filename='/Users/lz69/Downloads/test.log', format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
logging.warning("warning message")
logging.info("info message")
logging.error("error message")

