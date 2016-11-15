import sys
import lib_view as view
import lib_model as model


def show_all_books():
    list_of_book_id = list(model.all_books.keys())
    list_of_book_id.sort(key=int)
    view.print_all_books(model.all_books, list_of_book_id)


def show_all_users():
    view.print_all_users(model.all_users)


def show_users_with_books():
    view.print_users_with_books(model.users_with_books, model.all_users)


def show_users_with_overdue_books():
    users_with_overdue_books = model.get_users_with_overdue_books()
    view.print_users_with_overdue_books(users_with_overdue_books, model.all_users)


def show_available_books():
    model.available_books.sort(key=int)
    view.print_available_books(model.all_books, model.available_books)


def give_a_book():
    user_id = view.input_user_id()
    if not model.is_user_in_list(user_id):
        view.print_no_such_user()
        return
    if model.has_user_enough_books(user_id):
        view.print_no_more_books(model.NUMBER_OF_BOOKS_FOR_USER)
        return
    if model.has_user_overdue_books(user_id):
        view.print_has_overdue_book()
        return
    book_id = view.input_book_id()
    if not model.is_book_in_library(book_id):
        view.print_no_such_book()
        return
    if not model.is_book_available(book_id):
        view.print_book_is_unavailable()
        return
    model.give_book(user_id, book_id)
    view.print_record_was_done()


def receive_a_book():
    user_id = view.input_user_id()
    if not model.is_user_in_list(user_id):
        view.print_no_such_user()
        return
    if not model.has_user_a_book(user_id):
        view.print_user_has_no_books()
        return
    book_id = view.input_book_id()
    if not model.is_book_in_library(book_id):
        view.print_no_such_book()
        return
    if not model.has_user_particular_book(user_id, book_id):
        view.print_user_has_not_this_books()
        return
    model.receive_book(user_id, book_id)
    view.print_record_was_done()
    pass


def exit_program():
    model.write_changed_data()
    sys.exit()


if __name__ == '__main__':
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
        choise = input()
        if choise in action_dict:
            action_dict[choise]()
            view.print_press_enter()
            input()
        else:
            view.print_wrong_number()
            view.print_press_enter()
            input()
