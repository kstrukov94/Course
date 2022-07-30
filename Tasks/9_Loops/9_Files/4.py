"""ЛУЧШИЙ МЕНЕДЖЕР ПО ПРОДАЖАМ"""
# Рядом с программой находится файл sales.txt со списком продаж менеджеров рекламного агенства.
# Каждая продажа в этом файле записана в отдельной строке и состоит из двух частей:
# Менеджер<tab>Сумма, где Менеджер — это фамилия менеджера, <tab> — символ табуляции, который разделяет данные,
# а Сумма — количество денег, которое менеджер заработал.
#
# Пример файла:
#
# Иванов С. И.	1000
# Петров И. Л.	3000
# Иванов С. И.	3000
# Сидоров Н. В.	3500
# Обратите внимание, что некоторые менеджеры сделали несколько продаж, например Иванов С. И.
#
# Напишите программу, которая проходит по всем операциям в файле sales.txt, а после выводит данные менеджера,
# который суммарно заработал самое больше количество денег.
#
# Данные нужно вывести в следующем формате: Менеджер, Сумма продаж.
#
# Пример работы программы:
# > python program.py
# Иванов С. И., 4000

managers_list = []
sales_list = []
for line in open("4_sales.txt", "r", encoding="utf-8"):
    manager_name, sales_amount = line.strip().split("	")
    if manager_name not in managers_list:
        managers_list.append(manager_name)
        sales_list.append([manager_name, int(sales_amount)])
    else:
        for manager in sales_list:
            if manager[0] == manager_name:
                manager[1] += int(sales_amount)

sales_max = 0
manager_sales_max = None
for manager in sales_list:
    if manager[1] > sales_max:
        sales_max = manager[1]
        manager_sales_max = manager[0]
# print(managers_list)
# print(sales_list)
print(f"{manager_sales_max}, {sales_max}")

# sales_file = open("4_sales.txt")
#
# # Словарь для хранения сгруппированных данных по всем менеджерам.
# managers = {}
#
# # Переменные для хранения текущего лучшего менеджера и его результата.
# best_manager = None
# best_result = 0
#
# for sale in sales_file:
#     # Получаем данные.
#     manager, amount = sale.strip().split("\t")
#
#     # Заполняем словарь.
#     if manager not in managers:
#         managers[manager] = 0
#     managers[manager] += int(amount)
#
#     # Проверяем лучшего менеджера.
#     if best_result < managers[manager]:
#         best_manager = manager
#         best_result = managers[manager]
#
# print(f"{best_manager}, {best_result}")
