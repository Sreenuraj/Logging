import logging
import CustomLogger.custom_logger as cl


class TestCustomLogger:

    # a generic log object for any method in the class
    log = cl.custom_logger(logging.DEBUG)

    def test1(self):
        self.log.debug("debug message")
        self.log.info("Info message")
        self.log.warning("warning message")
        self.log.error("error message")
        self.log.critical("critical message")

    def test2(self):
        # custom log object for this method
        log1 = cl.custom_logger(logging.INFO)
        log1.debug("debug message")
        log1.info("info message")
        log1.critical("critical message")


test = TestCustomLogger()
test.test1()
test.test2()