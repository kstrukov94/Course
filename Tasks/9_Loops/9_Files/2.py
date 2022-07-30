result = 0
for line in open("2_transactions.txt", "r", encoding="utf-8"):
    # line_list = line.strip().split(";")
    # if line_list[1] == "income":
    #     result += int(line_list[2])
    # if line_list[1] == "outcome":
    #     result -= int(line_list[2])
    name, operation, amount = line.strip().split(";")
    if operation == "income":
        result += int(amount)
    else:
        result -= int(amount)
print(result)


# transactions_file = open("transactions.txt", "r")
#
# total = 0
#
# # Проходимся по всем строкам файла
# for transaction in transactions_file:
#     # Разбиваем строку на три составляющие
#     subject, operation, amount = transaction.split(";")
#     # В зависимости от направления платежа увеличиваем или уменьшаем баланс.
#     if operation == "income":
#         total += int(amount.strip())
#     else:
#         total -= int(amount.strip())
#
# print(total)