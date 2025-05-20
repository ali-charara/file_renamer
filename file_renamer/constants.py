from typing import Callable

from .formatters import format_to_snake_case
from .models import LoggingLevel

# fmt: off
WHITELIST_EXTENSIONS: list[str] = [
    "pdf", "xlsx", "jpg", "txt", "zip",
    "tif", "docx", "doc", "pptx", "png",
    "jpeg"
]

PROJECT_INDICATORS: list[str] = [
    ".renamer_ignore", ".git", ".obsidian", "data",
    "train", "test"
    ]

PRIVATE_HEADERS: list[str] = [".", "_"]

UNWANTED_PATTERNS: list[str] = [
    r"\s\(\d\)$",  r"\[\d{4,}\]$", r"\- Copy$",
    r"\s?copy$",
]
# fmt: on
REGEX_UNWANTED_PATTERNS = r"|".join(UNWANTED_PATTERNS)

FORMATTER: Callable = format_to_snake_case
LOGGER_VERBOSE: LoggingLevel = LoggingLevel.INFO
