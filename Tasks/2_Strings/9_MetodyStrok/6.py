#Напишите программу, которая получает через аргументы командной строки три числа,
# а после выводит каждое число с правой стороны строки длиной 15 знаков. Слева от чисел должны быть проставлены точки.
# Решение 1
import sys
digit1 = sys.argv[1]
digit2 = sys.argv[2]
digit3 = sys.argv[3]
print("." * (15-len(digit1)) + digit1)
print("." * (15-len(digit2)) + digit2)
print("." * (15-len(digit3)) + digit3)

# Решение 2_Strings

digit1 = sys.argv[1]
digit2 = sys.argv[2]
digit3 = sys.argv[3]
print(digit1.rjust(15, '.'))
print(digit2.rjust(15, '.'))
print(digit3.rjust(15, '.'))
