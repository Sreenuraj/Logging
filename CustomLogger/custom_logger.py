import inspect
import logging


def custom_logger(loglevel):

    # below to get the name of the class/method which calls this file
    logger_name = inspect.stack()[1][3]

    # create logger and set level
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # create handler and set level
    file_handler = logging.FileHandler("{}.log".format(logger_name), mode= 'w') # 'a' for append mode
    file_handler.setLevel(loglevel)

    # create formatter and assign to handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)

    # assign handler to logger
    logger.addHandler(file_handler)

    # return the logger
    return logger