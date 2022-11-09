import logging
from enum import Enum


class LoggingLevel(int, Enum):
    NOTSET = logging.NOTSET
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    CRITICAL = logging.CRITICAL
    ERROR = logging.ERROR
