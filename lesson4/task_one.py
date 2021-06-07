####################################################################
#
# Author: Dmitry Gromov
# Date: 2021-05-25
# Description: task1 of Homework4
#
####################################################################

""" 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
    В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
    Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""

import sys

def print_usage():
    """ Вывод справки по использованию"""

    print("Usage: task_one.py <output> <hourly wage> <bonus>")


def calculate_salary(output, hourly_wage, bonus):
    """ Расчет зп по формуле: (выработка в часах * ставка в час) + премия."""

    return ((output * hourly_wage) + bonus)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """ Расчет заработной платы сотрудника по формуле: (выработка в часах * ставка в час) + премия."""
    
    if len(sys.argv) != 4:
        print("Неверное число заданных параметров. Отмена.")
        print_usage()
        sys.exit(0)

    try:
        output = int(sys.argv[1])
        hourly_wage = int(sys.argv[2])
        bonus = int(sys.argv[3])
    except ValueError as e:
        print("Указанный параметр не является числом. Отмена.")
        print_usage()
        sys.exit(0)

    print(f"Расчитанная зарплата сотрудника:", calculate_salary(output, hourly_wage, bonus))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
