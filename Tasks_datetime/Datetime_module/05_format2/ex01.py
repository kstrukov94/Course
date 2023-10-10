"""АМЕРИКАНСКОЕ ВРЕМЯ"""
"""В американском языке время обычно записывают в 12-часовом формате с добавление суффикса am или pm. 
Am означает «до полудня», pm «после полудня». 
Так время 2:12 pm — это 14:12 если переводить на 24-часовой формат.

Напишите программу, 
которая принимает из первого аргумента командной строки дату в следующем виде "October 13, 2015 1:16 pm", 
а затем выводит время в 24-часовом формате.

Пример использования:
> python program.py "October 13, 2015 1:16 pm"
> 13:16"""


import sys
from datetime import datetime as dt

date_raw = dt.strptime(sys.argv[1], "%B %d, %Y %I:%M %p")
print(f"{date_raw:%H}:{date_raw:%M}")


""" Старое решение
import sys
from datetime import datetime as dt

date_raw = dt.strptime(sys.argv[1], '%B %d, %Y %I:%M %p')
print(f"{date_raw.strftime('%H')}:{date_raw.strftime('%M')}")"""