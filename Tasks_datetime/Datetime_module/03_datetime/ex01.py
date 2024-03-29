"""БУДУЩИЕ ВСТРЕЧИ"""
# В файле calendar.txt, который лежит рядом с программой, содержится информация о встречах.
# Каждая встреча записывается с новой строки и хранится в формате ID,ДД.ММ.ГГГГ ЧЧ:ММ,
# где ID — это идентификатор встречи в календаре, а ДД.ММ.ГГГГ ЧЧ:ММ — дата и время встречи.
#
# Вот пример одного из таких файлов:
#
# 461,06.04.2020 09:00
# 353,06.04.2020 03:15
# 537,05.04.2020 01:00
# 879,06.04.2020 15:15
# 254,05.04.2020 16:30
# 874,05.04.2020 10:30
# 308,06.04.2020 16:30
# 420,06.04.2020 05:30
# 109,04.04.2020 22:15
# 446,05.04.2020 08:00
# Напишите программу, которая анализирует данный файл и выводит ID встреч,
# которые произойдут в будущем (относительно текущего времени).
# Выведите идентификаторы встреч через запятую с пробелом в порядке их следования в файле.
#
# Пример использования (на момент времени 05.04.2020 18:11):
# > python program.py
# > 461, 353, 879, 308, 420

from datetime import datetime as dt

future_meetings_ids = []

with open('ex01_calendar.txt', 'r', encoding='UTF-8') as file:
    now_date = dt.now()
    # now_date = dt(2020, 4, 5, 18, 11)
    for line in file:
        id_raw, datetime_raw = line.strip().split(',')
        compare_date = dt.strptime(datetime_raw, '%d.%m.%Y %H:%M')
        if compare_date > now_date:
            future_meetings_ids.append(id_raw)
print(', '.join(future_meetings_ids))

# f_meetings = []
# now = dt.now()
# with open('ex01_calendar.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         user_id, date = line.strip().split(',')
#         date = dt.strptime(date, '%d.%m.%Y %H:%M')
#         if date > now:
#             f_meetings.append(user_id)
# print(', '.join(f_meetings))
