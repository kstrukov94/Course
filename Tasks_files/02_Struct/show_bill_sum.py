import struct

# goods = []
total_price = 0
with open("bill.data", "rb") as bill_file:
    bill = bill_file.read()
    bill_num, bill_data, goods_in_bill = struct.unpack('h10sh', bill[:struct.calcsize('h10sh')])

    # проходим циклом по каждому товару и добавляем к общей сумме
    for n in range(0, goods_in_bill):
        name, quantity, price = struct.unpack(
            f'{"100shf"}', bill[
                           struct.calcsize('h10sh') + struct.calcsize('100shf') * n:
                           struct.calcsize('h10sh') + struct.calcsize('100shf') + struct.calcsize('100shf') * n
                           ])
        # любопытства ради попробовал сгрупировать в список
        # goods.append([name.decode().rstrip("\x00"), quantity, price])
        total_price += price * quantity

# print(goods)
print(f"{total_price:.2f}")
