"""ПРОШЛОЕ, БУДУЩЕЕ И НАСТОЯЩЕЕ"""
# Две любые даты можно сравнить между собой, точно также как и обычные числа:
#
# d1 = date(2020, 1, 1)
# d2 = date(2020, 2, 1)
# print(d2 > d1)
# True

# Напишите программу, которая принимает из аргументов командной строки год, месяц и день,
# а затем сравнивает переданную дату с сегодняшним днем.
# Если сегодня меньше переданной даты, то программа должна вывести будущее,
# если сегодня больше переданной даты, то программа должна вывести прошлое,
# если даты равны, то программа должна вывести настоящее.
#
# Пример использования (2 апреля 2020 года):
# > python program.py 2020 4 1
# > прошлое

from datetime import date
import sys


year, month, day = map(int, sys.argv[1:])
inp_date = date(year, month, day)
today_date = date.today()
if today_date < inp_date:
    print('будущее')
elif today_date > inp_date:
    print('прошлое')
else:
    print('настоящее')

# year, month, day = map(int, sys.argv[1:])
# date_today = date.today()
# date_input = date(year, month, day)
#
# if date_today > date_input:
#     print('прошлое')
# elif date_today < date_input:
#     print('будущее')
# elif date_today == date_input:
#     print('настоящее')
