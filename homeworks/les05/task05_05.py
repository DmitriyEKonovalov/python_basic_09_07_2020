"""
5.
Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import random

num_cnt = 10  # количество чисел
num_lim = [-50, 50]  # диапазон для случайных чисел
with open('task05_05file.txt', 'w', encoding='UTF-8') as file:
    # файл заполняется num_cnt случайными целыми числами в заданном диапазоне num_lim
    file.write(' '.join([str(round(random() * (num_lim[1] - num_lim[0]) + num_lim[0])) for _ in range(num_cnt)]))

with open('task05_05file.txt', 'r', encoding='UTF-8') as file:
    print(sum([int(num) for num in (file.readline()).split(' ')]))
