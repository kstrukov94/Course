"""ФОРМИРУЕМ СЛОВАРЬ"""


# Напишите функцию get_dict, которая принимает один аргумент — текст, а затем формирует на базе этого текста словарь и возвращает его.
# Передаваемый текст имеет следующий формат: "ключ1:значение1;ключ2:значение2;ключN:значениеN" - каждая пара ключ/значение разделены точкой с запятой,
# а сами ключ и значения отделяются двоеточием.
#
# И ключ, и значение в итоговом словаре должны быть строками.
#
# Пример использования функции:
# result = get_dict("a:10;b:20;c:30")
# print(result)
# {'a': '10', 'b': '20', 'c': '30'}

def get_dict(text):
    d = {}
    pairs = text.split(';')
    for pair in pairs:
        key, value = pair.split(':')
        d.update({key: value})
    return d


# print(get_dict("a:10;b:20;c:30"))

# Решение упрощенное
# def get_dict(text: str):
#     data = {}
#     for item in text.split(";"):
#         k, v = item.split(":")
#         data[k] = v
#     return data