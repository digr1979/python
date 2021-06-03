##################################################################
#
#  Author: Dmitry Gromov
#  Date: 2021-06-01
#  Description: task4 of homework5
#
##################################################################


import os


def write_to_file(text, rest_string):
    """ записываем в файл './text4_out.txt' значения параметров text и rest_string"""

    try:
        with open("./text4_out.txt", 'a') as file_out:
            file_out.write((text + " " + rest_string))
    except Exception as e:
        print(e)
        return -1
    return 0

def main():
    """ 4. Создать (не программно) текстовый файл со следующим содержимым:
        One — 1
        Two — 2
        Three — 3
        Four — 4
        Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
        При этом английские числительные должны заменяться на русские.
        Новый блок строк должен записываться в новый текстовый файл.
    """

    # Проверяем файл 'text4_out.txt'. Если он есть, то удаляем его
    if os.path.exists("./text4_out.txt"):
        os.remove("./text4_out.txt")

    print("Файл \'text4_in.txt\': ")
    # Открываем файл ./text4_in.txt на чтение.

    with open("./text4_in.txt", 'r') as file_in:
        for line in file_in.readlines():
            print(line, end = '')
            text, rest_string = str(line).split(maxsplit = 1)
            if text == "One":
                text = str("Один")
            elif text == "Two":
                text = str("Два")
            elif text == "Three":
                text = str("Три")
            elif text == "Four":
                text = str("Четыре")
            else:
                continue
            if write_to_file(text, rest_string) == -1:
                print("Ошибка записи в файл. Отмена")
                return

    print("Файл \'text4_out.txt\' успешно записан.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
