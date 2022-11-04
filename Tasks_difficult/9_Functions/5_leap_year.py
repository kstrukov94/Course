"""#72: ВИСОКОСНЫЙ ГОД"""
# Сложность: 2 из 10
# Напишите функцию is_leap_year, которая принимает год и возвращает True если год високосный и False в противном случае.
#
# Год является високосным, если его номер кратен 4.
# Но из кратных 100 високосными являются лишь кратные 400.
# То есть 2000 — високосный, а 1800 — нет.


def is_leap_year(year: int) -> bool:
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    return True if year % 4 == 0 else False


# print(is_leap_year(2016))

# def is_leap_year(year):
#     """
#     Функция для вычисления високосного года.
#     """
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#         else:
#             return True
#
#     return False
