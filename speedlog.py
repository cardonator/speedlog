from pydoc import locate


class SpeedLog(object):
    test_classes = dict()
    logger_classes = dict()

    def __init__(self, testers=[], loggers=[]):
        for tester in testers:
            self.register_tester(tester)
        for logger in loggers:
            self.register_logger(logger)

    def register_tester(self, test_class):
        """ passing an import path, registers an object of type test_class to the testers """
        if test_class in self.test_classes:
            return

        obj = locate(test_class)
        self.test_classes[test_class] = obj()
        return

    def register_logger(self, logger_class):
        """ passing an import path, registers an object of type logger_class to the loggers """
        if logger_class in self.logger_classes:
            return

        obj = locate(logger_class)
        self.logger_classes[logger_class] = obj()
        return

    def execute(self):
        """ execute all the testers and pass their results to the loggers """
        for test_class in self.test_classes.values():
            test_class.execute()
            for logger_class in self.logger_classes.values():
                logger_class.log(test_class.get_results())


if __name__ == "__main__":
    SpeedLog(["speedtestlog.SpeedTestLog", "fastlog.FastLog"], ["influx.InfluxLogger"]).execute()
