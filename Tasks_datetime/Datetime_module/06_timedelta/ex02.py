"""ДНЕЙ ДО НОВОГО ГОДА"""
"""Напишите программу, которая принимает из аргументов командной строки три параметра: 
год, месяц и день, а затем вычисляет число полных дней до ближайшего к этой дате нового года.

Пример использования:
> python program.py 2020 4 14
> 261"""

import sys
from datetime import datetime

year, month, day = map(int, sys.argv[1:])
raw_date = datetime(year, month, day)
new_year_date = datetime(year, 12, 31)
print((new_year_date - raw_date).days)