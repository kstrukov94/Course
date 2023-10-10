"""АМЕРИКАНСКИЙ АНГЛИЙСКИЙ"""

"""В американском английском дату часто записывают в следующем формате «January 1, 2020». 
Напишите программу, которая преобразовывает дату из американского формата в российский — «1 января 2020».

Пример использования:
> python program.py "January 1, 2020"
> 1 января 2020"""

import sys
from datetime import datetime as dt

month_dict = {
    'January': 'января',
    'February': 'февраля',
    'March': 'марта',
    'April': 'апреля',
    'May': 'мая',
    'June': 'июня',
    'July': 'июля',
    'August': 'августа',
    'September': 'сентября',
    'October': 'октября',
    'November': 'ноября',
    'December': 'декабря'
}

inp_date = dt.strptime(sys.argv[1], '%B %d, %Y')
date_str = inp_date.strftime('%d %B %Y')
date_str = date_str.lstrip('0')
for month in month_dict:
    if month in date_str:
        date_str = date_str.replace(month, month_dict[month])
print(date_str)


""" Решение преподавателя
import sys
from datetime import datetime

MONTHS = [None, "января", "февраля", "марта", "апреля", "мая", "июня",
          "июля", "августа", "сентября", "октября", "ноября", "декабря"]

# Получаем даные.
date = datetime.strptime(sys.argv[1], "%B %d, %Y")

# Формируем результат.
date = "{} {} {}".format(date.day, MONTHS[date.month], date.year)

# Альтернативный вариант с поомщью f-строк
# date = f"{date.day} {MONTHS[date.month]} {date:%Y}"

print(date)"""

