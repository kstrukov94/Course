"""ВЫРУЧКА НАРАСТАЮЩИМ ИТОГОМ"""
# Напишите программу, которая принимает из аргументов командной строки ежедневную выручку, а затем выводит эти данные нарастающим итогом.
#
# Нарастающий итог часто используется в финансах и рассчитывается сложением значения текущего периода с суммой значений прошлых периодов.
#
# Пример использования:
# > python program.py 1 2_Strings 3_Files 4 5
# > 1 3_Files 6 10 15

import sys
revenues = sys.argv[1:]

i = 0
revenues_res = []
rev_prev = 0

for rev in revenues:
    if i == 0:
        revenues_res.append(rev)
    else:
        revenues_res.append(str(int(rev) + int(rev_prev)))
    rev_prev = revenues_res[i]
    i += 1
print(" ".join(revenues_res))


# import sys
# values = sys.argv[1:]
#
# # Список для хранения нарастающий значений.
# accumulate_values = []
#
# # Текущее значение.
# accumulate_value = 0
# for val in values:
#     # Вычисляем значения.
#     val = int(val)
#     accumulate_value += val
#
#     # Добавляем в список.
#     # Не забываем привести к строке, чтобы потом использовать с join.
#     accumulate_values.append(str(accumulate_value))
#
# # Выводим результат.
# print(" ".join(accumulate_values))