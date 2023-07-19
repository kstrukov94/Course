"""90: СТОИМОСТЬ ДОСТАВКИ"""


# Сложность: 3 из 10
# Напишите функцию delivery, которая рассчитывает стоимость доставки техники по Москве и области.
#
# Функция принимает один обязательный аргумент с ценой и 4 необязательных аргумента логического типа:
#
# region – принимает False если доставка по Москве и True если по области.
# big – принимает True если товар крупногабаритный и False для мелкогабаритной техники.
# time – принимает True если доставка назначена на определенное время.
# today – отвечает за доставку «День в день».
# Все дополнительные аргументы по умолчанию установлены на False.
#
# Для решения задачи используйте условия и цены доставки, которые мы взяли на сайте МВидео.
#
# Пример использования функции:
# # Товар ценой в 5000 с доставкой в регион.
# print(delivery(5000, True))
# 290
# # Товар ценой в 5000 с доставкой по Москве в определенное время.
# print(delivery(5000, False, False, True))
# 190

def delivery(price, region=False, big=False, time=False, today=False):
    delivery_price = 0

    if region:
        if big:
            delivery_price = 490
        else:
            delivery_price = 290

    elif price < 5000:
        if big:
            delivery_price = 490
        else:
            delivery_price = 290
    else:
        if big:
            delivery_price = 490
        else:
            delivery_price = 0

    if today:
        delivery_price = 990

    if time:
        delivery_price += 190

    return delivery_price

# Проверки


# delivery(1000) #290
# delivery(5000, False, True) #490
# delivery(1000, time=True, big=True) #680
# delivery(1000, time=True) #480


# def delivery(amount, region=False, big=False, time=False, today=False):
#     """
#     Функция расчета доставки.
#     Ничего сложного, просто логические выражения.
#     """
#
#     # Доставка день в день, сразу 990.
#     # Дальше считать смысла нет.
#     if today:
#         return 990
#
#     # Задаем базовую стоиомсть по Москве и в регионы.
#     if amount < 5000:
#         price = 290
#     else:
#         if region:
#             price = 290
#         else:
#             price = 0
#
#     # Проверяем не крупногабарит ли.
#     # Если крупногабарит, то цена 490.
#     if big:
#         price = 490
#
#     # Устанавливаем надбавку за срочность.
#     if time:
#         price += 190
#
#     return price