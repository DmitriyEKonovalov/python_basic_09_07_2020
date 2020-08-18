"""
6.
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().

"""


def int_func(word: str) -> str:
    result = word[0].upper() + word[1:]
    return result


def cleanup_str(s: str):
    """
    Очистка строки от двойных пробелов и пробелов с краев строки
    """
    while s.find("  ") != -1:
        s = s.replace("  ", " ")
    s = s.strip()
    return s


user_string = input('Введите строку из слов разделенных пробелами:\n')
user_string = cleanup_str(user_string)
words_list = user_string.split(" ")
words_list = map(int_func, words_list)
print(" ".join(words_list))





