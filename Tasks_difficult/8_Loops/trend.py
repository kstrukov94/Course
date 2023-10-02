""" #33: САМЫЙ ПРОДОЛЖИТЕЛЬНЫЙ ТРЕНД
Сложность: 7 из 10
Написать программу trend.py, которая получает в виде строки набор целых чисел разделенных пробелами,
вычисляет самый продолжительный тренд из этих чисел и выводит его на экран.

Тренд в данной задаче — это возрастающая или убывающая последовательность чисел (включая повторяющиеся значения).

Исходя из определения, в одной последовательности чисел может быть несколько трендов,
а также одно и то же число может попадать сразу в два тренда.
Например, из последовательности 1 2 3 4 4 3 2 можно выделить два тренда 1 2 3 4 4 и 4 4 3 2
— четверки попадают сразу в оба тренда.
Нам нужно получить самую продолжительную (длинную) последовательность, то есть 1 2 3 4 4.

Если самых продолжительных трендов будет несколько, то нужно вывести первый.

Пример использования:
> python trend.py "1 2 3 4 4 3 2"
1 2 3 4 4
"""


import sys


# создаем список для чтения и заполняем его
input_nums = list(map(int, sys.argv[1].split(' ')))

# создаем 2 списка trend для итогового сравнения и 2 списка temp для промежуточных расчетов
trend_up = []
trend_down = []
temp_up = []
temp_down = []
# для подсчета, какой из трендов был первый
trend_counter = 0

prev_num = input_nums[0]

# проходимся по изначальному списку и заносим в список temp число, если он соответствует условию
for num in input_nums[1:]:
    # проверка для возрастающей последовательности
    if num >= prev_num:
        # если temp новый, то захватываем предыдущее число
        if not temp_up:
            temp_up.append(prev_num)
        temp_up.append(num)
    # если temp больше либо равен trend, то заменяем его на более длинный (актуальный) и очищаем temp
        if len(temp_up) > len(trend_up):
            trend_up = (temp_up[:], trend_counter)
            trend_counter += 1
    # если меньше - чистим temp, все изменения все равно сохранены
    else:
        temp_up.clear()

    # проверка для убывающей последовательности
    if num <= prev_num:
        if not temp_down:
            temp_down.append(prev_num)
        temp_down.append(num)
        if len(temp_down) > len(trend_down):
            trend_down = (temp_down[:], trend_counter)
            trend_counter += 1
    else:
        temp_down.clear()

    prev_num = num

# сравниваем trend и выводим самый длинный, с учетом условия первоочередности
if len(trend_up[0]) == len(trend_down[0]):
    best_trend = ' '.join(map(str, trend_up[0])) if trend_up[1] < trend_down[1] \
        else ' '.join(map(str, trend_down[0]))
else:
    best_trend = ' '.join(map(str, trend_up[0])) if len(trend_up[0]) > len(trend_down[0]) \
        else ' '.join(map(str, trend_down[0]))
print(best_trend)

# TODO просмотреть и изучить решения преподавателя и учеников