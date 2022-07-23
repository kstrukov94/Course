"""ЗАПОЛНЯЕМ ПРОПУСКИ"""
# Иногда данные в программу попадают с пропусками и одна из стратегий нормализации данных — это заполнение пропусков предыдущими значениями.
#
# Напишите программу, которая принимает из аргументов командной строки набор данных,
# среди которых встречаются пропуски обозначенные словом null. Нужно заменить эти пропуски предшествующими значениями.
#
# Если перед null значений не было, то изменять null не нужно.
# Выведите итоговую последовательность в командную строку (терминал).
#
# Пример использования:
# > python program.py null null 2017 null 2019 null
# > null null 2017 2017 2019 2019

import sys
data = sys.argv[1:]
prev_d = "null"
data_result = []
for d in data:
    if d != "null":
        data_result.append(d)
    elif d == "null" and prev_d != "null":
        data_result.append(prev_d)
    else:
        data_result.append(d)
    prev_d = data_result[-1]
print(" ".join(data_result))

# import sys
# values = sys.argv[1:]
#
# # Список с результатом.
# result = []
# prev_value = None  # Предыдущее значение
#
# # Запускаем цикл.
# for value in values:
#     # Если текущее значение - это null и есть предыдущее значение prev_value
#     # то добавляем это значение в результирующий список.
#     # Если данные идут так "2016 null", то предыдущее значение - это 2016,
#     # И будет добавлено ['2016', '2016']
#     if value == "null":
#         if prev_value:
#             result.append(prev_value)
#         else:
#             # Если предыдущего значения нет, то просто добавляем null.
#             # Это для случаев, когда данные начинаются с null:
#             # 'null null 2016' -> ['null', 'null', '2016']
#             result.append(value)
#     else:
#         # Если текущее значение не null и оно не равно предыдущему,
#         # то обновляем предыдущее.
#         if prev_value != value:
#             prev_value = value
#         # Вставляем предыдущее значение, которое также будет являться текущим,
#         # если сработало условие выше.
#         result.append(prev_value)
#
# print(" ".join(result))
#
# # Вариант 2_Strings. Без использования дополнительных списков.
# # Делаем все замены "на месте"
# import sys
# values = sys.argv[1:]
#
# i = 1
# while i < len(values):
#     value = values[i]
#     if value == "null":
#         values[i] = values[i - 1]
#     i += 1
#
# print(" ".join(values))
#
#
# # Вариант 3_Files. Сложный.
# # Использует оператор := из Python 3_Files.8 (в нашей системе не сработает)
# # Приводится только для примера, в реальности я бы так не решал.
# # За основу взят код из обсуждения https://shultais.education/lms/courses/python-3/1494?thread=3400
# import sys
#
# # Предыдущее значение.
# prev_value = 'null'
#
# # Сразу генерируем итоговый результат.
# result = [prev_value := value if value not in (prev_value, 'null') else prev_value for value in sys.argv[1:]]
#
# # Выводим данные.
# print(" ".join(result))