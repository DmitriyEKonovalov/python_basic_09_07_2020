"""
2.
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

"""
from abc import ABC, abstractmethod


class Wear:

    @abstractmethod
    def get_cons_amount(self):
        pass


class Suit(Wear):

    def __init__(self, height):
        self._height = height

    def get_cons_amount(self):
        return self._height * 2 + 0.3

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height


class Coat(Wear):

    def __init__(self, size):
        self._size = size

    def get_cons_amount(self):
        return self._size / 6.5 + 0.5

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size


# проверка работы классов
coat = Coat(50)
print(f'{type(coat)}, размер: {coat.size}, расход материала: {coat.get_cons_amount():.2f}')
coat.size = 70  # проверка сеттера
print(f'{type(coat)}, размер: {coat.size}, расход материала: {coat.get_cons_amount():.2f}')

suit = Suit(2)
print(f'{type(suit)}, размер: {suit.height}, расход материала: {suit.get_cons_amount():.2f}')
suit.height = 1  # проверка сеттера
print(f'{type(suit)}, размер: {suit.height}, расход материала: {suit.get_cons_amount():.2f}')

# пример подсчета суммы расхода материала из списка одежды
wear_list = [Coat(50), Suit(2), Coat(60), Suit(1.5), Suit(1.2)]
print([round(i.get_cons_amount(), 2) for i in wear_list])
total_cons_amount = sum(i.get_cons_amount() for i in wear_list)
print(round(total_cons_amount, 2))