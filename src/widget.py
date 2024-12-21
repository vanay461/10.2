from masks import get_mask_card_number, get_mask_account  # Импортируем готовые функции из модуля masks

def mask_account_card(input_data: str) -> str:
    """
    Обрабатывает информацию о картах и счетах, возвращая замаскированную строку.

    :param input_data: строка, содержащая тип и номер карты или счета.
    :return: строка с замаскированным номером.
    """
    input_data = input_data.strip()  # Убираем лишние пробелы
    if input_data.lower() == "счет" or "счёт":  # Проверяем, начинается ли строка со слова "Счет"
        account_number = input_data.split(" ", 1)[1]  # Отделяем номер счета
        masked_account = get_mask_account(account_number)  # Маскируем номер счета
        return f"Счет {masked_account}"  # Возвращаем строку в формате "Счет **XXXX"

    else:
        card_parts = input_data.rsplit(" ", 1)  # Разделяем на название и номер карты
        card_name = card_parts[0]  # Тип карты (например, "Visa Platinum")
        card_number = card_parts[1]  # Номер карты
        masked_card = get_mask_card_number(card_number)  # Маскируем номер карты
        return f"{card_name} {masked_card}"  # Возвращаем строку в формате "Тип карты XXXX XX** **** XXXX"