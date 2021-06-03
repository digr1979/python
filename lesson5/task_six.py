##################################################################
#
#  Author: Dmitry Gromov
#  Date: 2021-06-02
#  Description: task6 of homework5
#
##################################################################


import sys


def calculate_subject_hours(hours):
    """ Суммирует учебные часы в строке

    :param hours:
        Список с количеством учебных часов по предмету
    :return:
        Сумма всех часов
    """

    hours_cumulative_sum = 0

    hours_list = hours.split(sep = ' ')

    for i in hours_list:
        # Если длина элемента меньше 4 знаков, то пропускаем
        if len(i) < 4:
            continue
        try:
            # Сплитим элемент один раз по левой скобке и берём самый первый элемент полученного списка
            num = i.split(sep = '(', maxsplit = 1)[0]
            hours = int(num)
        except Exception as e:
            # если исключение, то считаем остальное
            continue
        hours_cumulative_sum += hours

    return hours_cumulative_sum


def main():
    """ 6. Необходимо создать (не программно) текстовый файл,
        где каждая строка описывает учебный предмет и наличие лекционных,
        практических и лабораторных занятий по этому предмету и их количество.
        Важно, чтобы для каждого предмета не обязательно были все типы занятий.
        Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

        Примеры строк файла:
        Информатика: 100(л) 50(пр) 20(лаб).
        Физика: 30(л) — 10(лаб)
        Физкультура: — 30(пр) —

        Пример словаря:
        {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
    """

    print("Данные читаются из файла \'text6_in.txt\'\n")
    dist_str = "{"

    try:
        with open("./text6_in.txt", 'r', encoding = "utf8") as file_in:
            for line in file_in.readlines():
                subject, hours_str = line.split(sep = ':')
                subject_hours = calculate_subject_hours(hours_str)
                dist_str = dist_str + "\"" + subject + "\": " + str(subject_hours) + ", "

            # В строке получилась лишняя подстрока ", ", поэтому партиционируем полученную строку справа по запятой
            # и получаем первый элемент кортежа
            dist_str = dist_str.rpartition(',')[0] + "}"

            # Создаем сам словарь
            subject_dist = eval(dist_str)
            print(f"Результат: {subject_dist}")
    except IOError as e:
        print("Ошибка чтения файла. Выход.")
        sys.exit(-1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
