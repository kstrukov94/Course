"""ПОИСК ФИЛЬМОВ"""
# Рядом с программой находится файл films.txt в кодировке cp1251, который содержит список фильмов.
# Каждый фильм записан с отдельной строки и состоит из идентификатора, названия на русском языке и названия на английском языке.
# Все элементы отделены друг от друга запятой. Пример такого файла:
#
# 1,Зеленая миля,The Green Mile
# 2,Побег из Шоушенка,The Shawshank Redemption
# 3,Список Шиндлера,Schindler's List
# 4,1+1,Intouchables
# 5,Форрест Гамп,Forrest Gump
# 6,Интерстеллар,Interstellar
# Напишите программу, которая из первого аргумента командной строки получает название или часть названия фильма, а затем ищет его в файле.
# Название фильма может передаваться в любом регистре на любом языке.
#
# Программа должна выводить названия фильмов на русском языке в том порядке, в котором они находятся в файле.
# На один поисковый запрос может быть найдено несколько фильмов.
#
# Пример использования:
# > python program.py "список"
# Список Шиндлера
# > python program.py "orres"
# Форрест Гамп
# > python program.py "int"
# 1+1
# Интерстеллар

import sys
search_request = sys.argv[1] # lower() при получении переменной желательнее

for line in open("5_films.txt", "r", encoding="cp1251"):
    film_id, film_name_rus, film_name_eng = line.strip().split(",")
    if search_request.lower() in film_name_rus.lower() or search_request.lower() in film_name_eng.lower():
        print(film_name_rus)

# import sys
#
# name = sys.argv[1].lower()
#
# founded = []
# # Открываем файл в кодировке cp1251
# for line in open("films.txt", "r", encoding="cp1251"):
#     # Получаем элементы строки
#     _, ru_name, en_name = line.strip().split(",")
#
#     # Ищем совпадения
#     if name in ru_name.lower() or name in en_name.lower():
#         founded.append(ru_name)
#
# print("\n".join(founded))