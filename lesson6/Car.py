######################################################################
#
# Author: Dmitry Gromov
# Date: 2021-06-04
# Description: task4 of homework6
#
######################################################################


"""
    4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
        А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
        Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
        Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
        Для классов TownCar и WorkCar переопределите метод show_speed.
        При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
        Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
        Выполните вызов методов и также покажите результат.
"""


class Car:
    """ Класс Car (родительский), содержит:
        Атрибуты:
            - speed,
            - color,
            - name,
            - is_police
        Методы:
            - go,
            - stop,
            - turn(direction)
            - show_speed - отображает текущую скорость
        """

    # Определяем конструктор
    # def __init__(self, speed, color, name, is_police):
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = str(color)
        self.name = str(name) # Хотя вроде тут всё строка.
        self.is_police = bool(is_police)
        print(f"Поехали. Скорость автомобиля {self.name} (полиция={self.is_police}) составляет {self.speed}км\ч")

    def go(self):
        self.speed += 20
        print("Машина '", self.name, "' поехала (+20км/ч)")

    def stop(self):
        self.speed = 0
        print("Машина '", self.name, "' остановилась")

    def turn(self, direction):
        print(f"Машина '", self.name, "' повернула ", str(direction))

    def show_speed(self):
        print(f"Текущая скорость автомобиля", self.name, "' = ", str(self.speed))


class TownCar(Car):
    """ Класс TownCar, содержит:
        Атрибуты
            ..
        Методы:
            show_speed - отображает текущую скорость. При скорости >= 60 - отображает превышение
    """
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print(f"Превышение допустимой скорости 60км\ч!!! Текущая скорость автомобиля ", self.name, "' = ", str(self.speed))
        else:
            super().show_speed()
            # return ("Текущая скорость автомобиля " + self.name + "' = " + str(self.speed))


class SportCar(Car):
    """ Класс SportCar, содержит:
        Атрибуты
            ..
        Методы:
            ..
    """
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    """ Класс WorkCar, содержит:
        Атрибуты
            ..
        Методы:
            show_speed - отображает текущую скорость. При скорости >= 40 - отображает превышение
    """
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print(f"Превышение допустимой скорости 40км\ч!!! Текущая скорость автомобиля ", self.name, "' = ", str(self.speed))
        else:
            super().show_speed()
            # return ("Текущая скорость автомобиля " + self.name + "' = " + str(self.speed))


class PoliceCar(Car):
    """ Класс PoliceCar, содержит:
        Атрибуты
            ..
        Методы:
            ..
    """
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)



def main():
    # Создаем объект класса WorkCar и выводим данные
    wc = WorkCar(30, "grey", "speedwagon")
    wc.go() # +20 км
    wc.show_speed()
    wc.turn("left")
    wc.go() # +20 км
    wc.go() # +20 км
    wc.show_speed()
    wc.stop() # 0 км/ч
    wc.show_speed()
    print(' ') # Перевод строки для наглядности

    # Создаем объект класса PoliceCar и выводим данные
    pc = PoliceCar(80, "white", "patrol")
    pc.go() # +20 км
    pc.show_speed()
    pc.turn("right")
    pc.go() # +20 км
    pc.show_speed()
    pc.stop() # 0 км/ч
    print(' ') # Перевод строки для наглядности

    # Создаем объект класса TownCar и выводим данные
    tc = TownCar(25, "yellow", "taxi")
    tc.show_speed()
    tc.go() # +20 км
    tc.go() # +20 км
    tc.go() # +20 км
    tc.show_speed()
    tc.stop() # 0 км/ч
    tc.show_speed()
    print(' ') # Перевод строки для наглядности


if __name__ == '__main__':
    main()