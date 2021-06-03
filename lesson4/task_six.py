####################################################################
#
# Author: Dmitry Gromov
# Date: 2021-05-26
# Description: task6 of Homework4
#
####################################################################


from itertools import count, cycle

from iterator_one import get_iterator_one
from iterator_two import get_iterator_two




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    """6. Реализовать два небольших скрипта:
    а) итератор, генерирующий целые числа, начиная с указанного,
    б) итератор, повторяющий элементы некоторого списка, определенного заранее.
    Подсказка: использовать функцию count() и cycle() модуля itertools. 
    Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
    Необходимо предусмотреть условие его завершения.
    Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. 
    Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено."""

    # 6-1
    # Функция (генератор) принимает два параметра: start и end (значение последнего не входит в последовательность)
    # возращает последовательность с шагом 1
    my_gen = get_iterator_one(5, 29)

    # Выводим результат
    print("Вывод результата задачи 6-1: ")
    for i in my_gen:
        print(i, end = ' ')
    print()

    # 6-2
    # Функция (генератор) принимает два параметра: список данных и кол-во его повторов
    # возращает последовательность с шагом 1 заданное кол-во раз
    #
    my_list = [2, 4, 6, 11]
    my_gen = get_iterator_two(my_list, 3)

    # Выводим результат
    print("Вывод результата задачи 6-2: ")
    for i in my_gen:
        print(i, end = ' ')
    print()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
