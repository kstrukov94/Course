# ПЛАН ПО ПРОДАЖАМ
# В редакторе ниже находится словарь plans, который содержит данные о выполнение ежемесячных планов по продажам.
# Ключом словаря является год, а значение — это список из 12 элементов, по элементу на каждый месяц.
# True означает, что план в текущем месяце выполнен, а False, что нет.
#
# Напишите программу, которая первым аргументом командной строки получает год,
# а затем выводит процент выполнения планов в этом году.
#
# Данные нужно округлить и добавить к ним символ процента.
#
# Пример использования:
# > python program.py 2018
# > 67%

plans = {
    2017: [False, False, False, False, False, False, False, False, False, False, False, False],
    2018: [True, True, False, False, True, False, True, True, False, True, True, True],
    2019: [True, True, True, True, True, False, True, True, False, True, True, True],
    2020: [True, True, True, True, True, False, True, True, False, False, False, False],
    2021: [True, True, True, True, True, True, True, True, True, True, True, True]
}

import sys
year = int(sys.argv[1])
plans_true = plans.get(year).count(1)
plans_all = len(plans.get(year))
result = round(plans_true / plans_all * 100)
print("{:d}%".format(result))

