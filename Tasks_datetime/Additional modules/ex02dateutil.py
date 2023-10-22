"""ЕЖЕМЕСЯЧНЫЕ ПЛАТЕЖИ"""

"""
Напишите программу, которая принимает из командной строки два параметра: 
дату первого платежа в формате «ГГГГ-ММ-ДД» и количество платежей, 
а затем выводит график ежемесячных платежей начиная с переданной даты.

Каждую дату графика нужно выводить в формате «ДД.ММ.ГГ», а сами даты следует разделить запятой и пробелом.

Пример использования
> python program.py "2020-04-07" 3
> 07.04.20, 07.05.20, 07.06.20"""

import sys
from dateutil import relativedelta
from dateutil.parser import parse


inp_date_str, payments_count = sys.argv[1:]
start_date = parse(sys.argv[1])
payment_dates = []
for n in range(int(payments_count)):
    payment_dates.append((start_date + relativedelta.relativedelta(months=n)).strftime("%d.%m.%y"))
print(', '.join(payment_dates))