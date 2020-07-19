"""
3.
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.

"""


def my_func(a, b, c):
    return (a if a > b else b) + (b if b > c else c)


print(my_func(1, 2, 3))
print(my_func(2, 1, 3))
print(my_func(3, 2, 1))
