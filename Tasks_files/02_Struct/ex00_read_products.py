import struct

with open("ex00_products.data", "rb") as products_file:
    products = products_file.read()
    """ достаем первый товар
    p1 = products[:56]
    p1_name, p1_count, p1_price = struct.unpack('50shf', p1)
    print(
        p1_name.decode().rstrip('\x00'),
        p1_count,
        round(p1_price, 2)
    )"""
    # считываем универсальным способом
    products_in_file = int(len(products) / 56)
    for i in range(products_in_file):
        p = products[i * 56: i * 56 + 56]
        p_name, p_count, p_price = struct.unpack('50shf', p)
        print(
            p_name.decode().rstrip('\x00'),
            p_count,
            f'{p_price:.2f}'
        )

