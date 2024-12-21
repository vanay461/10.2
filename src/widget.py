from src.masks import get_mask_card_number, get_mask_account  # Импортируем готовые функции из модуля masks

from src.masks import get_mask_card_number, get_mask_account  # Импорты от корня проекта


def mask_account_card(input_data: str) -> str:
    """
    Обрабатывает информацию о картах и счетах, возвращая замаскированную строку.

    :param input_data: строка, содержащая тип и номер карты или счета.
    :return: строка с замаскированным номером.
    """
    input_data = input_data.strip()  # Убираем лишние пробелы

    if input_data.lower().startswith('счет'):  # Проверяем, начинается ли строка со слова "Счет"
            account_number = input_data.split(" ", 1)[1]  # Отделяем номер счета
            masked_account = get_mask_account(account_number)  # Маскируем номер счета
            return f"Счет {masked_account}"  # Возвращаем строку в формате "Счет **XXXX"


    else:
            card_parts = input_data.rsplit(" ", 1)  # Разделяем на название и номер карты
            if len(card_parts) != 2:
                raise ValueError("Неверный формат строки для карты. Ожидается '<тип карты> <номер>'.")

            card_name = card_parts[0]  # Тип карты (например, "Visa Platinum")
            card_number = card_parts[1]  # Номер карты
            masked_card = get_mask_card_number(card_number)  # Маскируем номер карты
            return f"{card_name} {masked_card}"  # Возвращаем строку в формате "Тип карты XXXX XX** **** XXXX"


from datetime import datetime


def get_date(date_string: str) -> str:
    # Преобразуем строку в объект datetime
    date_obj = datetime.fromisoformat(date_string)

    # Форматируем в 'DD.MM.YYYY'
    return date_obj.strftime('%d.%m.%Y')
