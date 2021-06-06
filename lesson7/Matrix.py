###########################################################
#
# Author: Dmitry Gromov
# Date: 2021-06-06
# Description: task1 of homework7
#
###########################################################


class Matrix():
    """ Класс 'Matrix' реализует простую матрицу
        атрибуты:
            - list_arr - список списков
        методы:
    """

    def __init__(self, list_arr):
        """ В качестве параметра, конструктор принимает список списков
        """
        self.list_arr = list_arr

    def __str__(self):
        text_row = "Matrix is:" + "\n"
        for row in self.list_arr:
            for item in row:
                text_row = text_row + str(item) + "\t"
            text_row += "\n"
        return text_row

    def __add__(self, right):
        """ Сложение двух матриц одного размера"""
        new_matrix = []
        new_row = []
        try:
            for row_left, row_right in zip(self.list_arr, right.list_arr):
                for item_left, item_right in zip(row_left, row_right):
                    new_item = item_left + item_right
                    new_row.append(new_item)
                # new_matrix.append(new_row)
                # new_row.clear()
                new_matrix.append(list(new_row))
                new_row.clear()
        except Exception as e:
            print(e)

        return Matrix(new_matrix)


def main():
    """ Создаем и складываем два объекта 'Matrix'
    """
    # первая матрица
    ma = Matrix([[1, 2, 3], [3, 6, 9]])
    print(ma)

    # вторая матрица
    mb = Matrix([[5, 4, -3], [10, 5, 0]])
    print(mb)

    # Проверяем результат
    mr = ma + mb
    print(mr)

    # Проверяем тип полученного объекта
    print("Тип объекта 'mr': ", type(mr))


if __name__ == "__main__":
    main()

