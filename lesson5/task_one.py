##################################################################
#
#  Author: Dmitry Gromov
#  Date: 2021-05-31
#  Description: task1 of homework5
#
##################################################################


import sys


def main():
    """ 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
    Об окончании ввода данных свидетельствует пустая строка.
    """

    # Небольшой prompt
    print("Введите несколько строк для записи в файл \'ftext1.txt\'\nПустая строка - завершение ввода: ")
    # Открываем стандартный ввод
    stdin = sys.stdin

    # Открываем файл для вывода. Если он уже существует, то будет перезаписан.
    try:
        with open("./text1.txt", 'w') as file_out:
            while True:
                line = stdin.readline()
                # Если длина строки == 0, соответсвенно строка пустая. Завершаем.
                if len(str(line).strip()) == 0:
                    break
                file_out.write(line)
    except IOError as e:
        print("Ошибка чтения файла. Выход.")
        sys.exit(-1)

    print("Файл \'text1.txt\'Записан. ")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
