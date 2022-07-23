# УДАЛЯЕМ МАРКУ
# В программе ниже создан список с марками автомобилей.
# Расширьте код так, чтобы программа принимала из первого аргумента командной строки индекс элемента списка,
# а затем удаляла элемент, расположенный по этому индексу.
#
# Пример использования:
# > python program.py 1
# > ['BMW', 'Mercedes', 'Lada', 'Nissan', 'Audi']

marks = ["BMW", "Toyota", "Mercedes", "Lada", "Nissan", "Audi"]

import sys
index = int(sys.argv[1])
del marks[index]
print(marks)

# import sys
#
# # Не забываем преобразовать к int.
# index = int(sys.argv[1])
#
# marks = ["BMW", "Toyota", "Mercedes", "Lada", "Nissan", "Audi"]
# 
# # Для удаления по индексу, используется метод pop.
# marks.pop(index)
#
# print(marks)