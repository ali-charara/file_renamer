from typing import Callable

from .formatters import format_to_snake_case
from .models import LoggingLevel

# fmt: off
WHITELIST_EXTENSIONS: list[str] = [
    "pdf", "xlsx", "jpg", "csv", "txt", "zip",
    "tif", "docx", "doc",
]

PROJECT_INDICATORS: list[str] = [
    ".renamer_ignore", ".git", ".obsidian"
    ]

UNWANTED_PATTERNS: list[str] = [
    r"[\s_]\(\d\)$",  r"\[\d{4,}\]$", r"\- Copy$",
    r"[\s_]?copy$",
]
# fmt: on
PRIVATE_HEADERS: list[str] = [".", "_"]


REGEX_UNWANTED_PATTERNS = r"|".join(UNWANTED_PATTERNS)
FORMATTER: Callable = format_to_snake_case
LOGGER_VERBOSE: LoggingLevel = LoggingLevel.INFO
