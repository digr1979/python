##################################################################
#
#  Author: Dmitry Gromov
#  Date: 2021-06-03
#  Description: task7 of homework5
#
##################################################################


import json
import sys


def main():
    """ 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
        Пример строки файла: firm_1 ООО 10000 5000.
        Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
        Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
        Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
        Итоговый список сохранить в виде json-объекта в соответствующий файл.
        Пример json-объекта:
        [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

        Подсказка: использовать менеджеры контекста.
    """

    # Для начала, просто выводим файл
    try:
        with open("./text7_in.txt", encoding="utf8") as file_in:
            print("Содержание файла \'text7_in.txt\':")
            print(file_in.read())
    except IOError as e:
        print(e)
        sys.exit(-1)

    # Собственно, обработка
    cumulative_profit = 0
    company_count = 0
    # Работает с этой строкой
    company_str = "[{"
    average_profit_dict_str = "{\"average_profit\": "

    try:
        with open("./text7_in.txt", encoding="utf8") as file_in:
            for row in file_in.readlines():
                data_list = row.strip().split()
                try:
                    # Считаем прибыль компании
                    profit_num = int(data_list[2]) - int(data_list[3])
                    # Если прибыль есть, то добавляем в расчет средней.
                    if profit_num > 0:
                        cumulative_profit += profit_num
                        company_count += 1
                    # print(data_list[0], str(profit_num))
                    company_str = company_str + "\"" + data_list[0] + "\": " + str(profit_num) + ", "
                except ValueError as e:
                    print(e)
                    sys.exit(-1)
    except IOError as e:
        print(e)
        sys.exit(-1)

    # Правим строку будущего словаря, удалаем последние символы ", "
    company_str = company_str.rpartition(", ")[0] + "}, {\"average_profit\": " + str(int(cumulative_profit) / int(company_count)) + "}]"


    data_list = eval(company_str)


    try:
        with open("./json7.dump", 'w') as json_file:
            json.dump(data_list, json_file, ensure_ascii = False)
    except IOError as e:
        print(e)
        sys.exit(-1)

    print("\nПолученная строка:", company_str)
    print("Средняя прибыль:", str(int(cumulative_profit) / int(company_count)))
    print("Файл \'json7.dump\' успешно записан.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
