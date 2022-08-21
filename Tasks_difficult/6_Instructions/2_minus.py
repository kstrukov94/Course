"""#28: СУММА ОТРИЦАТЕЛЬНЫХ ЧИСЕЛ"""
# Сложность: 1 из 10
# В файле numbers.txt в одну строку через пробелы записаны целые числа.
# Напишите программу minus.py, которая считает и печатает сумму всех отрицательных чисел из файла.
#
# Пример файла numbers.txt:
# 1 2 -3 4 -5 6 7
# Пример использования:
# > python minus.py
# -8

result = 0
for line in open("numbers.txt", "r", encoding="utf-8"):
    for num in line.split():
        if int(num) < 0:
            result += int(num)
print(result)

# # Открываем файл, читаем все данные, отсекаем лишние пробелы и разбиваем по пробелу.
# # После выполнения в numbers будет храниться список строк, содержащих цифры.
# numbers = open("numbers.txt", "r").read().strip().split(" ")
# summa = 0
#
# # Проходимся по списку.
# for num in numbers:
#     # Преобразуем каждое значение к целому числу.
#     num = int(num)
#     # Сравниваем с нулем и если число меньше, то увеличиваем сумму.
#     if num < 0:
#         summa += num
#
# print(summa)
#
#
# # <b>Вариант 2</b> (продвинутый) - решение в одну строку:
# # Используем функциональное программирование (ФП).
# # Если вам интересно как это работает, то рекомендуем пройти мини-курс по ФП.
# print(sum(filter(lambda x: x < 0, map(int, open("numbers.txt", "r").read().strip().spl