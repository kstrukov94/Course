"""ОПОЗДАВШИЕ РАБОТНИКИ"""
# Время прихода работников на работу фиксируется в файле visits.txt, который лежит рядом с программой.
# Информация о каждом сотруднике записывается с новой строки и хранится в формате ID,ЧЧ:ММ:CC,
# где ID — это идентификатор сотрудника (целое число), а ЧЧ:ММ:CC — время его прихода на работу.

# Вот пример одного из таких файлов:
#
# 172,08:56:12
# 6,10:00:00
# 45,08:17:12
# 684,09:00:00
# 12,09:00:01
# 4,09:01:00
# 41,07:00:00
# 61,08:59:59

# Напишите программу, которая анализирует данный файл и выводит ID сотрудников, которые опоздали на работу.
# Опоздавшими считаются работники, которые пришли после 09:00:00.
# Идентификаторы нужно разделить запятыми и вывести в порядке возрастания.

# Пример использования (на основе данных выше):
# > python program.py
# > 4,6,12

from datetime import time

late_ids = []
with open('ex01_visits.txt', 'r', encoding='UTF-8') as file:
    for line in file:

        worker_id, arrival_time = line.strip().split(',')
        worker_id = int(worker_id)

        arr_h, arr_m, arr_s = map(int, arrival_time.split(':'))
        arrival_time = time(hour=arr_h, minute=arr_m, second=arr_s)

        work_time = time(9, 0, 0)
        if arrival_time > work_time:
            late_ids.append(worker_id)

late_ids = map(str, sorted(late_ids))
print(','.join(late_ids))








# late = []
# for line in open('ex01_visits.txt', 'r', encoding='utf-8'):
#     user_id, t = line.split(',')
#     hours, minutes, seconds = map(int, t.split(':'))
#     t = time(hours, minutes, seconds)
#     if t > time(9, 0, 0):
#         late.append(int(user_id))
#
# print(','.join(map(str, sorted(late))))

