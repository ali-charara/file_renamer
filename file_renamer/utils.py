import re


def input_yes_no_answer(yes_no_question: str) -> bool:
    return (
        input(
            f"{yes_no_question} [Y]es or [N]o ",
        )
        or "N"
    ) == "Y"


def remove_unwanted_patterns(string: str, regex_unwanted_patterns: str) -> str:
    return re.sub(regex_unwanted_patterns, " ", string.strip())
