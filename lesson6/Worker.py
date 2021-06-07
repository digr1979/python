######################################################################
#
# Author: Dmitry Gromov
# Date: 2021-06-04
# Description: task3 of homework6
#
######################################################################


"""
    3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
        name, surname, position (должность), income (доход).
        Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
        например, {"wage": wage, "bonus": bonus}.
        Создать класс Position (должность) на базе класса Worker.
        В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
        Проверить работу примера на реальных данных (создать экземпляры класса Position,
        передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    """ Класс Worker, содержит:
        Атрибуты:
            - name
            - surname
            - position
            - income dict {"wage": wage, "bonus": bonus}
        Методы:
            - ..
        """

    # Определяем конструктор
    # def __init__(self, name, surname, position, **income):
    def __init__(self, *args, **kwargs):

        self.name = args[1]
        self.surname = args[2]
        self.position = args[3]
        self._income = kwargs


class Position(Worker):
    """ Класс Position, содержит:
        Методы:
            - get_full_name - возвращает полное имя
            - get_total_income - возвращает доход с учетом премии
        """

    # Определяем конструктор
    def __init__(self, *args, **kwargs):

        # Вызываем конструктор родительского класса
        super().__init__(self, *args, **kwargs)

    def get_full_name(self):
        return (self.position + " " + self.name + " " + self.surname)

    def get_total_income(self):
        try:
            return (int(self._income['wage']) + int(self._income['bonus']))
        except:
            print("Что-то пошло не так...")
            return None


def main():
    # Создаем объект класса и выводим данные
    p = Position("John", "Smith", "CEO", wage = 1000000, bonus = 250000)
    print("Должность и полное имя:", p.get_full_name())
    print("Оклад вместе с премией:", p.get_total_income())


if __name__ == '__main__':
    main()