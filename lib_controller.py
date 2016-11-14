import sys
import lib_view as view
import lib_model as model


def show_all_books():
    view.print_all_books(all_books)


def show_all_users():
    view.print_all_users(all_users)


def show_users_with_books():
    pass


def show_users_with_overdue_books():
    pass


def show_availiable_books():
    pass


def give_a_book():
    pass


def receive_a_book():
    pass


all_users = model.load_data_from_json('all_users.json')
all_books = model.load_data_from_json('all_books.json')

action_dict = {'1': show_all_users,
               '2': show_all_books,
               '3': show_users_with_books,
               '4': show_users_with_overdue_books,
               '5': show_availiable_books,
               '6': give_a_book,
               '7': receive_a_book,
               '8': sys.exit}
while True:
    view.print_menu()
    choise = input()
    if choise in action_dict:
        action_dict[choise]()
        view.print_press_enter()
        input()
    else:
        view.print_wrong_number()
        view.print_press_enter()
        input()
