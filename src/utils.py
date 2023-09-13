import json
from datetime import datetime


def read_json(name_file):
    '''Функция прочтения json-файла'''
    with open(name_file, "r", encoding='utf-8') as file:
        read_file = file.read()
        data = json.loads(read_file)
    return data

def filter_by_status(dictionary_list):
    '''Фильтрация списка словарей по статусу '''
    filter_status_list = []
    for operations in dictionary_list:
        if "state" in operations and operations["state"] == "EXECUTED":
            filter_status_list.append(operations)
    return filter_status_list

def sort_by_data(dictionary_list, number_of_operations):
    '''Сортировка словарей списка по дате'''
    dictionary_list = sorted(dictionary_list, key=lambda x: x["date"], reverse=True)
    return dictionary_list[:number_of_operations]

def formatted_operation(operation):
    '''форматирование операции'''
    date = datetime.strptime(operation["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
    description = operation["description"]
    to = operation["to"]
    to = to.replace(to[to.index(" ")+1:-4], "**")
    amount = operation["operationAmount"]["amount"]
    name = operation['operationAmount']["currency"]["name"]
    if "from" in operation:
        where = operation["from"]
        where = where.replace(where[where.rfind(" ")+7:-4], "** **** ")
        where = where[:where.find(" ")+5] + ' ' + where[where.find(" ")+5:]
        return f'{date} {description}\n{where} -> {to}\n{amount} {name}'
    return f"{date} {description}\n{to}\n{amount} {name}"
