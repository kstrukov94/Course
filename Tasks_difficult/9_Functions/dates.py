"""#87: ВЧЕРА И ЗАВТРА
Сложность: 4 из 10
Написать функцию dates, которая принимает аргумент-строку date (текущий день) и возвращает кортеж из двух элементов:
предыдущий день и следующий день, относительно переданного.

Аргумент date передается в виде строки формата ДД.ММ.ГГГГ.
Возвращаемый кортеж также содержит даты в виде строк в формате ДД.ММ.ГГГГ.
Функция должна учитывать високосные годы.

Пример использования функции:
result = dates('12.03.2016')
print(result)
('11.03.2016', '13.03.2016')
"""

from datetime import date, timedelta


def dates(*date_args, **date_kwargs):
    # TODO упростить код
    day, month, year = map(int, date_kwargs['date'].strip().split('.')) if date_kwargs else map(int, date_args[0].strip().split('.'))
    this_date = date(year, month, day)
    next_day = this_date + timedelta(1)
    prev_day = this_date - timedelta(1)
    return f'{prev_day:%d.%m.%Y}', f'{next_day:%d.%m.%Y}'


print(dates('12.03.2016'))


# # Вариант 1 (без использования сторонних библиотек)
# # Количество дней в месяцах для обычного года и для високосного.
# DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# DAYS2 = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#
# def is_leap_year(year):
#     """
#     Вычисляем високосный год или нет.
#     Функция из прошлых задач.
#     """
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#         else:
#             return True
#
#     return False
#
#
# def dates(date):
#     """
#     Функция возрващает дату вчерашнего и завтрашнего дня.
#     Без использования сторонних библиотек.
#     """
#     # Получаем данные, разбиваем date на три части и сразу помещаем их временные.
#     day, month, year = date.split(".")
#
#     # Преобразовываем к целым
#     day, month, year = int(day), int(month), int(year)
#
#     # Вычисляем високосный год или нет с помощью дополнительной функции.
#     if is_leap_year(year):
#         days = DAYS2
#     else:
#         days = DAYS
#
#     # Высчитываем числа в зависимости от месяца и текущего числа.
#     # Тут простая арифметика.
#     prev_day, prev_month, prev_year = day, month, year
#     if day == 1:
#         if month == 1:
#             prev_year = year - 1
#             prev_month = 12
#         else:
#             prev_month = month - 1
#
#         prev_day = days[prev_month]
#     else:
#         prev_year = year
#         prev_month = month
#         prev_day = day - 1
#
#     next_day, next_month, next_year = day, month, year
#     if day == days[month]:
#         if month == 12:
#             next_year = year + 1
#             next_month = 1
#         else:
#             next_month = month + 1
#         next_day = 1
#     else:
#         next_year = year
#         next_month = month
#         next_day = day + 1
#
#     # Получаем результат с помощью форматирования
#     prev_date = "{:02d}.{:02d}.{:02d}".format(prev_day, prev_month, prev_year)
#     next_date = "{:02d}.{:02d}.{:02d}".format(next_day, next_month, next_year)
#     return prev_date, next_date
#
#
# # Вариант 2
# # Испольузем встроенную библиотеку datetime.
# # Подробнее о работе с этой библиотекой в мини-курсе Дата и время в Python 3.
# from datetime import datetime, timedelta
#
#
# def dates(date):
#     # Парсим строку и преобразовываем её в дату
#     date = datetime.strptime(date, "%d.%m.%Y")
#
#     # Вычисляем прошлый и следующий день
#     prev_date = date - timedelta(days=1)
#     next_date = date + timedelta(days=1)
#
#     # Возвращаем результат преобразова его к
#     return prev_date.strftime("%d.%m.%Y"), next_date.strftime("%d.%m.%Y")
