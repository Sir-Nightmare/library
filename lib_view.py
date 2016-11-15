def print_menu():
    print('Options:\n\r',
          '1. Show list of all users\n\r',
          '2. Show list of all books\n\r',
          '3. Show list of users with books\n\r',
          '4. Show list of users with overdue books\n\r',
          '5. Show list of available books\n\r',
          '6. Give user a book\n\r',
          '7. Receive a book from a user\n\r',
          '8. Quit\n\r')


def print_no_more_books(number):
    print('User already has {} books'.format(number))


def print_has_overdue_book():
    print('User has overdue books')


def print_no_such_user():
    print('There is no user with this id')


def print_book_is_unavailable():
    print('This book is unavailable now')


def print_no_such_book():
    print('There is no book with this id')


def print_list_of_books(dict_to_print, list_of_book_id):
    print('{0:>3}{3}{1:35}{3}{2:25}{3}'.format('ID', 'Book name', 'Auhor', ' | '))
    print('-' * 71)
    for book_id in list_of_book_id:
        print('{0:>3}{3}{1:35}{3}{2:25}{3}'.format(book_id, dict_to_print[book_id]['book_name'],
                                                   dict_to_print[book_id]['author_name'], ' | '))


def print_all_books(dict_to_print, list_of_book_id):
    print('\n\rList of all books:')
    print_list_of_books(dict_to_print, list_of_book_id)


def print_available_books(dict_to_print, list_of_book_id):
    print('\n\rList of available books:')
    print_list_of_books(dict_to_print, list_of_book_id)


def print_all_users(dict_to_print):
    list_of_user_id = list(dict_to_print.keys())
    list_of_user_id.sort(key=int)
    print('\n\rList of all users:')
    print('{0:>3}{3}{1:15}{3}{2:15}{3}'.format('ID', 'First name', 'Last name', ' | '))
    print('-' * 41)
    for user_id in list_of_user_id:
        print('{0:>3}{3}{1:15}{3}{2:15}{3}'.format(user_id, dict_to_print[user_id]['first_name'],
                                                   dict_to_print[user_id]['last_name'], ' | '))


def print_users_with_books(users_with_books, all_users):
    list_of_user_id = list(users_with_books.keys())
    list_of_user_id.sort(key=int)
    print('\n\rList of users with book:')
    print('{0:>3}{4}{1:15}{4}{2:15}{4}{3:5}{4}'.format('ID', 'First name', 'Last name', 'Books',
                                                       ' | '))
    print('-' * 48)
    for user_id in list_of_user_id:
        print(
            '{0:>3}{4}{1:15}{4}{2:15}{4}{3:^5}{4}'.format(user_id, all_users[user_id]['first_name'],
                                                         all_users[user_id]['last_name'],
                                                         len(users_with_books[user_id]), ' | '))


def print_users_with_overdue_books(list_of_user_id, all_users):
    list_of_user_id.sort(key=int)
    print('\n\rList of users with overdue books:')
    print('{0:>3}{3}{1:15}{3}{2:15}{3}'.format('ID', 'First name', 'Last name', ' | '))
    print('-' * 41)
    for user_id in list_of_user_id:
        print('{0:>3}{3}{1:15}{3}{2:15}{3}'.format(user_id, all_users[user_id]['first_name'],
                                                   all_users[user_id]['last_name'], ' | '))

def print_press_enter():
    print('\n\rpress Enter to show options')


def print_wrong_number():
    print('There is no such number. Please input a number from 1 to 8')


def print_record_was_done():
    print('Information was recorded successfully')

def print_user_has_no_books():
    print('This user has no books')

def print_user_has_not_this_books():
    print('User do not have this book')


def input_user_id():
    return input('Input user ID:\n\r')


def input_book_id():
    return input('Input book ID:\n\r')


def input_option_number():
    return input('Input option number [1-8]:\n\r')
