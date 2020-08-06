"""
2.
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivException(Exception):
    def __init__(self):
        self._message = 'You should not divide by zero'


try:
    a = float(input('Введите делимое:'))
    b = float(input('Введите делитель:'))
    if not b:
        raise MyZeroDivException
    else:
        print(f'a / b = {a/b:.2f}')
except MyZeroDivException:
    print('В другой раз может получится поделить')

