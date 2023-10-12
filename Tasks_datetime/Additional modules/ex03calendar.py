"""ПЕРВЫЙ ПОНЕДЕЛЬНИК МЕСЯЦА"""

"""Каждый день в 9 часов утра на сервере запускается скрипт, задача которого сформировать и отправить отчет за прошлый месяц. 
Отчет за прошлый месяц необходимо отправлять в первый понедельник текущего месяца.

Напишите программу, которая из первого аргумента командной строки принимает дату в формате ГГГГ-ММ-ДД, 
а затем выводит True если переданный день — это первый понедельник месяца и False в противном случае.

Пример использования:
> python program.py 2022-01-03
> True
> python program.py 2022-01-10
> False"""

"""import sys
from calendar import Calendar
year, month, day = map(int, str(sys.argv[1]).split('-'))
c = Calendar()
month_calendar = c.monthdayscalendar(year, month)

result = False
for week in range(len(month_calendar)):
    if month_calendar[week][0] != 0:
        if month_calendar[week][0] == day:
            result = True
            break
        else:
            break
print(result)
"""
#TODO Изучить варианты решения преподавателя

"""# Три варианта решения.

import sys
from datetime import datetime, timedelta
import calendar

# Получаем дату
date = datetime.strptime(sys.argv[1], "%Y-%m-%d")


# Вариант 1 (используем calendar)
def is_first_monday(date):
    # Получаем весь месяц
    for week in calendar.monthcalendar(date.year, date.month):
        monday = week[0]
        if monday != 0:
            # Получаем число первого понедельника и сразу вычисляем дату.
            first_monday_day = monday
            break

    # Тут PyCharm будет ругаться на переменную first_monday_day, но это он просто не знает особенности алгоритма.
    return datetime(date.year, date.month, first_monday_day) == datetime(date.year, date.month, date.day)


# Вариант 2 (используем calendar)
# Принцип такой же как и у первого варианта, только first_monday_day вычисляем одной строкой.
def is_first_monday_2(date):
    # Сразу вычисляем число первого понедельника
    first_monday_day = [week[0] for week in calendar.monthcalendar(date.year, date.month) if week[0] != 0][0]
    return datetime(date.year, date.month, first_monday_day) == datetime(date.year, date.month, date.day)


# Вариант 3 (используем только datetime)
# Решение подсмотрено тут https://stackoverflow.com/questions/67378357/how-to-calculate-the-first-monday-of-the-month-python-3-3
def find_first_monday(date):
    # Получаем 7 число переданного месяца.
    # С 1 до 7 числа гарантировано есть один понедельник.
    d = datetime(date.year, date.month, 7)
    # Смотрим какой это день недели (0 - это понедельник, 6 - воскресенье).
    offset = -d.weekday()
    # Вычитаем из текущей даты номер дня недели.
    # Пример 1: в январе 2022 года первый понедельник был 3 января.
    #           Сперва мы получили 7 января и вычислили, что это пятница (4 день недели если считать с нуля).
    #           Далее мы из 7 вычитаем 4 и получаем 3. 3 - это дата первого понедельника.
    # Пример 2: в феврале 2022 года первый понедельник был 7 числа.
    #           Сперва мы получили 7 февраля и вычислили, что это понедельник (0 день недели если считать с нуля).
    #           Далее мы из 7 вычитаем 0 и получаем 7. 7 - это дата первого понедельника.
    # Пример 3: в августе 2022 года первый понедельник был 1 числа.
    #           Сперва мы получили 7 августа и вычислили, что это воскресенье (6 день недели если считать с нуля).
    #           Далее мы из 7 вычитаем 6 и получаем 1. 1 - это дата первого понедельника.
    first_monday = d + timedelta(offset)
    # Финальное сравнение
    return datetime(date.year, date.month, date.day) == first_monday

# Выводим финальный результат с помощью одной из фукнций
print(is_first_monday_2(date))"""
