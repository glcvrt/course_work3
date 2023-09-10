import json

def opener(file_txt):
    '''открывает файл и загружает его как список всех операций'''
    with open(file_txt, "r", encoding='utf-8') as file:
        read_file = file.read()
        data = json.loads(read_file)
    return data


def sorting(list_operations):
    '''возвращает 5 последних операций'''

    sorted_list = []

    final_list = []

    for operations in list_operations: #type: operations:dict

        if operations.get('date', False):
            item = operations['date'][:10] + " " +str(list_operations.index(operations))
            if operations["state"] == "EXECUTED":
                sorted_list.append(item)

    sorted_list = sorted(sorted_list, reverse=True)
    sorted_list = sorted_list[:5]

    for date in sorted_list:
        ind = int(date[-2:])
        final_list.append(list_operations[ind])
    return final_list


def formating(operations):
    '''форматирует операцию и возвращает её в нужном виде'''
    date = operations["date"][8:10] + "." + operations["date"][5:7] + "." + operations["date"][:4]
    description = operations["description"]

    if operations.get('from', False):
        s = operations["from"]
        name_point = s[:s.rfind(" ")]
        point = s[s.rfind(" ") + 1:]
        f_point = point[:4] + ' ' + point[4:6] + '** **** ' + point[-4:]
        from_oper = name_point + ' ' + f_point + ' ->'
    else:
        from_oper = ''

    to = operations["to"]
    to_point = to[to.rfind(' '):]
    to_point = to[:to.rfind(' ')] + ' ' + '**' + to_point[-4:]

    amount = operations["operationAmount"]["amount"]
    currency = operations["operationAmount"]["currency"]["name"]
    return f"{date} {description}\n{from_oper} {to_point}\n{amount} {currency}"