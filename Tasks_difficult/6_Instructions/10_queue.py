"""#52: ДОРОГУ СТАРШИМ"""
# Сложность: 4 из 10
# В очереди на кассе стоит несколько человек разного возраста.
# Кассир решила обслужить старшего покупателя первым.
#
# Напишите программу queue.py, которая принимает первым аргументом командной строки последовательность чисел разделенных пробелами,
# а после ставит самое большое число на первое место и выводит новую очередь на экран.
#
# Пример использования:
# > python queue.py "34 12 53 14"
# 53 34 12 14

import sys
queue = list(map(int, sys.argv[1].split()))
queue.insert(0, queue.pop(queue.index(max(queue))))
print(" ".join(list(map(str, queue))))

# import sys
#
# queue_txt = sys.argv[1]
#
# # Преобразовываем текстовую очередь в список чисел.
# queue = []
# for p in queue_txt.split(" "):
#     queue.append(int(p))
#
# # Получаем максималный возраст и вычисляе его индекс
# max_age = max(queue)
# max_age_index = queue.index(max_age)
#
# # Удаляем элемент с максимальным возрастом по индексу
# queue.pop(max_age_index)
#
# # Вставляем максимальный возрас в начало очереди
# queue.insert(0, max_age)
#
# # Снова переводим числовой список в текстовый
# queue_txt = []
# for p in queue:
#     queue_txt.append(str(p))
#
# # Выводим итоговый результат
# print(" ".join(queue_txt))
#
#
# # Вариант 2 (продвинутый) - с использование функционального программирования
# import sys
#
# # Получаем список возрастов преобразовав каждый элемент к целому числу
# queue = list(map(int, sys.argv[1].split(" ")))
#
# # Перемещаем максимальный элемент в начало.
# queue.insert(0, queue.pop(queue.index(max(queue))))
#
# # Выводим результат предварительно преобразовав каждый элемент к строке
# print(" ".join(map(str, queue)))
