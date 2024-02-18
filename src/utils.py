import json
from datetime import date


def get_operations():
    """
    Получает список выполненных операций из файла operations.json
    """
    with open("D:/pythonProject/course_work_3/operations.json", "r", encoding="utf-8") as f:
        transactions = json.load(f)
        executed_transactions = []
        for transaction in transactions:
            if transaction.get('state') == "EXECUTED":
                executed_transactions.append(transaction)
                if transaction.get('state') is None:
                    continue
        return executed_transactions


def get_converted_date(date_str):
    """
    Преобразует строку даты в дату.
    """
    date_trans = date_str.split("T")[0]
    converted_date = date.fromisoformat(date_trans)
    return converted_date
