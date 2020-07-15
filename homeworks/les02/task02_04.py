"""
4.
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки.
Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.

"""

user_string = input('Введите строку из нескольикх слов, разделенных пробелами:\n')

# очистка строки от лишних пробелов (двойных и с краев строки )
while user_string.find("  ") != -1:
    user_string = user_string.replace("  ", " ")
user_string = user_string.strip()

words_list = user_string.split(" ")

for word in words_list:
    print(f'{words_list.index(word)+1}. {word[0:10]}')




