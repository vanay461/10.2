import pytest
from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number_valid():
    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"

def test_get_mask_card_number_invalid_length():
    with pytest.raises(ValueError, match="Номер карты должен состоять из 16 цифр."):
        get_mask_card_number("1234")

def test_get_mask_card_number_non_digit():
    with pytest.raises(ValueError, match="Номер карты должен состоять из цифр."):
        get_mask_card_number("abcd1234abcd1234")

def test_get_mask_account_valid():
    assert get_mask_account("12345678") == "**5678"

def test_get_mask_account_short_length():
    with pytest.raises(ValueError, match="Номер счета должен состоять хотя бы из 4 цифр."):
        get_mask_account("123")