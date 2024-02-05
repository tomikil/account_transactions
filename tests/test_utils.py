from src import utils as u

file = './operations.json'
load = u.load_word(file)
sort_date = u.sort_by_date(file)


def test_load_word():
    assert u.load_word(file)[0]['id'] == 441945886
    assert u.load_word(file)[56]['id'] == 560813069


def test_sort_by_date():
    assert u.sort_by_date(file)[0]['date'] == '2019-12-08T22:46:21.935582'
    assert u.sort_by_date(file)[45]['date'] == '2019-02-08T09:09:35.038506'


def test_get_list_latest_transactions():
    assert u.get_latest_transactions(file)[0]['id'] == 863064926
    assert u.get_latest_transactions(file)[3]['id'] == 482520625


def test_get_list_data_transactions():
    assert u.get_list_data_transactions(file)[0] == '08.12.2019'
    assert u.get_list_data_transactions(file)[2] == '19.11.2019'


def test_get_list_number_card():
    assert u.get_list_number_card(file)[1] == '2842 87** **** 9012'
    assert u.get_list_number_card(file)[0] == 'Номер счета неизвестен'


def test_list_get_name_card():
    assert u.get_list_name_card(file)[1] == ['Visa', 'Classic']
    assert u.get_list_name_card(file)[4] == ['Наименование', 'неизвестно']


def test_get_list_to_name_card():
    assert u.get_list_to_name_card(file)[0] == ['Счет']


def test_to_list_number_card():
    assert u.get_list_to_number_card(file)[0] == '**5907'
    assert u.get_list_to_number_card(file)[4] == '**8381'


def test_get_list_sum_transactions():
    assert u.get_list_sum_transactions(file)[0] == '41096.24'
    assert u.get_list_sum_transactions(file)[3] == '62814.53'


def test_get_list_name_currency():
    assert u.get_list_name_currency(file)[0] == 'USD'
    assert u.get_list_name_currency(file)[3] == 'руб.'


def test_get_list_description():
    assert u.get_list_description(file)[2] == 'Перевод организации'
    assert u.get_list_description(file)[0] == 'Открытие вклада'
