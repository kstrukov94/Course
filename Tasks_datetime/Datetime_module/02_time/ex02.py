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

latest = None
for line in open('ex01_visits.txt', 'r', encoding='utf-8'):
    user_id, t = line.split(',')
    hours, minutes, seconds = map(int, t.split(':'))
    t = time(hours, minutes, seconds)
    if t > time(9, 0, 0):
        if latest is None:
            latest = [int(user_id), t]
        elif t > latest[1]:
            latest = [int(user_id), t]

print(f'{latest[0]},{latest[1]}') if latest is not None else print('')

