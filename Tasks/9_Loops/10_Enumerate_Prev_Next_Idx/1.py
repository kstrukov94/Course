"""ЕЖЕМЕСЯЧНЫЙ ПРИРОСТ АУДИТОРИИ"""
# Напишите программу, которая принимает из аргументов командной строки ежемесячные показатели регистраций пользователей,
# а затем выводит прирост относительно прошлого месяца.
# Например, если в текущем месяце 150 пользователей, а в прошлом было 100, то текущий прирост составляет 50.
#
# Пример использования:
# > python program.py 127 624 235 235 77 288
# > 127 497 -389 0 -158 211

import sys
regs = sys.argv[1:]
prev_reg = 0
result = []
for index, reg in enumerate(regs):
    prev_reg = int(regs[index - 1]) if index > 0 else 0
    result.append(str(int(reg) - prev_reg))
    # next_regs = regs[index + 1] if index < len(regs) - 1 else 0
print(" ".join(result))

# import sys
#
# values = sys.argv[1:]
#
# # Список для хранения значений.
# diff_values = []
#
# # Предыдущее значение.
# prev_value = 0
#
# for val in values:
#     # Вычисляем разницу.
#     val = int(val)
#     diff = val - prev_value
#
#     # Добавляем в список.
#     diff_values.append(str(diff))
#
#     # Обновляем прошлое значение.
#     prev_value = val
#
# # Выводим результат.
# print(" ".join(diff_values))


