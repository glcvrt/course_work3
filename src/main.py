import json
from utils import opener, sorting, formating


def main(file):
    final_list = []
    list_operations = opener(file)

    intermediate_list = sorting(list_operations)

    for operation in intermediate_list:
        operation = formating(operation)
        final_list.append(operation)
        print(operation)
        print()

    return final_list



print(main("..//operations.json"))
