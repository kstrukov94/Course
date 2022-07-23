# ИСПРАВЛЯЕМ ОШИБКУ
# Программа ниже должна принимать из аргументов командной строки новую модель автомобиля и добавлять её в конец списка cars.
# Но при написании что-то пошло не так и автомобиль не добавляется. Исправьте ошибку.
#
# Пример использования:
# > python program.py Lada
# > ['BMW', 'Audi', 'Toyota', 'Mazda', 'Lada']

# import sys
#
# new_car = sys.argv[1]
#
# cars = ['BMW', 'Audi', 'Toyota', 'Mazda']
# cars += new_car
# print(new_car)

import sys
new_car = [sys.argv[1]]

cars = ['BMW', 'Audi', 'Toyota', 'Mazda']
cars += new_car
print(cars)

# import sys
# new_car = sys.argv[1]
# cars = ['BMW', 'Audi', 'Toyota', 'Mazda']
# # Помещаем new_car в скобки.
# cars += [new_car]
# # Выводим cars.
# print(cars)