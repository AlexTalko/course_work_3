from datetime import date

from src.utils import get_operations, get_last_transaction_date, get_req_view_date, get_converted_date, get_trans_data, \
    get_from_to


def test_get_operations():
    assert type(get_operations()) == list


def test_get_last_transaction_date():
    assert type(get_last_transaction_date()) == list


def test_get_req_view_date():
    assert type(get_req_view_date("2021-01-01")) == str
    assert get_req_view_date("2021-01-01") == "01.01.2021"


def test_get_converted_date():
    assert get_converted_date("2019-08-26T10:50:58.294041") == date(2019, 8, 26)
    assert get_converted_date("2019-08-26") == date(2019, 8, 26)


def test_get_last_transaction_date():
    assert len(get_last_transaction_date()) == 5
    assert type(get_last_transaction_date()) == list
    assert type(get_last_transaction_date()[0]) == dict
    assert type(get_last_transaction_date()[0]["date"]) == str
    assert type(get_last_transaction_date()[0]["operationAmount"]) == dict


def test_get_trans_data():
    assert type(get_trans_data("Maestro 1596837868705199")) == str
    assert type(get_trans_data("Счет 64686473678894779589")) == str


def test_get_from_to():
    assert type(get_from_to({"description": "Перевод организации",
                             "from": "MasterCard 7158300734726758",
                             "to": "Счет 35383033474447895560"})) == str
    assert type(get_from_to({"description": "Открытие вклада",
                             "to": "Счет 41421565395219882431"})) == str
