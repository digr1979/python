##################################################################
#
#  Author: Dmitry Gromov
#  Date: 2021-06-02
#  Description: task5 of homework5
#
##################################################################


import sys


def calculate_line(line):
    """ Суммирует все цифры в строке

    :param line:
        Строка из цифр, разделенных пробелами
    :return:
        Сумма всех цифр полученной строки
    """

    num = 0
    cumulative_sum = 0
    num_list = line.split(sep = ' ')

    for i in num_list:
        try:
            num = int(i)
        except Exception as e:
            # если исключение, то считаем остальное
            continue
        cumulative_sum += num

    return cumulative_sum


def main():
    """ 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
        Программа должна подсчитывать сумму чисел в файле и выводить ее на экран..
    """

    print("Введите ряд чисел через пробелы. \'Q\\q\' - выход: ")

    stdin = sys.stdin

    while True:
        line = stdin.readline()
        if line == 'Q\n' or line == 'q\n':
            print("Завершение работы.")
            break
        result = calculate_line(line)
        print("сумма =", result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
