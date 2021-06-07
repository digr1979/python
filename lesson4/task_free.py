####################################################################
#
# Author: Dmitry Gromov
# Date: 2021-05-25
# Description: task3 of Homework4
#
####################################################################


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    """3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
    Подсказка: использовать функцию range() и генератор."""

    # Создаём генератор
    my_gen = (i  for i in range(20, 241) if i % 20 == 0 or i % 21 == 0 )

    # # Получаем генератор
    # my_gen = get_my_gen(input_list)

    # Выводим результат
    for i in my_gen:
        print(i, end = ' ')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
