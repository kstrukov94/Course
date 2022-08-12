"""ДИАПАЗОН СТРАНИЦ ПРИ ПЕЧАТИ"""
# При отправке документов на печать, некоторые программы позволяют задавать как отдельные страницы,
# так и диапазоны страниц (1,3,7-9):

# Номера отдельных страниц и диапазонов разделяются запятыми, а диапазоны имеют формат A-B,
# где A — это начальное значение страницы, а B — конечная страница, которую также нужно напечатать.
#
# Напишите программу, которая принимает строку с номерами отдельных страниц и диапазонами,
# а затем выводит номера отдельных страниц, которые нужно напечатать.
# Номера не должны повторяться и должны быть отсортированы в порядке увеличения.
#
# Пример работы программы:
# > python program.py "1,3,5-8,7"
# 1,3,5,6,7,8

import sys

pages = sys.argv[1].split(",")
result_pages = []
for n in pages:
    if '-' in n:
        start = int(n[0])
        end = int(n[-1]) + 1
        for i in range(start, end):
            result_pages.append(int(i))
    else:
        result_pages.append(int(n))
result_pages.sort()
result_pages = list(set(result_pages))

p = 0
for l in result_pages:
    result_pages[p] = str(l)
    p += 1
print(",".join(result_pages))

# import sys
#
# pages = sys.argv[1]
#
# # Список страниц для печати
# pages_list = []
#
# for element in pages.split(","):
#     # Поиск отдельных страниц.
#     if element.isdigit():
#         if int(element) not in pages_list:
#             pages_list.append(int(element))
#     # Иначе диапазон.
#     else:
#         # Получаем начальное и конечное значения.
#         start, end = element.split("-")
#         # Получаем список страниц
#         for page in range(int(start), int(end) + 1):
#             if page not in pages_list:
#                 pages_list.append(page)
#
# # Сортируем список.
# pages_list.sort()
#
# # Обратно преобразуем к строке
# for i in range(len(pages_list)):
#     pages_list[i] = str(pages_list[i])
#
# # Финальный вывод.
# print(",".join(pages_list))
#
#
# #
# # Альтернативный вариант
# #
#
# import sys
#
# pages = sys.argv[1]
#
# # Список страниц для печати
# pages_list = []
#
# for element in pages.split(","):
#     # Поиск отдельных страниц.
#     if element.isdigit():
#         pages_list.append(int(element))
#     # Иначе диапазон.
#     else:
#         # Получаем начальное и конечное значения.
#         start, end = element.split("-")
#         # Расширяем список страниц.
#         pages_list.extend(list(range(int(start), int(end) + 1)))
#
# # Убираем дубли с помощью множеств.
# pages_list = list(set(pages_list))
#
# # Сортируем список.
# pages_list.sort()
#
# # Обратно преобразуем к строке с помощью enumerate.
# for i, _ in enumerate(pages_list):
#     pages_list[i] = str(pages_list[i])
#
# # Финальный вывод.
# print(",".join(pages_list))
