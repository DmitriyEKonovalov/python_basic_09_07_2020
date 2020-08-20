"""
3.
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

"""


class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def _set_income(self, wage, bonus):
        self._income = {'wage': wage, 'bonus': bonus}

    def _get_income(self):
        return self._income.copy()


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._set_income(wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        result = self._get_income()
        return sum([i for i in self._get_income().values()])


position1 = Position('Иван', 'Смирнов', 'медбрат', 2000, 500)
position2 = Position('Анна', ' Петрова', 'врач', 3000, 100)

print(position1.get_full_name())
print(position1.get_total_income())

print(position2.get_full_name())
print(position2.get_total_income())

