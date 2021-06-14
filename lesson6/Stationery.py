######################################################################
#
# Author: Dmitry Gromov
# Date: 2021-06-06
# Description: task5 of homework6
#
######################################################################


"""
    5. Реализовать класс Stationery (канцелярская принадлежность).
    Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
    Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
    В каждом из классов реализовать переопределение метода draw.
    Для каждого из классов методы должен выводить уникальное сообщение.
    Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    """ Класс Stationery (родительский), содержит:
         Атрибуты:
             - title
         Методы:
             - draw
         """

    def __init__(self):
        self.title = "Stationery - parent class"

    def draw(self):
        """Метод выводит сообщение \“Запуск отрисовки.\”
        """
        print("Запуск отрисовки.")

class Pen(Stationery):
    """ Класс Pen, производный от Stationery, переопределяет метод "draw" содержит:
         Атрибуты:
             - title
         Методы:
             - draw
         """

    def __init__(self):
        super().__init__()
        self.title = "Pen"

    def draw(self):
        """ Метод выводит сообщение \“Запуск отрисовки (Pen).\”

            Переопределяет метод базового класса
        """
        print("Запуск отрисовки (Pen).")


class Pencil(Stationery):
    """ Класс Pencil, производный от Stationery, переопределяет метод "draw" содержит:
         Атрибуты:
             - title
         Методы:
             - draw
         """

    def __init__(self):
        super().__init__()
        self.title = "Pencil"

    def draw(self):
        """ Метод выводит сообщение \“Запуск отрисовки (Pencil).\”

            Переопределяет метод базового класса
        """
        print("Запуск отрисовки (Pencil).")


class Handle(Stationery):
    """ Класс Handle, производный от Stationery, переопределяет метод "draw" содержит:
         Атрибуты:
             - title
         Методы:
             - draw
         """

    def __init__(self):
        super().__init__()
        self.title = "Handle"

    def draw(self):
        """ Метод выводит сообщение \“Запуск отрисовки (Handle).\”

            Переопределяет метод базового класса
        """
        print("Запуск отрисовки (Handle).")


def main():
    """ Создаем объекты всех классов и вызываем методы \'draw\' """

    # Сперва объект базового класса
    obj = Stationery()
    obj.draw()

    # Теперь объект класса Pen
    obj = Pen()
    obj.draw()

    # Теперь объект класса Pencil
    obj = Pencil()
    obj.draw()

    # Теперь объект класса Handle
    obj = Handle()
    obj.draw()


if __name__ == '__main__':
    main()