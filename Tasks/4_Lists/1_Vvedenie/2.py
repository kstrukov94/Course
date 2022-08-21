# В программе ниже заданы два списка: с именами и фамилиями.
# Расширьте код так, чтобы программа принимала из командной строки два аргумента:
# номер имени и номер фамилии, а затем выводила сгенерированную на основе списков строку вида ИМЯ ФАМИЛИЯ.
#
# Обратите внимание, что передаваться в программу будут номера имен и фамилий так,
# # как будто они начинаются с единицы. То есть имя «Иван» имеет номер 1, а «Василий» - 4.
#
# Финальная строка должна выводится в верхнем регистре.
#
# Пример использования:
# > python program.py 1 1
# > ИВАН АНТОНОВ

first_names = ['Иван', 'Пётр', 'Дмитрий', 'Василий']
last_names = ['Антонов', 'Шмидт', 'Лебедев', 'Васильев', 'Шиков']

import sys
name_number, last_name_number = int(sys.argv[1]), int(sys.argv[2])
result = ("%s %s" % (first_names[name_number-1], last_names[last_name_number-1])).upper()
print(result)


# import sys
#
# # Получаем данные.
# fn_index = int(sys.argv[1]) - 1
# ln_index = int(sys.argv[2_Strings]) - 1
#
# first_names = ['Иван', 'Пётр', 'Дмитрий', 'Василий']
# last_names = ['Антонов', 'Шмидт', 'Лебедев', 'Васильев', 'Шиков']
#
# # Формируем строку.
# fl = "{} {}".format(first_names[fn_index], last_names[ln_index])
#
# # Выводим с увеличенным регистром.
# print(fl.upper())