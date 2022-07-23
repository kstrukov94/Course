# УЛУЧШЕННОЕ СРАВНЕНИЕ ДОХОДОВ
# В прошлой задаче вы вычитали доход второго года из первого.
# Теперь усовершенствуйте программу так, чтобы в каком бы порядке не передавались годы,
# всегда будет вычитаться доход раннего года из более позднего.

# То есть если передается 2020 и 2017, то будет вычитаться доход 2017 из 2020,
# и точно такое же действие будет если поменять данные местами.
#
# Пример использования:
# > python program.py 2021 2020
# > 88000
# > python program.py 2020 2021
# > 88000

revenue = {
    2017: 123_000,
    2018: 127_000,
    2019: 134_000,
    2020: 201_000,
    2021: 289_000
}
import sys
years = [int(sys.argv[1]), int(sys.argv[2])]
result = revenue.get(max(years), 0) - revenue.get(min(years), 0)
print(result)


# import sys
# year1, year2 = int(sys.argv[1]), int(sys.argv[2_Strings])
# revenues = [revenue.get(year1, 0), revenue.get(year2, 0)]
# result = max(revenues) - min(revenues)
# print(result)
