import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }
    ]

@pytest.mark.parametrize("currency, expected_count, expected_id", [
    ("USD", 1, 939719570),
    ("RUB", 1, 873106923),
    ("EUR", 0, None)
])
def test_filter_by_currency(sample_transactions, currency, expected_count, expected_id):
    transactions = list(filter_by_currency(sample_transactions, currency))
    assert len(transactions) == expected_count
    if expected_count > 0:
        assert transactions[0]["id"] == expected_id

@pytest.mark.parametrize("transactions, expected", [
    ([
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"}
    ], ["Перевод организации", "Перевод со счета на счет"]),
    ([], [])
])
def test_transaction_descriptions(transactions, expected):
    assert list(transaction_descriptions(transactions)) == expected

@pytest.mark.parametrize("start, end, expected", [
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (9999999999999997, 9999999999999999, ["9999 9999 9999 9997", "9999 9999 9999 9998", "9999 9999 9999 9999"])
])
def test_card_number_generator(start, end, expected):
    assert list(card_number_generator(start, end)) == expected

