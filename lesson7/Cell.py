###########################################################
#
# Author: Dmitry Gromov
# Date: 2021-06-07
# Description: task3 of homework7
#
###########################################################

""" 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
    В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
    В классе должны быть реализованы методы перегрузки арифметических операторов:
        сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
    Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
    умножение и обычное (не целочисленное) деление клеток, соответственно.
    В методе деления должно осуществляться округление значения до целого числа.
    Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
    Вычитание. Участвуют две клетки.
        Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
    Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
    Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
    В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
    Данный метод позволяет организовать ячейки по рядам. Метод должен возвращать строку вида *****\n*****\n*****...,
    где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает,
    то в последний ряд записываются все оставшиеся.
    Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
    Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
    Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""


class Cell():
    """ Класс 'Cell' родительский, абстрактный класс
        атрибуты:
            - __size - размер клетки (количество ячеек, целое число)
        методы:
            - get_size -
            - set_size - немного инкапсуляции ...
            - make_order - Метод должен возвращать строку вида *****\n*****\n*****...
    """

    def __init__(self, size):
        """ Если есть v или h, то инициализируем
        """
        self.__size = size

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

    def __add__(self, other):
        """ Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток."""
        return Cell(self.__size + other.__size)

    def __sub__(self, other):
        """ Вычитание. Участвуют две клетки.
            Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
            иначе выводить соответствующее сообщение.
        """
        diff = (self.__size - other.__size)
        if (diff > 0):
            return Cell(self.__size - other.__size)
        else:
            print("Разность количества ячеек двух клеток должна быть больше нуля")
            return None

    def __mul__(self, other):
        """ Умножение. Создается общая клетка из двух.
            Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
        """
        return Cell(self.__size * other.__size)

    def __truediv__(self, other):
        """ Деление. Создается общая клетка из двух.
            Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
        """
        # Если я правильно понял задачу, то:
        return Cell(self.__size // other.__size)

    def __print_cell_row(self, ordered_str, rest_items, items_in_row):
        """ Служебный метод

            Используется как рекурсия для вызова из метода make_order
        """

        if rest_items > items_in_row:
            ordered_str = ordered_str + ('*' * items_in_row)
        else:
            ordered_str = ordered_str + ('*' * rest_items)
            return ordered_str + "." # точку, на всякий случай...
        ordered_str += "\n"
        return self.__print_cell_row(ordered_str, (rest_items - items_in_row), items_in_row)

    def make_order(self, items_in_row):
        """ Метод должен возвращать строку вида *****\n*****\n*****...,
            где количество ячеек между \n равно переданному аргументу
        """
        ordered_str = ""
        return self.__print_cell_row(ordered_str, self.__size, items_in_row)


def main():
    """ Создаем объекты Cells
    """

    cell_15 = Cell(15)
    cell_10 = Cell(10)
    cell_8 = Cell(8)
    cell_18 = Cell(18)
    cell_2 = Cell(2)

    # Выводим то что имеем с разным ордером
    print(f"cell_15 of {cell_15.get_size()} is ordered by 3:")
    print(cell_15.make_order(3), '\n')
    print(f"cell_10 of {cell_10.get_size()} is ordered by 4:")
    print(cell_10.make_order(4), '\n')
    print(f"cell_8 of {cell_8.get_size()} is ordered by 3:")
    print(cell_8.make_order(3), '\n')
    print(f"cell_18 of {cell_18.get_size()} is ordered by 5:")
    print(cell_18.make_order(5), '\n')
    print(f"cell_2 of {cell_2.get_size()} is ordered by 2:")
    print(cell_2.make_order(2), '\n')

    # Сложение
    cell_15_add_cell_8 = cell_15 + cell_8
    print(f"cell_1_add_3 as sum of cell_1 and cell_8 of {cell_15_add_cell_8.get_size()} is ordered by 8:")
    print(cell_15_add_cell_8.make_order(8), '\n')

    # Вычитание
    cell_15_sub_cell_10 = cell_15 - cell_10
    print(f"cell_15_sub_cell_10 as sub of cell_15 - cell_10 of {cell_15_sub_cell_10.get_size()} is ordered by 5:")
    print(cell_15_sub_cell_10.make_order(5), '\n')

    # Умножение
    cell_2_mul_cell_8 = cell_2 * cell_8
    print(f"cell_2_mul_cell_8 as sub of cell_2 * cell_8 of {cell_2_mul_cell_8.get_size()} is ordered by 6:")
    print(cell_2_mul_cell_8.make_order(6), '\n')

    # Деление
    cell_10_truediv_cell_2 = cell_10 / cell_2
    print(f"cell_10_truediv_cell_2 as sub of cell_10 / cell_2 of {cell_10_truediv_cell_2.get_size()} is ordered by 5:")
    print(cell_10_truediv_cell_2.make_order(5), '\n')


if __name__ == "__main__":
    main()

