# generators.py

def filter_by_currency(transactions, currency):
    """
    Генератор, который фильтрует транзакции по указанной валюте.

    :param transactions: список словарей с транзакциями
    :param currency: код валюты для фильтрации (например, 'USD')
    :return: итератор транзакций с указанной валютой
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions):
    """
    Генератор, который возвращает описание операций из списка транзакций.

    :param transactions: список словарей с транзакциями
    :return: итератор описаний операций
    """
    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")


def card_number_generator(start, end):
    """
    Генератор номеров карт в формате XXXX XXXX XXXX XXXX.

    :param start: начальное значение диапазона (целое число)
    :param end: конечное значение диапазона (целое число)
    :return: итератор номеров карт
    """
    for number in range(start, end + 1):
        formatted_number = f"{number:016d}"
        yield f"{formatted_number[:4]} {formatted_number[4:8]} {formatted_number[8:12]} {formatted_number[12:]}"