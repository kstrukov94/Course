"""МАКСИМАЛЬНОЕ ОПОЗДАНИЕ"""
# В прошлом задании вы находили список опоздавших сотрудников, теперь нужно найти сотрудника с максимальным опозданием.
#
# Напишите программу, которая анализирует файл из прошлого задания и выводит идентификатор,
# а также время прихода на работу сотрудника, который опоздал больше всего
#
# Пример использования (на основе данных из прошлого задания):
# > python program.py
# > 6,10:00:00

from datetime import time

latest = tuple()
for line in open('ex01_visits.txt', 'r', encoding='utf-8'):
    user_id, arrival_time = line.split(',')
    hours, minutes, seconds = map(int, arrival_time.split(':'))
    arrival_time = time(hours, minutes, seconds)
    if arrival_time > time(9, 0, 0):
        if not latest or arrival_time > latest[1]:
            latest = user_id, arrival_time

print(f'{latest[0]},{latest[1]}') if latest else print('')

