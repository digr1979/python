##########################################################
#
# iterator1 for task #6-1
#
##########################################################

from itertools import count

def get_iterator_one(start: int, end: int):
    """ Функция возвращает итерируемое значение в пределе в заданном предлеле с шагом 1"""
    iter = count(start, 1)
    current_item = 0
    while(current_item < end):
        current_item = next(iter)
        yield current_item
