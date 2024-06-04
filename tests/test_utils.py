from src.utils import formatted_date
from src.utils import mask_card


def test_formatted_date():
    assert formatted_date('2018-04-14T19:35:28.978265') == '14.04.2018'
    assert formatted_date('2019-07-13T18:51:29.313309') == '13.07.2019'


def test_mask_card():
    assert mask_card('Visa Gold 7305799447374042') == 'Visa Gold 7305 79** **** 4042'
    assert mask_card('Счет 90562872508279542248') == 'Счет **2278'
