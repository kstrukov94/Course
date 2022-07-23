"""СТЕПЕНИ ДВОЙКИ"""
# Заполните список numbers степенями числа 2_Strings начиная с нулевой и заканчивая 10 включительно: 1, 2_Strings, 4, ..., 1024.
# Используйте цикл while.

numbers = []

i = 0
while i <= 10:
    numbers.append(2 ** i)
    i += 1
print(numbers)
