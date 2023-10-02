"""УДАЛЯЕМ ФРУКТ
В редакторе кода содержится множество фруктов.
Напишите программу, которая получает из аргументов командной строки название фрукта,
а после удаляет его из множества fruits.

Если фрукта во множестве нет, программа не должна падать с ошибкой.
После удаления нужно вывести оставшееся множество.

Пример использования:
> python program.py Киви
> {"Яблоки", "Бананы", "Ананасы"}"""


import sys

# Множество фруктов
fruits = {"Яблоки", "Бананы", "Ананасы", "Киви"}

inp_fruit = sys.argv[1]
fruits.discard(inp_fruit)
print(fruits)