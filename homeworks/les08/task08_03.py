"""
3.
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число)
и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""


class NotNumberException(Exception):
    def __init__(self):
        self._message = 'Not a number!'


def str_to_float(s: str) -> float:
    try:
        result = float(s)
        return result
    except ValueError:
        raise NotNumberException


user_input = ' '
lst = []
while user_input != 'stop':
    user_input = input('Введите число (для выхода введите stop):')
    try:
        number = str_to_float(user_input)
        lst.extend([number])
    except NotNumberException:
        if user_input != 'stop':
            print('Необходимо ввести число или stop (для выхода)')


print(f'Введен список чисел:\n{lst}')
