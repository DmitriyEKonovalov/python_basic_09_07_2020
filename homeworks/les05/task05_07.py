"""
7.
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{ "firm_1" : 5000 , "firm_2" : 3000 , "firm_3" : 1000 }, { "average_profit" : 2000 }]
Подсказка: использовать менеджер контекста.
"""
import json

with open('task05_07file_in.txt', 'r', encoding='UTF-8') as file:
    firm_table = [[i[0:-1].split(' ')[0],         # название компании
                  i[0:-1].split(' ')[1],          # форма собственности
                  float(i[0:-1].split(' ')[2]),   # выручка
                  float(i[0:-1].split(' ')[3]),   # издержки
                  float(i[0:-1].split(' ')[2]) - float(i[0:-1].split(' ')[3])] # прибыль
                  for i in file.readlines()]
    print(firm_table)
    firm_lst = [{row[0]: row[4] for row in firm_table},
                {'average_profit':
                    sum(row[4] for row in firm_table if row[4] > 0) / sum(1 for row in firm_table if row[4] > 0)}
                ]
    print(firm_lst)

with open('task05_07file_out.json', 'w') as file:
    file.write(json.dumps(firm_lst, ensure_ascii=False))
