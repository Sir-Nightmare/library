import json
from datetime import datetime, timedelta

NUMBER_OF_BOOKS_FOR_USER = 3
DAYS_TO_RETURN_BOOK = 30


def load_data_from_source1(file_path):
    with open(file_path, 'r') as input_file:
        if input_file:
            return json.load(input_file)


def load_data_from_source2(file_path):
    with open(file_path, 'r') as input_file:
        if input_file:
            return json.load(input_file)


def load_data_from_source3(file_path):
    with open(file_path, 'r') as input_file:
        if input_file:
            return json.load(input_file)


def write_data_to_source1(data_to_write, file_path):
    with open(file_path, 'w') as file_to_write:
        json.dump(data_to_write, file_to_write, indent=4, sort_keys=True, ensure_ascii=False)


def write_data_to_source2(data_to_write, file_path):
    with open(file_path, 'w') as file_to_write:
        json.dump(data_to_write, file_to_write, indent=4, sort_keys=True, ensure_ascii=False)


def write_data_to_source3(data_to_write, file_path):
    with open(file_path, 'w') as file_to_write:
        json.dump(data_to_write, file_to_write, indent=4, sort_keys=True, ensure_ascii=False)

'''
All functions for loading and writing data are equal now.
But each of them can be changed inside (loading from url, another file type etc.)
and interface will not change.
Only DATA_ADDRESSES in lib_controller.py will have to be changed.
'''
def load_data(source_number, address):
    load_types = {'1': load_data_from_source1,
                  '2': load_data_from_source2,
                  '3': load_data_from_source3}
    return load_types[source_number](address)


def write_changed_data(all_data, source_number, addresses):
    write_types = {'1': write_data_to_source1,
                   '2': write_data_to_source2,
                   '3': write_data_to_source3}
    all_data[2].sort(key=int)
    write_types[source_number](all_data[2], addresses[int(source_number) - 1][2])
    write_types[source_number](all_data[3], addresses[int(source_number) - 1][3])


def is_user_in_list(user_id, all_users):
    if user_id in all_users:
        return True


def has_user_a_book(user_id, users_with_books):
    if user_id in users_with_books:
        return True


def has_user_particular_book(user_id, book_id, users_with_books):
    if book_id in users_with_books[user_id]:
        return True


def has_user_enough_books(user_id, users_with_books):
    if user_id in users_with_books:
        if len(users_with_books[user_id]) >= NUMBER_OF_BOOKS_FOR_USER:
            return True


def has_user_overdue_books(user_id, users_with_books):
    if user_id in users_with_books:
        for date_str in users_with_books[user_id].values():
            date_of_book_return = datetime.strptime(date_str, '%Y-%m-%d').date()
            if date_of_book_return <= datetime.today().date():
                return True


def get_users_with_overdue_books(users_with_books):
    users_with_overdue_books = []
    for user_id in users_with_books.keys():
        if has_user_overdue_books(user_id, users_with_books):
            users_with_overdue_books.append(user_id)
    users_with_overdue_books.sort()
    return users_with_overdue_books


def is_book_in_library(book_id, all_books):
    if book_id in all_books:
        return True


def is_book_available(book_id, available_books):
    if book_id in available_books:
        return True


def give_book(user_id, book_id, available_books, users_with_books):
    date_to_return = str(datetime.today().date() + timedelta(days=DAYS_TO_RETURN_BOOK))
    if user_id in users_with_books:
        users_with_books[user_id][book_id] = date_to_return
    else:
        users_with_books[user_id] = {}
        users_with_books[user_id][book_id] = date_to_return
    available_books.remove(book_id)


def receive_book(user_id, book_id, available_books, users_with_books):
    users_with_books[user_id].pop(book_id)
    available_books.append(book_id)
    if len(users_with_books[user_id]) == 0:
        users_with_books.pop(user_id)
