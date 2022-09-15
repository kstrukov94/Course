"""ЗАПОЛНЯЕМ ПРОМЕЖУТКИ, ЧАСТЬ 3"""
# Напишите программу, которая из аргументов командной строки принимает два вещественных числа: начальное и конечное,
# а после заполняет промежуток между этими числами с шагом 0.1.
#
# В случае если первое число меньше второго, то промежуток заполняется числами в порядке увеличения.
# Если первое число больше второго, то числа в промежутке должны идти в убывающем порядке.
#
# Используйте функцию range().
#
# Пример использования:
# > python program.py 0.7 1.5
# > 0.7 0.8 0.9 1.0 1.1 1.2 1.3 1.4 1.5
# > python program.py 1.5 0.7
# > 1.5 1.4 1.3 1.2 1.1 1.0 0.9 0.8 0.7

import sys
start, end = sys.argv[1:]
start = int(float(start) * 10)
end = int(float(end) * 10 + 1)
result = []
if start < end:
    for n in range(start, end):
        result.append(str(n/10))
else:
    end -= 2
    for n in range(start, end, -1):
        result.append(str(n/10))
print(" ".join(result))

# import sys
# start = float(sys.argv[1])
# end = float(sys.argv[2])
#
# # Корректировка шага и конечного значения.
# if start > end:
#     step = -1
#     end = int(end * 10) - 1
# else:
#     step = 1
#     end = int(end * 10) + 1
#
# # Формируем начальное значение.
# start = int(start * 10)
#
# # Перебираем целые числа с помощью range.
# values = []
# for value in range(start, end, step):
#     values.append(str(value / 10))
#
#
# print(" ".join(values))