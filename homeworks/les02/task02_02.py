"""
2.
Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

"""

print('Введите список значений. Чтобы закончить заполнение списка введите "-"')
user_list = []
user_item = ''
counter = 0

while user_item != '-':
    user_item = input(f'Введите элемент с индеком {counter}: ')
    if user_item != '-':
        user_list.append(user_item)
        counter += 1
    else:
        break

i = 0
while i < len(user_list) - 1:
    user_list[i], user_list[i+1] = user_list[i+1], user_list[i],
    i += 2

print(f'Результат обмена соседних элементов: {user_list} ')