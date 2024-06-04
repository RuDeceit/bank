from src.main import main


def test_main():
    expected_operation_first = '''
    13.11.2019 Перевод со счета на счет
    Счет **9794 -> Счет **8125
    62814.53 руб.'''
    expected_operation_last = '''
    08.12.2019 Открытие вклада
    Счет **5907
    41096.24 USD'''
    assert main()[0] == expected_operation_first
    assert main()[-1] == expected_operation_last
