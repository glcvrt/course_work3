import json
from utils import opener, sorting, formating

def operations_on_accounts(file):
    list_operations = opener(file)

    final_list = sorting(list_operations)

    for operation in final_list:
        print(formating(operation))
        print()

operations_on_accounts("operations.json")
