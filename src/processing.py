def filter_by_state(transactions, state='EXECUTED'):
    return [transaction for transaction in transactions if transaction['state'] == state]
from typing import List, Dict


def sort_by_date(transactions: List[Dict], descending: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по дате.

    :param transactions: Список транзакций (словарей), где каждый словарь содержит ключ 'date'.
    :param descending: Флаг, указывающий порядок сортировки. По умолчанию True (убывающее).
    :return: Новый отсортированный список транзакций.
    """
    return sorted(transactions, key=lambda x: x['date'], reverse=descending)