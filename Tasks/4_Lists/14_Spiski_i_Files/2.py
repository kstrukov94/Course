# НАСЕЛЕНИЕ, ЧАСТЬ 3_Files
# Рядом с программой находится файл population.txt с населением России за разные годы.
# В первой строке содержится год, с которого начали заполнять этот файл.
# В следующих строках хранятся непосредственно данные о населении — каждое значение с новой строки и каждое отвечает за определенный год.
#
# Например, в следующем файле первая строка содержит год — 2004, соответственно население 144168205 относится к 2004 году, 143474219 к 2005 и тд.
#
# 2004
# 144168205
# 143474219
# 142753551
# Напишите программу, которая принимает из аргументов командной строки год, а затем выводит население этого года.
#
# Пример использования:
# > python program.py 2006
# > 142753551

import sys
year = int(sys.argv[1])
population_file = open("2_population.txt")
population_list = population_file.readlines()
start_year = int(population_list[0].strip())
population_result = population_list[year-start_year+1]
print(population_result)

# import sys
# # Открываем файл
# population_file = open("population.txt")
#
# # Сохраняем данные в список.
# all_data = population_file.readlines()
#
# # Получаем начальный год.
# start_year = int(all_data[0])
#
# # Вычисляем список населения.
# population = all_data[1:]
#
# # Получаем год.
# year = int(sys.argv[1])
#
# # Приводим к индексам списка.
# index = year - start_year
#
# # Выводим результат.
# print(population[index].strip())