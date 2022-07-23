# УДАЛЯЕМ МАРКУ, ЧАСТЬ 2_Strings
# В программе ниже создан список с марками автомобилей.
# Расширьте код так, чтобы программа принимала из первого аргумента командной строки название марки, а затем удаляла её из списка.
#
# Пример использования:
# > python program.py Toyota
# > ['BMW', 'Mercedes', 'Lada', 'Nissan', 'Audi']

marks = ["BMW", "Toyota", "Mercedes", "Lada", "Nissan", "Audi"]

import sys
to_remove = str(sys.argv[1])
marks.remove(to_remove)
print(marks)