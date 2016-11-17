import sys
import lib_view as view
import lib_model as model

DATA_ADDRESSES = [
    ['all_users1.json', 'all_books1.json', 'available_books1.json', 'users_with_books1.json'],
    ['all_users2.json', 'all_books2.json', 'available_books2.json', 'users_with_books2.json'],
    ['all_users3.json', 'all_books3.json', 'available_books3.json', 'users_with_books3.json']]


def get_source_number():
    correct_numbers = ['1', '2', '3']
    while True:
        number = view.input_source_type()
        if number in correct_numbers:
            return number
        else:
            view.print_wrong_source_number()


def load_all_datafiles(source_number, addresses):
    adr_num = int(source_number) - 1
    for address in addresses[adr_num]:
        data_piece = model.load_data(source_number, address)
        yield data_piece


def show_all_books(all_data):
    list_of_book_id = list(all_data[1].keys())
    list_of_book_id.sort(key=int)
    view.print_all_books(all_data[1], list_of_book_id)


def show_all_users(all_data):
    view.print_all_users(all_data[0])


def show_users_with_books(all_data):
    view.print_users_with_books(all_data[3], all_data[0])


def show_users_with_overdue_books(all_data):
    users_with_overdue_books = model.get_users_with_overdue_books(all_data[3])
    view.print_users_with_overdue_books(users_with_overdue_books, all_data[0])


def show_available_books(all_data):
    all_data[2].sort(key=int)
    view.print_available_books(all_data[1], all_data[2])


def give_a_book(all_data):
    user_id = view.input_user_id()
    if not model.is_user_in_list(user_id, all_data[0]):
        view.print_no_such_user()
        return
    if model.has_user_enough_books(user_id, all_data[3]):
        view.print_no_more_books(model.NUMBER_OF_BOOKS_FOR_USER)
        return
    if model.has_user_overdue_books(user_id, all_data[3]):
        view.print_has_overdue_book()
        return
    book_id = view.input_book_id()
    if not model.is_book_in_library(book_id, all_data[1]):
        view.print_no_such_book()
        return
    if not model.is_book_available(book_id, all_data[2]):
        view.print_book_is_unavailable()
        return
    model.give_book(user_id, book_id, all_data[2], all_data[3])
    view.print_record_was_done()


def receive_a_book(all_data):
    user_id = view.input_user_id()
    if not model.is_user_in_list(user_id, all_data[0]):
        view.print_no_such_user()
        return
    if not model.has_user_a_book(user_id, all_data[3]):
        view.print_user_has_no_books()
        return
    book_id = view.input_book_id()
    if not model.is_book_in_library(book_id, all_data[1]):
        view.print_no_such_book()
        return
    if not model.has_user_particular_book(user_id, book_id, all_data[3]):
        view.print_user_has_not_this_books()
        return
    model.receive_book(user_id, book_id, all_data[2], all_data[3])
    view.print_record_was_done()
    pass


def exit_program(all_data):
    model.write_changed_data(all_data, source_number, DATA_ADDRESSES)
    sys.exit()


if __name__ == '__main__':
    source_number = get_source_number()
    all_data = []
    for data in load_all_datafiles(source_number, DATA_ADDRESSES):
        all_data.append(data)
    print(all_data[2])
    action_dict = {'1': show_all_users,
                   '2': show_all_books,
                   '3': show_users_with_books,
                   '4': show_users_with_overdue_books,
                   '5': show_available_books,
                   '6': give_a_book,
                   '7': receive_a_book,
                   '8': exit_program}
    while True:
        view.print_menu()
        choise = view.input_option_number()
        if choise in action_dict:
            action_dict[choise](all_data)
            view.print_press_enter()
            input()
        else:
            view.print_wrong_option_number()
            view.print_press_enter()
            input()
