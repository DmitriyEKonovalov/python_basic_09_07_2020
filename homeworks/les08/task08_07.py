""""
7.
Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение
и умножение созданных экземпляров. Проверьте корректность полученного результата.

"""


class ComplexNum:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        сложение комплексных чисел (a + bi) + (c + di) = (a + c) + (b + d)i
        """
        a, b = self.x, self.y
        c, d = other.x, other.y
        return ComplexNum(a + c, b + d)

    def __mul__(self, other):
        """
        умножение комплексных чисел (a + bi) * (c + di) = (ac - bd) + (bc + ad)i
        """
        a, b = self.x, self.y
        c, d = other.x, other.y

        return ComplexNum(a * c - b * d, b * c + a * d)

    def __str__(self):
        return f'({self.x}, {self.y}i)'


# проверка
c_num1 = ComplexNum(10, 5)
c_num2 = ComplexNum(-4, 2)
c_num3 = ComplexNum(-1, -1)

print(c_num1 + c_num2)
print(c_num2 * c_num3)
