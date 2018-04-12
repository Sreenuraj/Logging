import logging
import logging.config


class ReadFromConfig:

    def read_config(self):
        # 1. Read file and create logger
        logging.config.fileConfig('log.conf') #
        logger = logging.getLogger(ReadFromConfig.__name__)

        # test by printing the messages
        logger.debug("Debug message")
        logger.info("Info message")
        logger.warning("warning message")
        logger.error("Error message")
        logger.critical("Critical message")


test = ReadFromConfig()
test.read_config()
