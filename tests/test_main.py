from src.main import main


def test_main():
    assert main("..//operations.json") == ['08.12.2019 Открытие вклада\n Счет **5907\n41096.24 USD', '07.12.2019 Перевод организации\nVisa Classic 2842 87** **** 9012 -> Счет **3655\n48150.39 USD', '19.11.2019 Перевод организации\nMaestro 7810 84** **** 5568 -> Счет **2869\n30153.72 руб.', '13.11.2019 Перевод со счета на счет\nСчет 3861 14** **** 9794 -> Счет **8125\n62814.53 руб.', '05.11.2019 Открытие вклада\n Счет **8381\n21344.35 руб.']

