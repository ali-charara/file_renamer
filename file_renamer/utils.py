def input_yes_no_answer(yes_no_question: str) -> bool:
    return (
        input(
            f"{yes_no_question[0].upper() + yes_no_question[1:]} [Y]es or [N]o ",
        )
        or "N"
    ) == "Y"
