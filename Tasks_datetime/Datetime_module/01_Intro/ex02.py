"""ЭТОТ ДЕНЬ В ДРУГОМ ГОДУ"""
# Напишите программу, которая принимает из аргументов командной строки год,
# а затем выводит день недели, который был в переданном году в сегодняшний день.
# Например, если сегодня 2 апреля, а в программу передается год 2009,
# то она должна вывести день недели, который соответствует дате 2 апреля 2009 года.
#
# Пример использования (с учетом, что сегодня 2 апреля):
# > python program.py 2009
# > четверг


from datetime import date
import sys

weekday_rus = {
    0: 'понедельник',
    1: 'вторник',
    2: 'среда',
    3: 'четверг',
    4: 'пятница',
    5: 'суббота',
    6: 'воскресенье'
}

inp_year = int(sys.argv[1])
date_inp_year = date.today().replace(inp_year)
print(weekday_rus[date_inp_year.weekday()])






# year = int(sys.argv[1])
# weekday = date.today().replace(year=year).weekday()
# print(weekday_rus[weekday])














