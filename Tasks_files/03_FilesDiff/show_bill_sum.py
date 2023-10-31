"""#415: XML СЧЕТ НА ОПЛАТУ"""
"""Сложность: 2 из 10

В XML файле bill.xml содержится информация о выставленном для оплаты счете.

Напишите программу show_bill_sum.py, 
которая прочитает данные этого файла и выведет в консоль конечную стоимость всех товаров и работ в счете. 
Результат нужно вывести с двумя знаками после точки.

Пример использования (на основе счета выше):
> python show_bill_sum.py
> 4597.20"""

import xml.etree.ElementTree as et

bill = et.parse("bill.xml").getroot()

bill_sum = 0

# Способ №1
# for data in bill:
#     if data.tag == "products":
#         for product in data:
#             bill_sum += int(product.attrib["count"]) * float(product.attrib["price"])

# Способ №2 (iter)
# for data in bill.iter("products"):
#     for product in data:
#         bill_sum += int(product.attrib["count"]) * float(product.attrib["price"])

# Способ №3 (XPath)
for product in bill.findall("./products/product"):
    bill_sum += int(product.attrib["count"]) * float(product.attrib["price"])

print(f"{bill_sum:.2f}")

"""Решение преподавателя"""
"""
import xml.etree.ElementTree as ET
tree = ET.parse("bill.xml")
bill = tree.getroot()

amount = 0
for product in bill.findall("./products/product"):
    amount += float(product.attrib["price"]) * int(product.attrib["count"])

print("{:.2f}".format(amount))
"""
