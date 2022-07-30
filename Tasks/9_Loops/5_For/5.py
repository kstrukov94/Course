"""СРАВНЕНИЕ С ЛУЧШИМ МЕСЯЦЕМ"""
# Напишите программу, которая принимает из аргументов командной строки ежемесячные показатели регистраций пользователей,
# а затем сравнивает показатели каждого месяца с лучшим и выводит разницу.
#
# Пример использования:
# > python program.py 127 624 235 235 77 288
# > -497 0 -389 -389 -547 -336

import sys
regs = sys.argv[1:]
regs_max = 0

for reg in regs:
    if int(reg) > regs_max:
        regs_max = int(reg)

regs_result = []
for reg in regs:
    regs_result.append(str(int(reg) - regs_max))

print(" ".join(regs_result))

# import sys
#
# values = sys.argv[1:]
#
# # Сперва вычисляем лучший месяц.
# max_value = int(values[0])
# for value in values[1:]:
#     value = int(value)
#     if value > max_value:
#         max_value = value
#
# result = []
#
# # Теперь сравнение
# for value in values:
#     # Вычисляем разницу.
#     value = int(value)
#     diff = value - max_value
#
#     # Добавляем в список.
#     result.append(str(diff))
#
# # Выводим результат.
# print(" ".join(result))