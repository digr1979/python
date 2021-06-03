##################################################################
#
#  Author: Dmitry Gromov
#  Date: 2021-05-31
#  Description: task2 of homework5
#
##################################################################


import sys


def main():
    """ 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
        выполнить подсчет количества строк, количества слов в каждой строке.
    """

    # Небольшой prompt
    print("Программное открытие и чтение файла \'text2.txt\': ")

    print("{}\t{}\t{}".format("\'Длина строки\'", "\'Всего слов\'", "\'Строка\'"))

    # Открываем файл на чтение.
    try:
        with open("./text2.txt", 'r') as file_in:
            for line in file_in.readlines():
                word_count = len(line.split())
                str_len = len(line)
                print(f"{str_len:^12d}\t{word_count:^12d}\t{line:s}")
    except IOError as e:
        print("Ошибка чтения файла. Выход.")
        sys.exit(-1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
