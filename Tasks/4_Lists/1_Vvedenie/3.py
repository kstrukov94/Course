# ЗАМЕНА ЗНАЧЕНИЯ
# Напишите программу, которая принимает из аргументов командной строки индекс элемента списка languages,
# а также новое значение, которое должно быть размещено на позиции переданного индекса.
# После замены элемента, программа должна вывести список в консоль.
#
# Пример использования:
# > python program.py 1 PHP
# > ['Python', 'PHP', 'JavaScript', 'Java']

languages = ['Python', 'C++', 'JavaScript', 'Java']
import sys
lang_index, new_data = int(sys.argv[1]), sys.argv[2]
languages[lang_index] = new_data
print(languages)


