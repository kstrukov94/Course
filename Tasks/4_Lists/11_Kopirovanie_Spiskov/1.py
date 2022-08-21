# СРЕДНЯЯ ОЦЕНКА
# Во многих видах спорта на соревнованиях работает следующая схема выставления оценок.
# Сперва убирается одна максимальная и минимальная оценка, а уже после рассчитывается среднее значение из оставшихся.
# Это позволяет исключить заниженные и завышенные оценки.
#
# Напишите программу, которая принимает произвольное количество оценок, затем исключает минимум и максимум,
# а после рассчитывает среднее из оставшихся.
# Программа должна вывести список оригинальных оценок, а также среднее с двумя знаками после десятичной точки.
#
# Пример использования:
# > python program.py 10 9 8 7 9 10 9 9 8 9
# > [10, 9, 8, 7, 9, 10, 9, 9, 8, 9] 8.88

# Преобразуем каждый элемент в целое число.
# Элемент функционального программирования, будем изучать в отдельном курсе.
# votes = list(map(int, votes))


import sys

votes = sys.argv[1:]
votes = list(map(int, votes))
votes_sorted = list(sorted(votes.copy()))
del votes_sorted[0]
del votes_sorted[-1]
result = sum(votes_sorted) / len(votes_sorted)
print("{} {:.2f}".format(votes, result))

# import sys
#
# votes = sys.argv[1:]
#
# # Преобразуем каждый элемент в целое число.
# # Элемент функционального программирования, будем изучать в отдельном курсе.
# votes = list(map(int, votes))
#
# # Делаем копию.
# work_votes = votes.copy()
#
# # Сортируем.
# work_votes.sort()
#
# # Убираем крайние значения.
# work_votes = work_votes[1:-1]
#
# # Считаем среднее.
# avg = sum(work_votes) / len(work_votes)
#
# # Выводим список оценок и результат.
# print(votes, "{:.2f}".format(avg))