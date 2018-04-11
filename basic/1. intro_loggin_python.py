import logging

'''
Logging levels
DEBUG
INFO
WARNING
ERROR
CRITICAL
'''

# Configuring the file location and setting the level of logging
logging.basicConfig(filename='/Users/lz69/Downloads/test.log', level=logging.DEBUG)

# Examining the above by printing some logs
logging.warning("A warning msg")
logging.info("Info msg")
logging.error("Error msg")