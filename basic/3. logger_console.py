import logging


class LoggerConsoleBasic:

    def basic_method(self):

        # 1. Create the logger and set the log level
        logger = logging.getLogger(LoggerConsoleBasic.__name__)
        logger.setLevel(logging.INFO)

        # 2. Create console_handler. Logger create the log record message and pass it to handler
        console_handler = logging.StreamHandler()  # StreamHandler for writing the log to console
        console_handler.setLevel(logging.INFO)

        # 3. Create Formatter. It formats the log record obj and pass it back to handler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')

        # 4. Add formatter to the console handler
        console_handler.setFormatter(formatter)

        # 5. Add console_handler back to logger
        logger.addHandler(console_handler)

        # to test we will try to print some messages
        logger.debug("Debug message") # which will not appear here as the level is INFO
        logger.info("Info message")
        logger.warning("Warning message")
        logger.error("Error message")
        logger.critical("Critical message")


demo_logger_console = LoggerConsoleBasic()
demo_logger_console.basic_method()





