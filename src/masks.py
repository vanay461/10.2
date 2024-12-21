def get_mask_card_number(card_number: str) -> str:
    """
    Принимает номер карты и возвращает его в замаскированном формате XXXX XX** **** XXXX.
    """
    if not card_number.isdigit():
        raise ValueError("Номер карты должен состоять из цифр.")
    if len(card_number) != 16:
        raise ValueError("Номер карты должен состоять из 16 цифр.")

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Принимает номер счета и возвращает его в замаскированном формате **XXXX.

    :param account_number: Номер счета (строка из цифр)
    :return: Замаскированный номер счета
    """
    if len(account_number) < 4:
        raise ValueError("Номер счета должен состоять хотя бы из 4 цифр.")
    if not account_number.isdigit():
        raise ValueError("Номер счета должен состоять цифр.")
    return f"**{account_number[-4:]}"
