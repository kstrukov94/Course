"""#82: СЧАСТЛИВЫЙ ИЛИ ВСТРЕЧНЫЙ"""
# Сложность: 1 из 10
# Напишите функцию ticket_type, которая получает номер билета в виде строки из шести цифр и возвращает его тип:
# счастливый, встречный, пьяный или обычный.
#
# Счастливым называют такой билет, что сумма первых трех цифр его номера равна сумме последний трех цифр.
# Встречным называют такой билет, что сумма первых трех цифр его номера отличается на единицу от суммы последних трех цифр.
# Пьяным называют такой билет, что сумма первых трех цифр его номера отличается на двойку от суммы последних трех цифр.
# Обычными называют все остальные билеты.
#
# Пример использования функции:
# result = ticket_type("123321")
# print(result)
# счастливый

def ticket_type(number: str) -> str:
    if len(number) != 6:
        return 'Номер билет состоит не из 6 символов'
    first = sum(list(map(int, number[:3])))
    last = sum(list(map(int, number[3:])))
    if first == last:
        return 'счастливый'
    if abs(first - last) == 1:
        return 'встречный'
    if abs(first - last) == 2:
        return 'пьяный'
    return 'обычный'


# def ticket_type(ticket):
#     # Разбиваем билет на две части
#     left, right = ticket[:3], ticket[3:]
#
#     # Создаем нулевые суммы
#     left_sum = right_sum = 0
#
#     # Вычисляем суммы левой и правой половины
#     for l in left:
#         left_sum += int(l)
#
#     for r in right:
#         right_sum += int(r)
#
#     # Сравниваем суммы по модулю.
#     if abs(left_sum - right_sum) == 0:
#         return "счастливый"
#
#     if abs(left_sum - right_sum) == 1:
#         return "встречный"
#
#     if abs(left_sum - right_sum) == 2:
#         return "пьяный"
#
#     return "обычный"
#
#
# # Вариант 2
# def ticket_type(ticket):
#     # Используем математику для вычисления суммы.
#     num = int(ticket)
#
#     left_sum = num % 1000000 // 100000 + num % 100000 // 10000 + num % 10000 // 1000
#     right_sum = num % 1000 // 100 + num % 100 // 10 + num % 10 // 1
#
#     # Результат получаем из словаря, а если в словаре нет, то используем "обычный"
#     return {0: "счастливый", 1: "встречный", 2: "пьяный"}\
#         .get(abs(left_sum - right_sum), "обычный")