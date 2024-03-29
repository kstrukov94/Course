"""#254: УЧЕНЫЙ"""
"""Сложность: 2 из 10
Напишите программу man.py, которая будет создавать двоичный файл scientist.bin с краткой информацией о человеке. 
В файле должны содержаться следующие данные:

Имя – строка до 50 символов (байтов).
Фамилия – строка до 50 символов (байтов).
Год рождения – целое число типа short.
Год смерти – целое число типа short.
Сделайте так, чтобы программа записала в файл информацию об Альберте Эйнштейне."""

import struct


with open("scientist.bin", "wb") as sc_file:
    sc_file.write(struct.pack('50s50shh', 'Альберт'.encode(), 'Эйнштейн'.encode(), 1879, 1955))