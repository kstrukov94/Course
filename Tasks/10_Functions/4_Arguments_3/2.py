"""СКОРОСТЬ БЕГА"""
# Чуть ранее вы написали функцию для вычисления темпа бега, теперь стоит обратная задача.
#
# Напишите функцию pace_to_speed, которая принимает два аргумента.
# Первый аргумент обязательный и отвечает за минуты, а второй опциональный и отвечает за секунды.
# В случае если второй аргумент не передается, то нужно считать значение равным нулю.
#
# Функция должна вычислить скорость бегуна в км/ч и вернуть результат в виде вещественного числа,
# округленного до 1 знака после десятичной точки.
#
# Пример использования функции:
# s = pace_to_speed(5)
# print(s)
# 12
# s = pace_to_speed(4, 48)
# print(t)
# 12.5

def pace_to_speed(mins, secs = 0):
    hours = mins / 60 + secs / 3600
    return  round(1 / hours, 1)

print(pace_to_speed(4, 48))

def pace_to_speed(minutes, seconds=0):
    """
    Функция переводит темп бега км/мин в скорость.
    """
    # Преобразовываем к десятичном виду.
    time = minutes + (seconds / 60)

    # Округляем и выводим результат.
    return round(60 / time, 1)