import json

NUMBER_OF_BOOKS_FOR_USER = 3
ALL_USERS_FILE_PATH = 'all_users.json'
ALL_BOOKS_FILE_PATH = 'all_books.json'
AVAILABLE_BOOKS_FILE_PATH = 'available_books.json'
USERS_WITH_BOOKS_FILE_PATH = 'users_with_books.json'


def load_data_from_json(file_path):
    with open(file_path, 'r') as input_file:
        if input_file:
            return json.load(input_file)


def write_data_to_json(data_to_write, file_path):
    with open(file_path, 'w') as file_to_write:
        json.dump(data_to_write, file_to_write, indent=4, sort_keys=True, ensure_ascii=False)


def write_changed_data():
    available_books.sort(key=int)
    write_data_to_json(available_books, AVAILABLE_BOOKS_FILE_PATH)
    write_data_to_json(users_with_books, USERS_WITH_BOOKS_FILE_PATH)


def is_user_in_list(user_id):
    if user_id in all_users:
        return True
    return False


def has_user_enough_books(user_id):
    if user_id in users_with_books:
        if len(users_with_books[user_id]) == NUMBER_OF_BOOKS_FOR_USER:
            return True


def has_user_overdue_books(user_id):
    # TODO: make everything with dates
    return False


def is_book_in_library(book_id):
    if book_id in all_books:
        return True


def is_book_available(book_id):
    if book_id in available_books:
        return True


def give_book(user_id, book_id):
    pass
    # TODO: make


def receive_book(user_id, book_id):
    pass
    # TODO: make


all_users = load_data_from_json(ALL_USERS_FILE_PATH)
all_books = load_data_from_json(ALL_BOOKS_FILE_PATH)
available_books = load_data_from_json(AVAILABLE_BOOKS_FILE_PATH)
users_with_books = load_data_from_json(USERS_WITH_BOOKS_FILE_PATH)
