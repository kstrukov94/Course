"""#1204: ОТЧЕТ ПО СЧЕТАМ"""
# Сложность: 5 из 10
# Вы уже вычисляли баланс каждого счета по отдельности. Теперь время построить отчет по всем счетам банка.
#
# Напишите программу, которая проходит по всем операциям в файле bank.txt, а после выводит все счета и баланс каждого счета.
#
# Данные нужно вывести в следующем формате:
# Счет1 Баланс1;Счет2 Баланс2;Счет N; Баланс N.
# То есть счета между собой разделены точкой с запятой, а каждый счет по отдельности содержит свой номер и баланс, разделенные пробелом.
#
# Счета нужно выводить в порядке увеличения баланса (см. пример отчета ниже).
#
# Обратите внимание, что файле есть счет 000 — это внутренний счет банка, его выводить не надо:
#

# Пример отчета (на основе данных из условия):
# > python program.py
# 789 -300;456 -100;123 600
import operator

accounts = {}
# читаем строки
for line in open("bank.txt", "r", encoding="utf-8"):
    acc_from, acc_to, amount = line.strip().split(";")

    # создаем аккаунты, которые не встречались в листе
    if acc_from not in accounts:
        accounts.update({acc_from: 0})
    if acc_to not in accounts:
        accounts.update({acc_to: 0})

    # проводим транзакции
    accounts.update({acc_from: accounts.pop(acc_from) - int(amount)})
    accounts.update({acc_to: accounts.pop(acc_to) + int(amount)})

# убираем из печати банк
accounts.pop('000')

# выводим на печать аккаунты
print(';'.join(f'{key} {value}' for key, value in sorted(accounts.items(), key=lambda x: x[1])))




# Альтернативные варианты

# transactions_file = open("bank.txt", "r")
#
# # Словарь, который будет хранить счета.
# accounts = {}
#
# total = 0
# for transaction in transactions_file:
#     account_from, account_to, amount = transaction.split(";")
#
#     # Добавляем в словарь счета если их еще там нет.
#     if account_to not in accounts:
#         accounts[account_to] = 0
#
#     if account_from not in accounts:
#         accounts[account_from] = 0
#
#     # Заполняем данными.
#     accounts[account_from] -= int(amount)
#     accounts[account_to] += int(amount)
#
# # Удаляем словарь 000
# del accounts["000"]
#
# # Сортируем словарь по балансу и формируем список для вывода
# accounts_list = []
# for account, balance in sorted(accounts.items(), key=lambda a: a[1]):
#     accounts_list.append(f"{account} {balance}")
#
# print(";".join(accounts_list))
#
#
# #
# # Вариант 2 - улучшенный
# #
# from collections import defaultdict
# transactions_file = open("bank.txt", "r")
#
# # Словарь, который будет хранить счета.
# # Используем defaultdict, чтобы автоматически создавать ключи.
# accounts = defaultdict(int)
#
# total = 0
# for transaction in transactions_file:
#     account_from, account_to, amount = transaction.split(";")
#
#     # Заполняем данными.
#     accounts[account_from] -= int(amount)
#     accounts[account_to] += int(amount)
#
# # Удаляем словарь 000
# del accounts["000"]
#
# # Сразу сортируем словарь и формируем финальный результат.
# print(";".join([f"{account} {balance}" for account, balance in sorted(accounts.items(), key=lambda a: a[1])]))


