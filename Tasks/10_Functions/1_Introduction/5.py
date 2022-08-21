"""ТЕМП БЕГА"""
# В обычной жизни скорость передвижения измеряется в км/ч,
# однако бегуны на длинные дистанции (полумарафон, марафон) измеряют не скорость бега, а темп бега,
# то есть время, которое необходимо для преодоления 1 км пути.
#
# Напишите функцию speed_to_pace, которая первым параметром принимает скорость в км/ч,
# а затем возвращает темп бега в формате М:CC (минуты:секунды).
# Возвращаемое значение должно быть строкой.
#
# Пример использования функции:
# t = speed_to_pace(12)
# print(t)
# 5:00
# t = speed_to_pace(12.5)
# print(t)
# 4:48

def speed_to_pace(kmh):
    mins = round(60 // kmh)
    secs = round((60 / kmh - mins) * 60)
    return f"{mins}:{secs:02}"

print(speed_to_pace(11.9))

# def speed_to_pace(speed):
#     """
#     Функция переводит скорость (speed) в км/ч в темп (км/мин).
#     """
#     temp = 60 / speed
#     minutes = int(temp)
#     seconds = (temp - minutes) * 60
#     return "{}:{:02.0f}".format(minutes, seconds)