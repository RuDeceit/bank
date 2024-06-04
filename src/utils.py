import json
from datetime import datetime


def load_operations_json():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        list_operations = []
        for item in data:
            list_operations.append(item)
        return list_operations


def sort_operations():
    list_operations = load_operations_json()
    list_operations_filtered = [op for op in list_operations if "date" in op]
    sorted_operations = sorted(list_operations_filtered, key=lambda x: x["date"])
    return sorted_operations[-5:]


def mask_card(card_number):
    if 'Счет' in card_number:
        masked_number = card_number[:4] + ' **' + card_number[-4:]
        return masked_number
    else:
        masked_number = card_number[:-16] + card_number[-16:-12] + ' ' + card_number[-12:-10] + '** ' + '**** ' + card_number[-4:]
        return masked_number


def formatted_date(date):
    iso_date_str = date
    date_obj = datetime.fromisoformat(iso_date_str)
    return date_obj.strftime('%d.%m.%Y')
