"""ПАРСИМ ДАТУ"""

"""Напишите программу, которая из первого аргумента командной строки принимает дату и время в формате "ГГГГММДДЧЧММСС", 
а затем выводит эту же дату в формате "ДД.ММ.ГГ ЧЧ:ММ".

Пример использования:
> python program.py 20190418133454
> 18.04.19 13:34"""

import sys
from datetime import datetime

this_date = datetime.strptime(sys.argv[1], '%Y%m%d%H%M%S')
print(this_date.strftime('%d.%m.%y %H:%M'))
