"""#253: ФИЛЬМ"""
"""Сложность: 3 из 10
В двоичном файле film.data содержится информация о фильме. 
Данные хранятся в следующем формате: 50s50sif10s, что соответствет 
названию фильма на русском языке, названию фильма на английском языке, бюджету, рейтингу и дате в формате ГГГГ-ММ-ДД. 
Все строки хранятся в кодировке windows-1251.

Напишите программу film.py, 
которая прочитает данные этого файла и выведет в консоль российское название фильма и его год выпуска в скобках.

Двоичный файл, на котором можно потренироваться: film.data

Пример использования (на основе тестового файла):
> python film.py
> Тор: Рагнарёк (2017)"""


import struct
from datetime import datetime as dt


with open("film.data", "rb") as film_file:
    film = film_file.read()
    name_ru, name_eng, budget, rating, release_date = struct.unpack("50s50sif10s", film)

    name_ru = name_ru.decode("windows-1251").rstrip("\x00")

    release_date = dt.strptime(release_date.decode("windows-1251"), "%Y-%m-%d")
    release_year = str(release_date.year)

    pattern = f"{name_ru} ({release_year})"
print(pattern)