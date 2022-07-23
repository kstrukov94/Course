# НАЛИЧИЕ АВТОМОБИЛЯ
# Ниже в редакторе содержится список cars с автомобилями.
# Напишите программу, которая принимает из аргументов командной строки два параметра:
# марку и модель автомобиля, а затем выводит True если автомобиль есть в списке и False в противном случае.
#
# Пример использования:
# > python program.py Ford Focus
# > True

cars = ["Ford Focus", "Skoda Octavia", "Toyota Prius",
        "Hyundai Solaris", "Volkswagen Polo", "Skoda Rapid"]

import sys
vendor, model = sys.argv[1], sys.argv[2]
print("{:s} {:s}".format(vendor, model) in cars)