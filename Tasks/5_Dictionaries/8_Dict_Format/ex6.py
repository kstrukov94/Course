"""РЕЙТИНГ ФИЛЬМОВ"""
# Спецификаторы, которые позволяют работать со словарями,
# также поддерживают и дополнительное форматирование с использованием двоеточия: "{словарь:доп_форматирование}".
# То есть в строке форматирования мы можем получить данные из словаря по его ключу, а затем привести эти данные в нужный для нас вид.
#
# Так в редакторе ниже находится словарь movies, который содержит данные о фильме: название, рейтинг и количество голосов.
# Все данные в словарь попадают из аргументов командной строки.
#
# Программа должна сформировать и вывести строку вида: "Фильм (Рейтинг)",
# где Рейтинг — это вещественное число с одним знаком после десятичной точки.
#
# В целом в программе всё готово, кроме самого шаблона для формирования финального текста.
# Заполните шаблон m_template текстом и спецификаторами для вывода необходимой фразы.
#
# Пример использования:
# > python program.py "Зеленая миля" 9.213 125610
# > Зеленая миля (9.2)

import sys

# Формируем словарь.
movie = {
   "name": sys.argv[1],
   "rating": float(sys.argv[2]),
   "votes": int(sys.argv[3])
}

m_template = "{m[name]} ({m[rating]:.1f})"

# Форматируем строку данными из словаря.
print(m_template.format(m=movie))