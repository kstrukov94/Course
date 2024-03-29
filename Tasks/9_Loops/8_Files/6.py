"""ПОМОЩЬ МАРКЕТОЛОГАМ SPARА"""
# Маркетологи магазина SPAR попросили вас помочь найти им слова, которые содержат внутри себя слово «спар».
# Сам набор слов находится в файле room_dict.txt, который лежит рядом с программой и сохранен в кодировке cp1251.
# Каждое слово занимает одну строку.
#
# Напишите программу, которая проходится по всему файлу room_dict.txt, ищет в нём слова, которые содержат «спар» в любом регистре,
# а затем выводит эти слова в том порядке, в котором они сохранены в файле. При этом само слово «спар» при выводе надо заменить на SPAR.
#
# Пример файла room_dict.txt
#
# авокадо
# воспарить
# проспорить
# спарринг
# Пример использования программы (с файлом выше):
# > python program.py
# > воSPARить
# > SPARринг

results = []
for line in open("6_dict.txt", "r", encoding="cp1251"):
    line = str(line).lower()
    if "спар" in line:
        results.append(str(line).strip().replace("спар", "SPAR"))
print("\n".join(results))

# result = []
#
# for line in open("room_dict.txt", encoding="cp1251"):
#     line = line.strip().lower()
#     if "спар" in line:
#         result.append(line.replace("спар", "SPAR"))
#
# print("\n".join(result))