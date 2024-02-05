import utils as u
file = '../operations.json'
load = u.get_latest_transactions(file)


def main():
    number = 0
    while number != 5:
        print(
            f"{u.get_list_data_transactions(file)[number]} {u.get_list_description(file)[number]}\n"
            f"{' '.join(u.get_list_name_card(file)[number])} {u.get_list_number_card(file)[number]} > "
            f"{' '.join(u.get_list_to_name_card(file)[number])} {u.get_list_to_number_card(file)[number]}\n"
            f"{u.get_list_sum_transactions(file)[number]} {u.get_list_name_currency(file)[number]}\n")
        number += 1


if __name__ == '__main__':
    main()
