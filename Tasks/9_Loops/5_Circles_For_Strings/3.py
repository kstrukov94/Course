"""РАЗДЕЛЯЕМ ЧИСЛА"""
# Напишите программу, которая принимает через аргументы командной строки произвольное количество целых чисел,
# а затем разделят их на отрицательные и положительные.
#
# Программа должна сперва вывести отрицательные числа, а затем положительные.
# Ноль нужно отнести к положительным.
# Числа следует выводить через пробел.
# Порядок следования чисел нужно сохранить (то есть сортировать числа не нужно).
#
# Пример использования:
# > python program.py 5 1 -3 6 -8 9
# > -3 -8 5 1 6 9

import sys
nums = sys.argv[1:]

positive = []
negative = []

for num in nums:
    if int(num) >= 0:
        positive.append(num)
    else:
        negative.append(num)
result = negative + positive
print(" ".join(result))
