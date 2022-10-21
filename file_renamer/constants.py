from typing import Callable

from .formatters import format_to_snake_case
from .models import LoggingLevel

# fmt: off
WHITELIST_EXTENSIONS: list[str] = [
    "pdf", "xlsx", "jpg", "csv", "txt", "zip",
    "tif", "docx",
]
# fmt: on
PRIVATE_HEADERS: list[str] = [".", "_"]

FORMATTER: Callable = format_to_snake_case
LOGGER_VERBOSE: LoggingLevel = LoggingLevel.INFO