#########################################################################
#
# Author: Dmitry Gromov
# Date: 2021-06-14
# Description: task456 of homework8
#
#########################################################################


""" 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
    А также класс «Оргтехника», который будет базовым для классов-наследников.
    Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
    общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
    5. Продолжить работу над первым заданием. Разработать методы,
    отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
    Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
    можно использовать любую подходящую структуру, например словарь.
    6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
    Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
    Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
    изученных на уроках по ООП.
"""


import sys
from abc import ABC, abstractmethod


class NotNumError(Exception):
    """ Класс 'NotNumError' - проверка на цифры
        атрибуты:
        методы:
    """

    def __init__(self, text):
        self.text = text

    def __str__(self):
        return ("Пользовательское исключение: " + self.text)

class Storage:
    """ Класс Storage"""
    __units = []

    @classmethod
    def put_unit(cls, **kwargs):
        """ добавляет юнит на склад"""
        # for item in kwargs:
            # if item['unit_type'] == "printer":
            #     Storage.__units.append(Printer(item))
            # elif item['unit_type'] == "scanner":
            #     Storage.__units.append(Scanner(item))
            # elif item['unit_type'] == "xerox":
            #     Storage.__units.append(Xerox(item))
        if kwargs['unit_type'] == "printer":
            Storage.__units.append(Printer(**kwargs))
        elif kwargs['unit_type'] == "scanner":
            Storage.__units.append(Scanner(**kwargs))
        elif kwargs['unit_type'] == "xerox":
            Storage.__units.append(Xerox(**kwargs))


    @classmethod
    def pull_unit(cls, **kwargs):
        """ забирает юнит со склада"""
        pass

    @classmethod
    def list_units(cls):
        """ Печатаем текущее состояние списка товаров."""
        for unit in Storage.__units:
            unit.print_unit()


class Unit(ABC):
    """ Базовый класс"""
    # def __init__(self, unit_type, unit_model, unit_name, unit_qty):
    def __init__(self, **kwargs):
            unit_type = kwargs.get("unit_type")
            unit_model = kwargs.get("unit_model")
            unit_name = kwargs.get("unit_name")
            unit_qty = kwargs.get("unit_qty")
            # self.__unit_prop = {'unit_type': kwargs["unit_type"], 'unit_model': kwargs["unit_model"], 'unit_name': kwargs["unit_name"], 'unit_qty': kwargs["unit_qty"]}
            self.__unit_prop = {'unit_type': unit_type, 'unit_model': unit_model, 'unit_name': unit_name, 'unit_qty': unit_qty}

    def print_unit(self):
        for item in self.__unit_prop:
            print(item, "=", self.__unit_prop[item], " ", end="")

class Printer(Unit):
    """ Class Printer"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        printer_prop = kwargs.get('printer')
        try:
            if printer_prop is None:
                raise ValueError
            else:
                is_laser = printer_prop.get('is_laser')
                resolution = printer_prop.get('resolution')
                formats = printer_prop.get('formats')
                self.__printer_prop = {'is_laser': is_laser, 'resolution': resolution, 'formats': formats}
        except ValueError:
           print("Значение объекта класса \"Printer\", задано неверно")

    def print_unit(self):
        super().print_unit()
        for item in self.__printer_prop:
            print(item, "=", self.__printer_prop[item], " ", end="")
        print()


class Scanner(Unit):
    """ Class Scanner"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        scanner_prop = kwargs.get('scanner')
        try:
            if scanner_prop is None:
                raise ValueError
            else:
                duplex = scanner_prop.get('duplex')
                resolution = scanner_prop.get('resolution')
                self.__scanner_prop = {'duplex': duplex, 'resolution': resolution}
        except ValueError:
           print("Значение объекта класса \"Scanner\", задано неверно")

    def print_unit(self):
        super().print_unit()
        for item in self.__scanner_prop:
            print(item, "=", self.__scanner_prop[item], " ", end="")
        print()


class Xerox(Unit):
    """ Class Xerox"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        xerox_prop = kwargs.get('xerox')
        try:
            if xerox_prop is None:
                raise ValueError
            else:
                resolution = xerox_prop.get('resolution')
                speed = xerox_prop.get('speed')
                self.__xerox_prop = {'resolution': resolution, 'speed':speed}
        except ValueError:
           print("Значение объекта класса \"Xerox\", задано неверно")

    def print_unit(self):
        super().print_unit()
        for item in self.__xerox_prop:
            print(item, "=", self.__xerox_prop[item], end="")
        print()


def main():
    """ Проверяем

        Задача выполнена не в полном объеме, и сейча я бы её реализовывал иначе.
        К сожалению времени нет.
     """

    # Принтер 1
    kwargs1 = {"unit_type": "printer", "unit_model": "hp", "unit_name": "5025", "unit_qty": 3, "printer": {"is_laser": True}}
    # Принтер 2
    kwargs2 = {"unit_type": "printer", "unit_model": "hp", "unit_name": "3005", "unit_qty": 1,
            "printer": {"is_laser": True}, "formats": {"A3": True, "A4": True, "Letter": True}}
    # Сканнер
    kwargs3 = {"unit_type": "scanner", "unit_model": "hp", "unit_name": "1000", "unit_qty": 1,
            "scanner": {"duplex": False}, "resolution": 600}
    # Ксерокс
    kwargs4 = {"unit_type": "xerox", "unit_model": "xerox", "unit_name": "7500dn", "unit_qty": 2,
            "xerox": {"resolution": 1200}, "speed": 60}


    Storage.put_unit(**kwargs1)
    Storage.put_unit(**kwargs2)
    Storage.put_unit(**kwargs3)
    Storage.put_unit(**kwargs4)

    Storage.list_units()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
