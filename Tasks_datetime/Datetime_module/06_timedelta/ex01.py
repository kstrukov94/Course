"""ДНЕЙ ОСТАЛОСЬ"""

"""Напишите программу, которая принимает из аргументов командной строки 6 значений: 
год, месяц, день, часы, минуты и секунды. 
Переданная дата всегда находится в будущем и после её обработки, 
программа должна вывести количество полных дней, которое осталось до этой даты.

Пример использования (на момент запуска 5 апреля 2020 в 19:44:25):
> python program.py 2020 04 10 22 12 24
> 5"""

import sys
from datetime import datetime as dt

now_date = dt.now()
year, month, day, hours, minutes, seconds = sys.argv[1:]
raw_date = dt(int(year), int(month), int(day), int(hours), int(minutes), int(seconds))
# ЛИБО
# raw_date_str = ' '.join(sys.argv[1:])
# raw_date = dt.strptime(raw_date_str, '%Y %m %d %H %M %S')
print((raw_date - now_date).days)
