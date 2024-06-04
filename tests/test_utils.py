from src.utils import formatted_date, mask_card, load_operations_json


def test_formatted_date():
    assert formatted_date('2018-04-14T19:35:28.978265') == '14.04.2018'
    assert formatted_date('2019-07-13T18:51:29.313309') == '13.07.2019'


def test_mask_card():
    assert mask_card('Visa Gold 7305799447374042') == 'Visa Gold 7305 79** **** 4042'
    assert mask_card('Счет 90562872508279542248') == 'Счет **2248'


def test_load_operations_json():
    expected_operation_first = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }
    expected_operation_last = {
        "id": 667307132,
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309",
        "operationAmount": {
            "amount": "97853.86",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612"
    }
    assert load_operations_json()[0] == expected_operation_first
    assert load_operations_json()[-1] == expected_operation_last
