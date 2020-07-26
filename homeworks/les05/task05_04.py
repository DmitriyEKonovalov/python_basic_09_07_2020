"""
4.
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

"""

eng_ru_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}
with open('task05_04file.txt', 'r', encoding='UTF-8') as file_in, \
        open('task05_04file_out.txt', 'w', encoding='UTF-8') as file_out:
    while True:
        row = file_in.readline()
        if row:
            row = row.split(' ')
            row[0] = eng_ru_dict[row[0]]
            file_out.writelines(' '.join(row))
        else:
            break
