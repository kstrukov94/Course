"""ЗАМЕНА ПО СЛОВАРЮ"""
# Напишите функцию replace_all, которая принимает два аргумента: текст и словарь.
# Функция должна сделать в тексте замены в соответствии с данными из словаря.
# Так если в словаре есть ключ "one" со значением "один" ({'one': 'один'}),
# то функция должна заменить в тексте слово 'one' на 'один'. Обратите внимание, что в словаре может быть сколько угодно элементов и нужно сделать замены для каждого из них.
#
# Для успешной работы данной программы вам также понадобится функция get_dict из прошлой задачи.
#
# Пример использования функции:
# result = replace_all("one, two, three, four", {'one': 'один', 'three': 'три', 'five': 'пять', 'two': 'два'})
# print(result)
# 'один, два, три, four'
import sys


# Создайте функцию replace_all в этом месте

dictionary = "'one': 'один', 'three': 'три', 'five': 'пять', 'two': 'два'"

def replace_all(text: str, data: dict) -> str:
    new_text = ""
    for key in data.keys():
        new_text = text.replace(key, data[key])
    return new_text

# Добавьте функцию get_dict из прошлой задачи сюда

def get_dict(text):
    new_dict = {}
    for block in text.split(";"):
        key, value = block.split(": ")
        new_dict[key] = value
    return new_dict

# Не удаляйте код ниже, он нужен для тестирования вашей функции.
import sys

# Получаем текст
text = sys.argv[1]

# Формируем словарь
data = get_dict(sys.argv[2])

# Получаем новый текст
print(replace_all(text, data))
