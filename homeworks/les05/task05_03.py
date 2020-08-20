"""
3.
Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

with open('task05_03file.txt', 'r', encoding='UTF-8') as file:
    table = [[row.split(' ')[0], float(row.split(' ')[1])] for row in file]
    avg_salary = sum(i[1] for i in table) / len(table)
    name_list = [name[0] for name in table if float(name[1]) < 20000]
    print(f'Средняя зарплата составляет: {avg_salary:.2f}')
    print(f'Список сотрудников с зарплатой меньше 20 тыс: {name_list}')