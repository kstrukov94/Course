"""АЛКОГОЛЬНАЯ ПРОДУКЦИЯ"""
# В переменной age содержится возраст пользователя, а в hour — текущее время в часах (например, 14).
# Напишите программу, которая проверяет, может ли продавец продать покупателю алкогольную продукцию.
#
# Алкогольную продукцию разрешено продавать с 7 часов утра до 22 часов вечера лицам достигшим 18 лет.
#
# Если продавать можно, то программа должна вывести «Разрешено» иначе «Запрещено».

import sys
import random

age, hour = int(sys.argv[1:])
# age, hour = 5, 16
if hour < 7 or hour > 22:
    print("Запрещено")
elif age < 18:
    print("Запрещено")
else:
    print("Разрешено")


# num = sys.argv[1]
# nums = str(num)
# counter = 0
# for n in nums:
#     if n in "0123456789":
#         counter += 1
#
# print(counter)

# num = sys.argv[1]
# num = 11.0
# nums = list(str(num))
#
# if len(nums) > 2:
#     if not nums[1].isdigit():
#         del nums[2]
#     else:
#         del nums[1]
# elif len(nums) > 1:
#     del nums[1]
#
# print("".join(nums).strip("."))
