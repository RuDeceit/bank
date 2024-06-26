from src.utils import sort_operations
from src.utils import formatted_date
from src.utils import mask_card


def main():
    """
    Основная функция для отображения последних пяти операций
    """
    sorted_operations = sort_operations()
    for operation in sorted_operations:
        operation_amount = operation["operationAmount"]["amount"]
        operation_currency = operation["operationAmount"]["currency"]["name"]
        print(f'\n{formatted_date(operation["date"])} {operation["description"]}')
        if 'from' in operation:
            print(f'{mask_card(operation["from"])} -> {mask_card(operation["to"])}')
        else:
            print(f'{mask_card(operation["to"])}')
        print(operation_amount, operation_currency)


main()
