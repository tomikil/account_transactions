import json
from datetime import datetime
import os


def load_word(file):
    """
    Загрузка истории операций по счетам клиента
    :return:
    """
    with open(file, 'r', encoding="utf-8") as f:
        data = json.load(f)
        return data


def sort_by_date(file):
    """
    Возвращает сортированный список операции по дате от новых к старым
    :return:
    """
    lists = load_word(file)
    list_sort = sorted(lists, key=lambda item: dict(item).get('date', ' '), reverse=True)
    return list_sort


def get_latest_transactions(file):
    """
   Возвращает последние 5 выполненных (EXECUTED) операций
    :return:
    """
    list_operation = []
    for item in sort_by_date(file):
        if dict(item).get('state') == 'EXECUTED':
            list_operation.append(item)
    return list_operation[0:5]


def get_list_data_transactions(file):
    list_data = []
    for item in get_latest_transactions(file):
        date = datetime.strptime(dict(item).get('date'), '%Y-%m-%dT%H:%M:%S.%f')
        list_data.append(f"{date:%d.%m.%Y}")
    return list_data


def get_list_number_card(file):
    list_card = []
    for item in get_latest_transactions(file):
        if 'from' in item:
            open_number_card = ''.join(i if i.isdigit() else ' ' for i in dict(item).get('from')).split()
            encrypted_number_card = open_number_card[0][:6] + len(open_number_card[0][6:-4]) * "*" + open_number_card[
                                                                                                         0][-4:]
            len_number_card = len(encrypted_number_card)
            list_card.append(' '.join([encrypted_number_card[i:i + 4] for i in range(0, len_number_card, 4)]))
        else:
            list_card.append("Номер счета неизвестен")
    return list_card


def get_list_name_card(file):
    list_name_card = []
    for item in get_latest_transactions(file):
        list_name_card.append(''.join(
            i if i.isalpha() else ' ' for i in dict(item).get('from', 'Наименование неизвестно')).split())

    return list_name_card


def get_list_to_name_card(file):
    to_name_card = []
    for item in get_latest_transactions(file):
        to_name_card.append(''.join(i if i.isalpha() else ' ' for i in dict(item).get('to')).split())
    return to_name_card


def get_list_to_number_card(file):
    to_number_card = []
    for item in get_latest_transactions(file):
        to_open_number_card = ''.join(i if i.isdigit() else ' ' for i in dict(item).get('to')).split()
        to_number_card.append(len(to_open_number_card[0][-6:-4]) * '*' + to_open_number_card[0][-4:])
    return to_number_card


def get_list_sum_transactions(file):
    list_sum = []
    for item in get_latest_transactions(file):
        list_sum.append(item['operationAmount']['amount'])
    return list_sum


def get_list_name_currency(file):
    list_name_currency = []
    for item in get_latest_transactions(file):
        list_name_currency.append(item['operationAmount']['currency']['name'])
    return list_name_currency


def get_list_description(file):
    list_description = []
    for item in get_latest_transactions(file):
        list_description.append(item['description'])
    return list_description
