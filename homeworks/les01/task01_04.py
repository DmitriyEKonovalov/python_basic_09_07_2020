# 4.
# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

n = int(input("введите целое число n: "))

remain = n
maxDigit = 0

while remain > 0:
    digit = remain % 10
    if digit > maxDigit:
        maxDigit = digit
    remain = remain // 10

print("Максимальная цифра в числе:", maxDigit)