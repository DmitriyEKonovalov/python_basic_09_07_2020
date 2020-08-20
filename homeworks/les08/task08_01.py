"""
1.
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date_str: str):
        self.__date = date_str

    @classmethod
    def date_to_nums(cls, date_str: str) -> (int, int, int):
        return tuple(int(i) for i in date_str.split('-'))

    @staticmethod
    def is_valid_date(date_str) -> bool:
        day_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        try:
            date_num = tuple(int(i) for i in date_str.split('-'))
        except ValueError:
            return False
        finally:
            if date_num[1] in day_in_month.keys() and date_num[0] <= day_in_month[date_num[1]]:
                return True
            else:
                return False


print(Date.date_to_nums('10-12-2020'))
print(Date.is_valid_date('1-5-2020'))
print(Date.is_valid_date('44-12-2020'))


