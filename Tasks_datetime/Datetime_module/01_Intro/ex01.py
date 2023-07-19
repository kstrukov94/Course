"""ДЕНЬ НЕДЕЛИ"""
# Напишите программу, которая принимает из аргументов командной строки три параметра: год, месяц и день,
# а затем выводит на русском языке день недели для переданной даты.
#
# Пример использования (2 апреля 2020):
# > python program.py 2020 4 2
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

year, month, day = map(int, sys.argv[1:])
weekday = date(year, month, day).weekday()
print(weekday_rus[weekday])

# import sys
# from datetime import date
#
# # Список дней.
# DAYS = ["понедельник", "вторник", "среда", "четверг",
#         "пятница", "суббота", "воскресенье"]
#
# # Получаем данные.
# year = int(sys.argv[1])
# month = int(sys.argv[2])
# day = int(sys.argv[3])
#
# # Формируем дату.
# d = date(year, month, day)
#
# # Выводим день недели.
# print(DAYS[d.weekday()])