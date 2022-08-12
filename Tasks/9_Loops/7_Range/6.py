"""FIZZBUZZ"""
# Популярная задача с собеседований.
# Напишите программу, которая получает из первого аргумента командной строки число N,
# а затем выводит числа от 1 до N (включительно).
# При этом вместо чисел, кратных трем, программа должна выводить слово Fizz, а вместо чисел, кратных пяти — слово Buzz.
# Если число кратно и 3, и 5, то программа должна выводить слово FizzBuzz.
#
# Пример использования:
# > python program.py 20
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
# Fizz
# 19
# Buzz

import sys
end = int(sys.argv[1]) + 1

for n in range(1, end):
    string = ""
    if n % 3 and n % 5:
        string = n
    if n % 3 == 0:
        string += "Fizz"
    if n % 5 == 0:
        string += "Buzz"
    print(string)




