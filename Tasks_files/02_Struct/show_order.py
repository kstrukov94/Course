"""#251: ЗАКАЗ"""
"""Сложность: 2 из 10
В двоичном файле order.data содержится информация о заказе в интернет магазине. 
Файл имеет следующую структуру:

Номер заказа – целое число типа integer.
Дата – строка вида ГГГГ-ММ-ДД.
Товар – строка до 70 байтов.
Количество – целое число типа short.
Цена единицы товара – вещественное число типа float.
Напишите программу show_order.py, 
которая прочитает данные этого файла и выведет в консоль информацию о заказе в следующем виде: 
Заказ <NUM> от <DATE> на сумму <SUM>. 

Где <NUM> – это номер заказа, <DATE> – дата в формате ДД.ММ.ГГГГ, 
а <SUM>– стоимость всего заказа. 

Стоимость нужно вывести с двумя знаками после точки.

Двоичный файл, на котором можно потренироваться: order.data

Пример использования (на основе тестового файла):
> python show_order.py
> Заказ 43 от 15.01.2017 на сумму 15297.00"""


import struct
from datetime import datetime as dt

with open("order.data", "rb") as order_file:
    order = order_file.read()
    order_n, order_date, order_product, order_quantity, order_price = struct.unpack('i10s70shf', order)

    order_date = dt.strptime(order_date.decode(), "%Y-%m-%d")
    order_date = order_date.strftime("%d.%m.%Y")

    order_sum = order_quantity * order_price

    # order_product_name = order_product.decode().rstrip('\x00')

    print(f"Заказ {order_n} от {order_date} на сумму {order_sum:.2f}")
