from enum import Enum


# Logger types ENUM
class LoggerLevel(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    ERROR = "ERROR"


# Logger interface
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

    def create_logger(log_level):
        if log_level == LoggerLevel.DEBUG:
            return DebugLogger()
        elif log_level == LoggerLevel.INFO:
            return InfoLogger()
        elif log_level == LoggerLevel.ERROR:
            return ErrorLogger()


def main():
    debug_logger = LoggerFactory.create_logger(LoggerLevel.DEBUG)
    info_logger = LoggerFactory.create_logger(LoggerLevel.INFO)
    error_logger = LoggerFactory.create_logger(LoggerLevel.ERROR)

    debug_logger.log("This is a debug log msg")
    info_logger.log("This is a info log msg")
    error_logger.log("This is a error log msg")


if __name__ == "__main__":
    main()
