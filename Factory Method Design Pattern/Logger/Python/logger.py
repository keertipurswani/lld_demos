from enum import Enum


# Logger types ENUM
class LoggerLevel(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    ERROR = "ERROR"


# Logger interface
# Python doesn't have interfaces(natively), hence we use a class.
class ILogger:

    def log(self, message: str):
        pass


class DebugLogger(ILogger):

    def __init__(self):
        pass

    def log(self, message: str):
        print(f"{LoggerLevel.DEBUG.value}: {message}")


class InfoLogger(ILogger):

    def __init__(self):
        pass

    def log(self, message: str):
        print(f"{LoggerLevel.INFO.value}: {message}")


class ErrorLogger(ILogger):

    def __init__(self):
        pass

    def log(self, message: str):
        print(f"{LoggerLevel.ERROR.value}: {message}")


class LoggerFactory():

    def create_logger(self):
        pass


class DebugLoggerFactory(LoggerFactory):

    def create_logger(self):
        return DebugLogger()


class InforLoggerFactory(LoggerFactory):

    def create_logger(self):
        return InfoLogger()


class ErrorLoggerFactory(LoggerFactory):

    def create_logger(self):
        return ErrorLogger()


def main():
    debug_factory = DebugLoggerFactory()
    logger = debug_factory.create_logger()

    logger.log("This is a debug log msg")


if __name__ == "__main__":
    main()
