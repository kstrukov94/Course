"""ЕЖЕНЕДЕЛЬНЫЕ ПЛАТЕЖИ"""

"""Напишите программу, которая принимает из командной строки два параметра: 
дату первого платежа в формате «ГГГГ-ММ-ДД» и количество платежей, 
а затем выводит график еженедельных платежей начиная с переданной даты.

Каждую дату графика нужно выводить в формате «ДД.ММ.ГГ», а сами даты следует разделить запятой и пробелом.

Пример использования
> python program.py "2020-04-07" 5
> 07.04.20, 14.04.20, 21.04.20, 28.04.20, 05.05.20"""

import sys
from datetime import datetime as dt, timedelta as td

first_payment_date, payment_num = sys.argv[1:]
first_payment_date = dt.strptime(first_payment_date, '%Y-%m-%d')
payment_period = td(days=7)
payment_dates = []
for n in range(int(payment_num)):
    payment_dates.append((first_payment_date + (payment_period * n)).strftime('%d.%m.%y'))
print(', '.join(payment_dates))
