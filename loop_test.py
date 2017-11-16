pipdef start():
    login = 'Valera'
    password = 'qwerty'

    is_check = True

    while is_check:
        input_login = input('Your log: ')
        input_password = input('Your pass: ')
        if login == input_login and password == input_password:
            print('Welcome')
            is_check = False
        else:
            print('Wrong input data')


if __name__ == '__main__':
    start()

# def fun():
#     pass
#
#
# class SuperClass:
#
#     def is_check(self):
#         pass
#
#
# name = 'Valera'
#
# temp = list()
# for index, letter_ in enumerate(name):
#     temp.append(letter_)
#     print(index + 1, '-->', ''.join(temp))