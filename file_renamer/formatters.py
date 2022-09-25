import re


def format_to_snake_case(string: str) -> str:
    return re.sub(r"[\s_\-—]+", "_", string.strip()).lower()
