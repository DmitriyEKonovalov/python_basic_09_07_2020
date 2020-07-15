"""
6. *
Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}

"""

# заполнение базы данных
ITEM_PARS = ("название", "цена", "количество", "ед")  # параметры товаров
goods = []

print('Заполните базу товаров. Чтобы закончить введите "-" (незаконченный товар не сохранится)')
user_input = ''
counter = 1
while user_input != '-':
    goods.append((counter, {}))  # создать новую запись в базе
    for item_par in ITEM_PARS:  # для каждого параметра ввести значение
        user_input = input(f'Для товара №{counter} введите характеристику "{item_par}": ')
        goods[counter - 1][1].update({item_par: user_input})
        if user_input == '-':
            break
    if user_input == '-':
        goods.pop(-1)  # удалить незаконченную запись в базе
        break
    else:
        counter += 1

# заполненная база для тетсирования аналитики, чтобы не вводить саммоу
# goods = [
#     (1, {'название': 'a', 'цена': 1, 'количество': 11, 'ед': 'aa'}),
#     (2, {'название': 'b', 'цена': 2, 'количество': 22, 'ед': 'bb'}),
#     (3, {'название': 'c', 'цена': 3, 'количество': 33, 'ед': 'cc'})
# ]

# сбор аналитики
analyze = {
    "название": [],
    "цена": [],
    "количество": [],
    "ед": []
}
for item in goods:
    for item_par in item[1]:
        analyze[item_par].append(item[1][item_par])
        
# вывод аналитики
print(f'\nАналитика\n{"-"*40}\n')
for item_par in analyze:
    print(f'{item_par}: {analyze[item_par]}')
