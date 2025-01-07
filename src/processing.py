from typing import List, Dict


def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список транзакций по заданному состоянию.

    :param transactions: Список транзакций, где каждая транзакция представлена словарем.
                         Пример: [{'id': 1, 'state': 'EXECUTED'}, {'id': 2, 'state': 'CANCELED'}]
    :param state: Состояние транзакции для фильтрации (по умолчанию 'EXECUTED').
    :return: Новый список транзакций, отфильтрованный по указанному состоянию.
             Пример: [{'id': 1, 'state': 'EXECUTED'}]
    """
    return [transaction for transaction in transactions if transaction["state"] == state]


def sort_by_date(transactions: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по дате.

    :param transactions: Список транзакций (словарей), где каждый словарь содержит ключ 'date'.
    :param descending: Флаг, указывающий порядок сортировки. По умолчанию True (убывающее).
    :return: Новый отсортированный список транзакций.
    """
    return sorted(transactions, key=lambda x: x["date"], reverse=descending)
