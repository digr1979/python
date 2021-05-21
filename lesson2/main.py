##############################################################
#
# Author: Dmitry Gromov
# Date: 2021-05-21
# Description: homework2
#
##############################################################



def task_one():
    """
    1. Создать список и заполнить его элементами различных типов данных.
    Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
    Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
    """
    my_list = ['prosto stroka', 24, 0.15, (1, '2'), True, {'some_key':'some_value'}, 1+5j, ['item1', 'item2', 'some_str']]

    for item in my_list:
        print(f'type of {item} is: ', type(item))


def task_two():
    """
    2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
    При нечетном количестве элементов последний сохранить на своем месте.
    Для заполнения списка элементов необходимо использовать функцию input()
    """
    my_list = []
    new_list = []

    list_len = int(input("Укажите длину вводимого списка: "))

    for i in range(0, list_len, 1):
        my_list.append(input("Введите новый элемент списка: "))

    index_start = 0
    index_end = 2

    while(index_end <= list_len):
        item_left, item_right = my_list[index_start:index_end]
        new_list.append(item_right)
        new_list.append(item_left)
        index_start += 2
        index_end += 2
    else:
        if(list_len > index_start and list_len < index_end):
            new_list.append(my_list[index_start])

    print(f"Введённый список: {my_list}")
    print(f"Преобразованый список: {new_list}")


def task_free():
    """
    3. Пользователь вводит месяц в виде целого числа от 1 до 12.
    Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
    Напишите решения через list и через dict.
    """
    # month_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    # month_dict = {'1':'Январь', '2':'Февраль', '3':'Март', '4':'Апрель', '5':'Май', '6':'Июнь', '7':'Июль', '8':'Август', '9':'Сентябрь', '10':'Октябрь', '11':'Ноябрь', '12':'Декабрь'}

    month_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
    month_dict = {'1':'Зима', '2':'Зима', '3':'Весна', '4':'Весна', '5':'Весна', '6':'Лето', '7':'Лето', '8':'Лето', '9':'Осень', '10':'Осень', '11':'Осень', '12':'Зима'}

    # month_num = int(input("Введите номер месяца (1-12): "))
    month_num_as_str = input("Введите номер месяца (1-12): ")

    # Небольшая проверка на валидность
    if(month_num_as_str.isnumeric() == False):
        print("Введенноё значение не является числом. Выход")
        return

    # Проверка на попадание в диапазон
    month_num = int(month_num_as_str)
    if(month_num not in range(1, 13)):
        print("Введенноё значение не входит в заданный диапазон (1-12). Выход")
        return

    # Решение для списка
    index = month_num - 1
    season_as_list_item = month_list[month_num - 1]
    print(f"\nРешение для списка: {month_list}")
    print(f"Введённый номер месяца соответсвует времени года \'{season_as_list_item}\'")

    # Решение для словаря
    season_as_dict_item = month_dict.get(month_num_as_str)
    print(f"\nРешение для списка: {month_list}")
    print(f"Введённый номер месяца соответсвует времени года \'{season_as_dict_item}\'")


def task_four():
    """
    4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
    Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
    """
    entered_str = input("Введите строку из нескольких слов, разделённых пробелами: ")
    word_list = entered_str.split(sep=' ')

    for num, word in enumerate(word_list, 1):
        print(f"{num}.)", word[:10])


def task_five():
    """
    5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
    У пользователя необходимо запрашивать новый элемент рейтинга.
    Если в рейтинге существуют элементы с одинаковыми значениями,
    то новый элемент с тем же значением должен разместиться после них.
    Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
    Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
    Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
    Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
    Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
    """

    # my_list = [7, 5, 3, 3, 2]
    my_list = [9, 7, 6, 4, 4, 3, ]
    list_len = len(my_list)

    print(f"Исходный список: {my_list}")
    print("Ввод натуральных чисел в цикле. Для отмены, введите любой символ не цифру")
    value = input("Введите число: ")
    while (value.isnumeric()):
        num = int(value)
        for i in range(0, list_len, 1):
            if num > my_list[i]:
                my_list.insert(i, num)
                break
        else:
            my_list.append(num)
        print(f"Полученный список", my_list)
        value = input("Введите число: ")


def task_six():
    """
    6. * Реализовать структуру данных «Товары».
    Она должна представлять собой список кортежей.
    Каждый кортеж хранит информацию об отдельном товаре.
    В кортеже должно быть два элемента — номер товара и словарь с параметрами
        (характеристиками товара: название, цена, количество, единица измерения).
    Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
    """
    product_list = []
    product_attributes_headers_list = ["product_name", "product_price", "product_qty", "mesuring_unit"]
    index = 1


    while(True):
        # Обнуляем будущие атрибуты
        product_attributes_list = []
        product_attributes_list.append(input("Введите наименование товара: "))
        product_attributes_list.append(input("Укажите цену: "))
        product_attributes_list.append(input("Введите количество: "))
        product_attributes_list.append(input("Укажите единицу измерения: "))

        product_dict = dict(zip(product_attributes_headers_list, product_attributes_list))
        product_list.append(tuple([index, product_dict]))
        answer = input("Продолжить добавление товаров (Y/y)-Да, любая другая кнопка-Нет?")
        if(str.upper(answer) != 'Y'):
            break

        index += 1

    # Рисуем шапку
    print("\n№\t\'Наименование\'\t\'Цена\'\t\'Количество\'\t\'Единица измерения\'")

    # Выводим форматированные данные
    for item in product_list:
        print(f"{item[0]}\t{item[1]['product_name']:^14}\t{item[1]['product_price']:^6}\t{item[1]['product_qty']:^12}\t{item[1]['mesuring_unit']:^15}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    task_one()
    task_two()
    task_free()
    task_four()
    task_five()
    task_six()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
