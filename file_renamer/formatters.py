import re


def format_to_snake_case(string: str) -> str:
    return re.sub(
        r"[\s_\-—]+",
        "_",
        re.sub("(?<=[a-z0-9])([A-Z]+)|(?<=[A-Z]{2})([a-z]+)", r" \1", string.strip()),
    ).lower()
