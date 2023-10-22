import struct

products = [
    ["Стиральный порошок Tide", 12, 93.40],
    ["Кодниционер Ariel", 7, 87.22]
]

with open('ex00_products.data', 'wb') as products_file:
    for product in products:
        product = struct.pack('50shf', product[0].encode(), product[1], product[2])
        # либо целиком *product и отдельно к каждой строке в списке применить .encode()
        products_file.write(product)




"""name = "Стиральный порошок Tide"
count = 12
price = 93.40

with open('ex00_products.data', 'wb') as products_file:
    product = struct.pack('50shf', name.encode(), count, price)
    products_file.write(product)
"""