# По умолчанию положительные числа выводятся без знака «плюс»:
#
# print(10)
# 10   # Положительное число. Выводится без знака +
# print(-10)
# -10  # Отрицательное число. Выводится со знаком -

# Однако иногда требуется явно указать знак для числа, например при выводе температуры.
# Для этого используются следующие спецификаторы: {:+d}, {:+f}, {:+.Nf}, где N — число знаков после десятичной точки.

# Если в спецификатор передается отрицательное число, то оно будет выведено со знаком «минус», а если положительное, то со знаком «плюс»:
# print("{:+d}, {:+.3f}".format(10, -7.4589))
# +10, -7.459

# Напишите программу, выводящую средний балл ученика с указанием разницы относительно прошлого периода.
# Программа должна принимать из аргументов командной строки два числа: средний балл на начало периода и средний балл на конец периода.
# В конце нужно вывести средний балл на конец периода и разницу между двумя переданными числами. Если разница положительная, то впереди должен стоять +, а если отрицательная, то минус.
# Все числа нужно выводить с двумя знаками после десятичной точки.
#
# Пример использования:
# > python program.py 8.741 8.85
# > 8.85 (+0.11)

import sys
start = float(sys.argv[1])
end = float(sys.argv[2])
diff = end - start
print(f"{end} ({diff:+.2f})".format()) #вычислять в методе формат не надо (нельзя)
