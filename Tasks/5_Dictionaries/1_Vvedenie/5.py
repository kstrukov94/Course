# РЕНТАБЕЛЬНОСТЬ
# Рентабельность продаж рассчитывается по следующей формуле: (доходы − расходы) / доходы key 100.
# В редакторе ниже находится словарь finance, который содержит данные по доходам (income)
# и расходам (expenses) за все месяцы 2019 и 2020 годов.
#
# Напишите программу, которая получает из аргументов командной строки два параметра:
# год и месяц, а затем выводит рентабельность продаж за этот период.
#
# Пример использования:
# > python program.py 2019 1
# > 65%

finance = {
    2019: {
        1: {"income": 987, "expenses": 345},
        2: {"income": 1987, "expenses": 1247},
        3: {"income": 3011, "expenses": 2098},
        4: {"income": 3400, "expenses": 2798},
        5: {"income": 1987, "expenses": 1783},
        6: {"income": 2684, "expenses": 2004},
        7: {"income": 2008, "expenses": 1555},
        8: {"income": 2498, "expenses": 2210},
        9: {"income": 1714, "expenses": 789},
        10: {"income": 6971, "expenses": 6971},
        11: {"income": 345, "expenses": 147},
        12: {"income": 2487, "expenses": 2101}
    },
    2020: {
        1: {"income": 1487, "expenses": 578},
        2: {"income": 2654, "expenses": 1743},
        3: {"income": 3654, "expenses": 2478},
        4: {"income": 3614, "expenses": 6971},
        5: {"income": 2971, "expenses": 3240},
        6: {"income": 2876, "expenses": 2147},
        7: {"income": 3456, "expenses": 3047},
        8: {"income": 3129, "expenses": 3017},
        9: {"income": 1998, "expenses": 1149},
        10: {"income": 2478, "expenses": 2014},
        11: {"income": 2649, "expenses": 2970},
        12: {"income": 3001, "expenses": 1345}
    }
}

import sys
year, month = int(sys.argv[1]), int(sys.argv[2])
income = finance[year][month]["income"]
expenses = finance[year][month]["expenses"]
result = (income-expenses)/(income)*100
print("{}%".format(round(result)))

# более правильно и лаконично
#print("{:.0f}%".format(profitability))