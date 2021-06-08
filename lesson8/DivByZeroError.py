#########################################################################
#
# Author: Dmitry Gromov
# Date: 2021-06-08
# Description: task2 of homework8
#
#########################################################################


""" 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
    Проверьте его работу на данных, вводимых пользователем.
    При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


import sys


class DivByZeroError(Exception):
    """ Класс 'DivByZeroError' - обработка деления на нуль
        атрибуты:
        методы:
    """

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return ("Пользовательское исключение: " + self.text)


def main():
    """ Проверяем

        Ctrl+C - выход из программы
     """

    print("Ctrl+C - выход из программы")

    while True:
        try:
            num1 = int(input("Укажите делимое:"))
            num2 = int(input("Укажите делитель:"))

            if num2 == 0:
                raise DivByZeroError("Деление на нуль!!!")
            else:
                print(num1 / num2)
        except DivByZeroError as e:
            print(e)
        except ValueError as e:
            print("Завершение работы")
            sys.exit(0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
