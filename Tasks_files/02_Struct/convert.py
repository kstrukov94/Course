"""#256: СПОРТИВНОЕ ПИТАНИЕ"""
"""Сложность: 6 из 10
В файле sport_food.csv, который находится в папке с программой, содержится список товаров спортивного питания. 
Напишите программу convert.py для преобразования данных из CSV файла в двоичный файл sport_food.bin.

Информация в CSV файле хранится в кодировке windows-1251. Первой строкой идут имена столбцов – название, вес, стоимость. 
Данные разделены запятыми, а все значения заключены в двойные кавычки.

В двоичном файле сперва должно идти количество товаров представленное беззнаковым типом int (unsigned int), 
а после список товаров в том же порядке, что и в CSV файле. 
Каждый товар должен быть представлен форматом 100sHH, что соответствует имени, весу и стоимости. 
Имя товара должно быть записано в кодировке UTF-8.

Пример CSV файла из 3-х товаров: sport_food.csv

Пример двоичного файла, который получается на основе тестового CSV: sport_food.bin"""

import csv
import struct

with open("sport_food.csv", "r", encoding="windows-1251") as sport_food_csv:
    food = csv.DictReader(sport_food_csv)
    goods_quantity = 0
    for peace in food:
        goods_quantity += 1

    # перемещаем укзаатель ридера в начало файла (автоматически ридер этого не делает)
    sport_food_csv.seek(0)
    # пропукскаем первую итерируемую строку с заголовками
    next(sport_food_csv)

    with open("sport_food.bin", "wb",) as sport_food_bin:
        sport_food_bin.write(struct.pack('I', goods_quantity))
        for peace in food:
            name, weight, price = peace["Название"].encode("utf-8"), peace["Вес"], peace["Стоимость"]
            sport_food_bin.write(struct.pack('100sHH', name, int(weight), int(price)))




"""Решение преподавателя"""

"""import struct, csv

# Открываем CSV файл для чтения
with open("sport_food.csv", "r", encoding='windows-1251') as sport_food_file:

    # Подключаем CSV файл
    food_reader = csv.DictReader(sport_food_file, delimiter=',', quotechar='"')

    # Сперва нужно узнать количество товаров, поэтому проходим по всему CSV файлу
    # и сохраняем данные в список
    products = []
    for row in food_reader:
        products.append(row)

    # Открываем файл в режиме двоичной записи
    with open("sport_food.bin", "wb") as products_file:

        # Записываем количество продуктов
        count = struct.pack("I", products.__len__())
        products_file.write(count)

        # Записываем сами продукты
        for product in products:
            product = struct.pack(
                "100sHH", 
                product["Название"].encode(), 
                int(product["Вес"]), 
                int(product["Стоимость"])
            )
            products_file.write(product)"""
