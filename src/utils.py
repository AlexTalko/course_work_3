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


def get_last_transaction_date():
    """
        Получает список последних 5 операций по дате.
    """
    last_transactions = sorted(get_operations(), key=lambda x: get_converted_date(x['date']), reverse=True)
    return last_transactions[:5]


def get_req_view_date(date_str):
    """
        Преобразует дату в нужный формат.
    """
    date_trans = date_str.split("T")[0]
    req_view_date = date.fromisoformat(date_trans)
    return req_view_date.strftime("%d.%m.%Y")


def get_trans_data(trans_data):
    """
        Получает данные транзакции в нужном формате.
    """
    number_data = trans_data.split()[-1]
    name_data = trans_data.split()[:-1]
    if name_data[0] == "Счет":
        number_data = "**" + number_data[-4:]
    if name_data[0] != "Счет":
        number_data = f'{number_data[:4]} {number_data[5:7]}** {(len(number_data[8: -4]) * "*")} {number_data[-4:]}'

    return f"{" ".join(name_data)} {number_data}"


def get_from_to(trans_description):
    """
        Выводит адрес(откуда -> куда) транзакции с маскировкой данных.
    """
    if trans_description["description"] != "Открытие вклада":
        data_description = get_trans_data(trans_description["from"]) + " -> " + get_trans_data(trans_description["to"])

    if trans_description["description"] == "Открытие вклада":
        data_description = get_trans_data(trans_description["to"])
    return f"{trans_description["description"]}\n{data_description}"
