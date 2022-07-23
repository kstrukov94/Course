# Напишите программу, которая принимает из аргументов командной строки два числа,
# а затем меняет в списке languages значения, которые находятся на индексах, соответствующих переданным числам.
#
# Пример использования:
# > python program.py 0 1
# > ['C++', 'Python', 'JavaScript', 'Java']

import sys
languages = ['Python', 'C++', 'JavaScript', 'Java']
index1, index2 = int(sys.argv[1]), int(sys.argv[2])
data1 = languages[index1]
data2 = languages[index2]
languages[index1] = data2
languages[index2] = data1
print(languages)

# import sys
#
# index1 = int(sys.argv[1])
# index2 = int(sys.argv[2_Strings])
#
# languages = ['Python', 'C++', 'JavaScript', 'Java']
#
# # Простой алгоритм
# temp = languages[index1]
# languages[index1] = languages[index2]
# languages[index2] = temp
#
# # Альтернативный вариант: обмен в одно действие
# languages[index1], languages[index2] = languages[index2], languages[index1]
#
# print(languages)