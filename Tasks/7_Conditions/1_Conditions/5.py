"""ЦЕНЫ НА 99"""
# Напишите программу, которая первым аргументом командной строки принимает цену товара,
# а затем, если цена оканчивается на 99, увеличивает её на единицу.
# В остальных случаях цену менять не нужно.
#
# В конце программа должна вывести итоговую цену товара.
#
# Пример использования:
# > python program.py 121
# > 121
# > python program.py 199
# > 200

import sys

product_price = int(sys.argv[1])
if product_price % 100 == 99:
    product_price += 1
print(product_price)
