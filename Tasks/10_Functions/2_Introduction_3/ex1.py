"""ОПЛАТА ПО ЧАСАМ"""
# Напишите функцию calc_money() для расчета оплаты по часам.
# Функция должна принимать два аргумента:
# 1) стоимость 1 часа работы — целое число;
# 2) потраченное время — список из двух элементов (часы и минуты).
#
# При вычислении оплаты за минуты,
# итоговое значение следует округлить классическим способом до 0 знаков после запятой.
# Сама функция calc_money() должна вернуть целое число.
#
# Пример использования функции (работа в течение 7 часов 37 минут по ставке 1500 рублей/час):
# money = calc_money(1500, (7, 37))
# print(money)
# 11425

def calc_money(money_per_hour, time):
    # проверка
    if type(money_per_hour) == str and money_per_hour.isdigit():
        money_per_hour = float(money_per_hour)

    # проверка на кортеж доделать
    if type(time) == list:
        time = tuple(time)

    result = int(round(money_per_hour * (time[0] + (time[1]/60))))

    # Либо распаковываем список в две отдельные переменные
    # hours, minutes = duration

    return result

# Пример использования функции
print(calc_money(700, [4, 46]))

# import sys
#
# def calc_money(rate_per_hour, duration):
#     # Распаковываем список в две отдельные переменные
#     hours, minutes = duration
#     # Считаем часы
#     hours_money = hours * rate_per_hour
#     # Считаем минуты с округлением.
#     minutes_money = round((minutes * rate_per_hour / 60), 0)
#     return int(hours_money + minutes_money)
#
#
# # Рассчитываем зарплату
# money = calc_money(int(sys.argv[1]), tuple(map(int, sys.argv[2:])))
#
# # Получаем ответ для проверки
# print(money)
