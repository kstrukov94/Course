# ФАМИЛИЯ И. О.
# Напишите программу, которая принимает фамилию, имя и отчество записанные в одну строку,
# а затем выводит данные в формате: Фамилия И. О.
#
# Учитывайте следующие особенности получаемых данных:
# между словами может быть любое количество пробелов,
# а сами слова могут быть набраны в разных регистрах.
# При этом выводить их нужно в формате, описанном выше.
#
# Пример использования
# > python program.py "ИваноВ иван   Иванович"
# > Иванов И. И.

import sys
fio = sys.argv[1]
last_name, first_name, parent_name = fio.split()
last_name = last_name.capitalize()
first_name = first_name.capitalize()[0]
parent_name = parent_name.capitalize()[0]
print("{} {}. {}.".format(last_name, first_name, parent_name))

# import sys
#
# # Получаем ФИО.
# fio = sys.argv[1]
#
# # Рабиваем по пробелу.
# f, i, o = fio.split()
#
# # Выводим данные.
# print("{} {}. {}.".format(f.capitalize(), i[0].upper(), o[0].upper()))
#
# #
# # Альтернативный вариант.
# #
# import sys
#
# # Получаем ФИО, приводим к нужному виду и сразу разбиваем.
# fio = sys.argv[1].title().split()
#
# # Выводим данные.
# print("{fio[0]} {fio[1][0]}. {fio[2_Strings][0]}.".format(fio=fio))