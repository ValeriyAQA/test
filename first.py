# -*- coding: UTF-8 -*-
from random import Random
import csv
import datetime


login = 'python'
password = 'qwerty'

is_check = True

# while is_check:
#     input_login = input('Your log: ')
#     input_password = input('Your pass: ')
#     if login == input_login and password == input_password:
#         print('Welcome')
#         is_check = False
#     else:
#         print('Wrong input data')

#
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


class Game21:
    """
    Простая игра в 21
    """
    _user_points = 0
    _comp_points = 0
    _flag = True

    def __init__(self, name='Маруська', win=21):
        self.username = name
        self._win = win

    def __str__(self):
        return 'Простая игра в {} c участником {}'.format(self._win, self.username)

    def say_hello(self):
        """
        Приветствие
        :return: Void
        """
        print('+'*70)
        print(' ')
        print('------- Привет, {} -------'.format(self.username))
        print(' ')

    @staticmethod
    def get_number():
        """
        Генерация случайного числа
        :return: int
        """
        number = Random()
        return number.randrange(1, 12)

    @staticmethod
    def _save_result(log):
        """
        Сохраняет результаты игры в файл
        :param log: list
        :return: void
        """
        with open('results.csv', 'a', encoding='UTF-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(i for i in log)

    def _get_result(self):
        """
        Проверка результата
        :return: void
        """
        print('')
        time = datetime.datetime.now()
        if self._comp_points < self._user_points <= self._win:
            print('Выиграл {}({}). У соперника {} баллов'.format(self.username, self._user_points, self._comp_points))
            log = [self.username, self._user_points, self._comp_points, time]
        elif self._comp_points < self._user_points > self._win:
            print('Проиграл {}({}). У соперника {} баллов'.format(self.username, self._user_points, self._comp_points))
            log = ['comp', self._comp_points, self._user_points, time]
        elif self._user_points < self._comp_points <= self._win:
            print('Проиграл {}({}). У соперника {} баллов'.format(self.username, self._user_points, self._comp_points))
            log = ['comp', self._comp_points, self._user_points, time]
        elif self._user_points < self._comp_points > self._win:
            print('Выиграл {}({}). У соперника {} баллов'.format(self.username, self._user_points, self._comp_points))
            log = [self.username, self._user_points, self._comp_points, time]
        elif self._user_points > self._win and self._comp_points > self._win:
            print('Проиграли оба (по {} баллов)'.format(self._user_points))
            log = ['Проиграли оба', self._user_points, self._comp_points, time]
        else:
            print('Ничья. У обоих по {} баллов'.format(self._user_points))
            log = ['Ничья', self._user_points, self._comp_points, time]

        self._save_result(log)

        print(' ')
        print('-'*20, ' >>> NEW GAME <<<', '-'*20, '\n')
        self._comp_points = 0
        self._user_points = 0
        self._flag = True

    def _check_points(self):
        """
        Проверяет что бы количество баллов не превысило максимальнодопустимое значение
        :return: bool
        """
        if self._user_points > self._win or self._comp_points > self._win:
            self._get_result()
        return False

    def _main_user_process(self):
        """
        Главный игровой процесс
        :return:void
        """
        while self._flag:
            self._check_points()

            print('\n', '-' * 10, 'У Вас сейчас {} баллов'.format(self._user_points), '-' * 10)
            answer = input('Нажми 1 для раздачи\nНажми 2 если хватит\nНажми 3 для выхода из игры ')
            if answer == '1':
                self._user_points += self.get_number()
                self._comp_points += self.get_number()
            elif answer == '2':
                self._flag = False
                self._get_result()
            elif answer == '3':
                exit('Вы вышли из игры')
            else:
                print('Допустимые значения только 1 и 2')
                continue

    def start(self):
        """
        Метод для запуска игры
        :return: void
        """
        self.say_hello()
        self._main_user_process()


if __name__ == '__main__':
    username = input('Как вас зовут: ')
    while True:
        game = Game21(username)
        game.start()
