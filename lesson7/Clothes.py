###########################################################
#
# Author: Dmitry Gromov
# Date: 2021-06-07
# Description: task2 of homework7
#
###########################################################

""" 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
    Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
    К типам одежды в этом проекте относятся пальто и костюм.
    У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
    Это могут быть обычные числа: V и H, соответственно.
    Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
    для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
    Реализовать общий подсчет расхода ткани.
    Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
    проверить на практике работу декоратора @property.
"""


from abc import ABC, abstractmethod


class Clothes(ABC):
    """ Класс 'Clothes' родительский, абстрактный класс
        атрибуты:
            - v - размер,
            - h - рост
        методы:
            - get_material_consumption - интерфейс
    """

    def __init__(self, **kwargs):
        """ Если есть v или h, то инициализируем
        """
        self.v = kwargs.get('v')
        self.h = kwargs.get('h')

    @abstractmethod
    def get_material_consumption(self):
        pass


class Coat(Clothes):
    """ Класс 'Coat' производный от 'Clothes'
        атрибуты:
            - v - размер,
            - h - рост  (не используется)
        методы:
            - get_material_consumption - интерфейс
    """

    @property
    def get_material_consumption(self):
        """ Возвращает расход материала растчитанный по формуле (V/6.5 + 0.5) """
        return ((self.v / 6.5) + 0.5)



class Suit(Clothes):
    """ Класс 'Suit' производный от 'Clothes'
        атрибуты:
            - v - размер (не используется),
            - h - рост
        методы:
            - get_material_consumption - интерфейс
    """

    @property
    def get_material_consumption(self):
        """ Возвращает расход материала растчитанный по формуле (2 * H + 0.3) """
        return ((2 * self.h) + 0.3)




def main():
    """ Создаем объекты классов Coat и Trousers
    """

    # Создаем объект "Пальто" и выводи расход материала
    c = Coat(v = 46)
    material_consumption = c.get_material_consumption
    print(f"Расчитанный расход материала на пальто: {material_consumption:.2f}")

    # Создаем объект "Костюм" и выводи расход материала
    s = Suit(h = 180)
    material_consumption = s.get_material_consumption
    # Что-то много получилось...
    print(f"Расчитанный расход материала на костюм: {material_consumption:.2f}")

if __name__ == "__main__":
    main()

