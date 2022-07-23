# НОВЫЙ АВТОМОБИЛЬ
# В программе ниже создан список с марками автомобилей.
# Расширьте код так, чтобы программа принимала из первого аргумента командной строки еще одну марку, а затем добавляла её в список marks.
#
# Пример использования:
# > python program.py Nissan
# > ['BMW', 'Toyota', 'Mercedes', 'Nissan']

marks = ["BMW", "Toyota", "Mercedes"]

import sys
marks.append(sys.argv[1])

print(marks)

