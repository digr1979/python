#########################################################################
#
# Author: Dmitry Gromov
# Date: 2021-06-08
# Description: task7 of homework8
#
#########################################################################

""" 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
    реализуйте перегрузку методов сложения и умножения комплексных чисел.
    Проверьте работу проекта,
    создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
    Проверьте корректность полученного результата.
"""

class Cnum():
    """ Класс 'Cnum - комплесное число'
        атрибуты:
            - __n - дейстыительная часть
            - __i - мнимая часть
        методы:
            - parse_date_str - парсит строку и возвращает список целых чисел
            - validate_date - проверяет строку на соответсвие шаблону 'dd-mm-yyyy'
    """

    def __init__(self, n, i):
        """ Конструктор."""
        self.__n = n
        self.__i = i

    def __str__(self):
        """Перегружаем представление"""
        return str(self.__n) + "+" + str(self.__i) + "i" if self.__i > 0 else str(self.__n) + str(self.__i) + "i"

    def __add__(self, other):
        """Перегружаем операцию сложения"""
        new_cnum = Cnum(0, 0)
        new_cnum.__n = self.__n + other.__n
        new_cnum.__i = self.__i + other.__i
        return new_cnum

    def __mul__(self, other):
        """Перегружаем операцию умножения"""
        new_cnum = Cnum(0, 0)
        # x1x2 + x1iy2 + iy1x2 + iy1iy2
        new_cnum.__n = self.__n * other.__n + (self.__i * other.__i * -1)
        new_cnum.__i = (self.__n * other.__i) + (self.__i * other.__n)
        return new_cnum


def main():
    """ проверяем."""
    cn1 = Cnum(2, -3)
    cn2 = Cnum(5, 4)

    print("Первое комплесное число:", cn1)
    print("Второе комплесное число:", cn2)

    print(f"Сложение комлексных чисел {cn1} и {cn2} = ", cn1 + cn2)
    print(f"Умножение комлексных чисел {cn1} и {cn2} = ", cn1 * cn2, '\n')

    # еще пример
    cn1 = Cnum(4, -1)
    cn2 = Cnum(6, 11)

    print("Первое комплесное число:", cn1)
    print("Второе комплесное число:", cn2)

    print(f"Сложение комлексных чисел {cn1} и {cn2} = ", cn1 + cn2)
    print(f"Умножение комлексных чисел {cn1} и {cn2} = ", cn1 * cn2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
