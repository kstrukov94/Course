"""#255: СПИСОК ПРОДУКТОВ"""
"""Сложность: 4 из 10
Напишите программу products.py, которая будет создавать двоичный файл products.data 
и записывать в него список товаров для покупки.

Сперва в файле должно идти количество товаров представленное беззнаковым типом short (unsigned short), 
а после список товаров в алфавитном порядке. На каждый товар можно выделать не более 60 байтов.

Список товаров, которые должны быть в файле: свинина, майонез, морковь, свекла, сыр, чеснок, масло, картофель.

Пример двоичного файла из 3-х продуктов (свинина, майонез, морковь): products.data"""

import struct


products = [
    "свинина",
    "майонез",
    "морковь",
    "свекла",
    "сыр",
    "чеснок",
    "масло",
    "картофель"
]


with open("products.data", "wb") as products_file:
    products_enc = products[:]
    products_enc.sort()
    for n in range(products.__len__()):
        products_enc[n] = products_enc[n].encode()
    products_file.write(struct.pack(f"H{'60s' * products.__len__()}", products.__len__(), *products_enc))


