##################################################################
#
#  Author: Dmitry Gromov
#  Date: 2021-05-31
#  Description: task3 of homework5
#
##################################################################


import sys


def main():
    """ 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
        Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
        Выполнить подсчет средней величины дохода сотрудников.
    """

    #
    print("Список сотрудников с зарплатой меньше 20000:\n ")

    print("{}\t\t\t{}".format("\'Сотрудник\'", "\'Зарлата\'"))

    count = 0 # считаем сотрудников
    progressive_sum = 0 # суммируем зп

    # Открываем файл ./text3.txt на чтение.
    try:
        with open("./text3.txt", 'r') as file_in:
            for line in file_in.readlines():
                employee, salary = line.split()
                salary = int(salary)

                count += 1
                progressive_sum += salary

                if(salary >= 20000):
                    continue
                print(f"{employee:<20s}\t{salary:^d}")
    except IOError as e:
        print("Ошибка чтения файла. Выход.")
        sys.exit(-1)

    print(f"\nСредняя зп составляет: ", int((progressive_sum / count)))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
