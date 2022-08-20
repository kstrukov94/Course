"""ОШИБКИ В КЛАССЕ"""
# В редакторе ниже начинающий программист создал класс House для работы с домами.
# Изначально планировалось, что объект класса будет содержать два атрибута: цену (price) и площадь (square) выставленные в 0.
# Однако при запуске кода разработчик получил ошибку, которую не смог исправить.
#
# Внесите изменения в класс, чтобы код заработал.
#
# Пример использования класса:
# house = House()
# print(house.price)
# 0
# print(house.square)
# 0
# house.price = 1000000
# print(house.price)
# 1000000

class House:
    def __init__(self):
        self.price = 0
        self.square = 0

house = House()
print(house.price)

print(house.square)

house.price = 1000000
print(house.price)
