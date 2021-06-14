##########################################################
#
# iterator2 for task #6-2
#
##########################################################

from itertools import cycle, count

def get_iterator_two(input_list, loops):
    """ Функция (генератор) принимает список данных и количество циклов его повтора"""

    # Вычислем длину результирующего набора =  длина списка * кол-во циклов
    list_len = len(input_list) * loops
    index = 0
    # Получаем итератор
    iter = cycle(input_list)

    # Извлекаем следующий элемент и увеличиваем индекс пока он меньше требуемой длины
    while index < list_len:
        current_item = next(iter)
        yield current_item
        index += 1

