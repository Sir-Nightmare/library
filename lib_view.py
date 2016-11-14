def print_menu():
    print('Options:\n\r',
          '1. Show list of all books\n\r',
          '2. Show list of all users\n\r',
          '3. Show list of users with books\n\r',
          '4. Show list of users with overdue books\n\r',
          '5. Show list of available books\n\r',
          '6. Give user a book\n\r',
          '7. Receive a book from a user\n\r',
          '8. Quit\n\r',
          'Input option number [1-8]:')


def print_no_more_books(number):
    print('User already has {} books'.format(number))


def print_has_overdue_book():
    print('User has overdue books')


def print_all_books(dict_to_print):
    list_of_book_id = list(dict_to_print.keys())
    list_of_book_id.sort(key=int)
    print('\n\rList of all books:')
    print('{0:>3}{3}{1:35}{3}{2:25}{3}'.format('ID', 'Book name', 'Auhor', ' | '))
    print('-' * 71)
    for book_id in list_of_book_id:
        print('{0:>3}{3}{1:35}{3}{2:25}{3}'.format(book_id, dict_to_print[book_id]['book_name'],
                                                   dict_to_print[book_id]['author_name'], ' | '))


def print_all_users(dict_to_print):
    list_of_user_id = list(dict_to_print.keys())
    list_of_user_id.sort(key=int)
    print('\n\rList of all users:')
    print('{0:>3}{3}{1:15}{3}{2:15}{3}'.format('ID', 'First name', 'Last name', ' | '))
    print('-' * 41)
    for user_id in list_of_user_id:
        print('{0:>3}{3}{1:15}{3}{2:15}{3}'.format(user_id, dict_to_print[user_id]['first_name'],
                                                   dict_to_print[user_id]['last_name'], ' | '))


def print_press_enter():
    print('\n\rpress Enter to show options')


def print_wrong_number():
    print('There is no such number. Please input a number from 1 to 8')
