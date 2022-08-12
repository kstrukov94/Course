"""НЕСКОЛЬКО ИНДЕКСОВ"""
# Напишите функцию get_chars, которая первым аргументом принимает строку,
# а затем произвольное количество чисел.
# Каждое переданное число отвечает за индекс элемента в переданной строке.
#
# Функция должна вернуть строку, включающую только символы, которые стоят на соответствующих переданных позициях.
#
# Пример использования функции:
# # Выводим 0, 2, 4 и 6 символы строки "I am Programmer"
# print(get_chars("I am Programmer", 0, 2, 4, 6))
# Ia r

def get_chars(text, *indexes):
    result = ""
    for index in indexes:
        result += str(text)[index]
    return result

print(get_chars("I am Programmer", 0, 2, 4, 6))
print(get_chars("Python is the best", -1, -2, -3, -4, -5))

