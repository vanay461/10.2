import pytest
from src.widget import mask_account_card, get_date

def test_mask_account_card_valid_account():
    assert mask_account_card("Счет 12345678") == "Счет **5678"

def test_mask_account_card_valid_card():
    assert mask_account_card("Visa Platinum 1234567812345678") == "Visa Platinum 1234 56** **** 5678"

def test_mask_account_card_invalid_format():
    with pytest.raises(ValueError, match="Неверный формат строки для карты."):
        mask_account_card("InvalidFormat")

def test_get_date_valid():
    assert get_date("2023-01-20T12:00:00") == "20.01.2023"

def test_get_date_invalid_format():
    with pytest.raises(ValueError):
        get_date("invalid-date")
