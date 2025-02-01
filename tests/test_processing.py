import pytest
from src.processing import filter_by_state, sort_by_date

@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-20T12:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2022-12-15T10:30:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-18T09:00:00"},
    ]

def test_filter_by_state(sample_transactions):
    result = filter_by_state(sample_transactions, state="EXECUTED")
    assert len(result) == 2
    assert all(tr["state"] == "EXECUTED" for tr in result)

def test_sort_by_date_descending(sample_transactions):
    result = sort_by_date(sample_transactions, descending=True)
    assert result[0]["date"] == "2023-01-20T12:00:00"

def test_sort_by_date_ascending(sample_transactions):
    result = sort_by_date(sample_transactions, descending=False)
    assert result[0]["date"] == "2022-12-15T10:30:00"
