#########################################################################
#
# Author: Dmitry Gromov
# Date: 2021-06-08
# Description: task1 of homework8
#
#########################################################################


class Date():
    """ Класс 'Date'
        атрибуты:
            - day (1 - 31)
            - month (1 - 12)
            - year (0 - 3000)
        методы:
            - parse_date_str - парсит строку и возвращает список целых чисел
            - validate_date - проверяет строку на соответсвие шаблону 'dd-mm-yyyy'
    """

    @classmethod
    def parse_date_str(self, date_str):
        date_list = date_str.split(sep="-")
        # self.day = int(date_list[0])
        # self.month = int(date_list[1])
        # self.year = int(date_list[2])
        return [int(date_list[0]), int(date_list[1]), int(date_list[2])]

    @staticmethod
    def validate_date(date_str):
        date_list = date_str.split(sep="-")
        try:
            if int(date_list[0]) not in range(1, 32):
                return False
            elif int(date_list[1]) not in range(1, 13):
                return False
            elif int(date_list[2]) not in range(0, 3001):
                return False
        except ValueError as ve:
            print("Строка не соответсвует шаблону: dd-mm-yyyy")
            return False
        return True

    def __init__(self, date_str):
        self.day, self.month, self.year = Date.parse_date_str(date_str)

    def __str__(self):
        return str(self.day).zfill(2) + '-' + str(self.month).zfill(2) + '-' + str(self.year).zfill(4)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    date_str = "10-03-2008"
    print("Проверяем валидность строки \"10-03-2008\":", Date.validate_date(date_str))

    date_str = "41-03-2021"
    print("Проверяем валидность строки \"41-03-2021\":", Date.validate_date(date_str))

    date_str = "15-13-2020"
    print("Проверяем валидность строки \"15-13-2020\":", Date.validate_date(date_str))

    parsed = Date.parse_date_str(date_str)
    print("Проверяем парсинг строки \'10-03-2008\':", parsed)

    date_str = "10-03-2008"
    my_date = Date(date_str)
    print("Принтим дату \"10-03-2008\":",  my_date)

    date_str = "23-05-100"
    my_date = Date(date_str)
    print("Принтим дату \"23-05-100\":",  my_date)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
