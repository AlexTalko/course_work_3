from src.utils import get_operations, get_last_transaction_date, get_req_view_date, get_from_to

executed_transactions = get_operations()  # Получаем список выполненных операций из файла

last_transactions = get_last_transaction_date()  # Получаем список последних 5 операций по дате


def main():
    """
        Выводим 5 последних 5 операций по дате, в нужном формате.
    """
    for transaction in last_transactions:
        transaction = (f"{get_req_view_date(transaction['date'])} "
                       f"{get_from_to(transaction)}\n"
                       f"{transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']
                       ['name']}\n")

        print(transaction)


if __name__ == "__main__":
    main()
