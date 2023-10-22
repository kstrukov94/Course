"""#137: АНАЛИЗ ЛОГОВ WEB-СЕРВЕРА"""
"""Сложность: 6 из 10
Каждый раз, когда вы заходите на сайт, web-сервер сохраняет информацию о посещении в специальный лог-файл. 
Каждая запись в лог-файле начинается с новой строки и содержит базовую информацию о визите: 
IP-адрес, время посещения, адрес страницы, код и размер ответа, данные о браузере.

Напишите программу analyze.py, которая будет анализировать упрощенный лог-файл 
и выводить самую посещаемую страницу за определенную дату. 
Дату программа получает из первого аргумента командной строки в формате ДД.ММ.ГГГГ.

Лог-файл должен находится в папке с программой и называться server.log. Скачать тестовый лог.

Так как лог-файл может достигать размера в несколько гигабайт, то программа должна экономить оперативную память.

Программа должна выводить адрес страницы и количество посещений за этой страницы.

Пример файла server.log
217.107.255.12 [01/Jan/2016:00:21:51] "GET / HTTP/1.1" 200
217.76.47.143 [01/Jan/2016:00:21:56] "GET /cars HTTP/1.1" 200
213.134.192.55 [01/Jan/2016:00:22:30] "GET /search HTTP/1.1" 200
Разбор записи в лог-файле
217.76.47.143 [01/Jan/2016:00:21:56] "GET /cars HTTP/1.1" 200
217.76.47.143 — IP-адрес.
[01/Jan/2016:00:21:56] — дата и время в квадратных скобках.
"GET /cars HTTP/1.1" — блок с запросом, который состоит из 3 частей:
GET — тип запроса.
/cars — адрес страницы.
HTTP/1.1 — протокол.
200 — кода ответа сервера.
Пример работы программы:
Программа выводит, что 01.01.2016 страницу / посетили 795 раз.

> python analyze.py 01.01.2016
> / 795"""


import sys
from datetime import datetime as dt

inp_date = dt.strptime(sys.argv[1], '%d.%m.%Y')

pages = set()
pages_visits = {}

# сортируем лог построчно
with open('server.log', 'r', encoding='utf-8') as log_file:
    for line in log_file:
        ip_str, date_str, type_str, page_str, protocol_str, servcode_str = line.strip().split(' ')
        log_date = dt.strptime(date_str.strip('[]'), '%d/%b/%Y:%H:%M:%S')
        log_page = page_str
        # проверяем, что попали в нужную дату
        if log_date.year == inp_date.year and log_date.month == inp_date.month and log_date.day == inp_date.day:
            # для быстроты поиска страниц создаем сет и список
            if log_page not in pages:
                pages.add(log_page)
                pages_visits[log_page] = 1
            else:
                pages_visits[log_page] = pages_visits[log_page] + 1

# ищем в результатах самую просматриваемую страницу
page_most_visited = None
for key, value in pages_visits.items():
    if not page_most_visited or pages_visits[page_most_visited] < value:
        page_most_visited = key
print(f'{page_most_visited} {pages_visits[page_most_visited]}')



""" Решение преподавателя
import sys
from datetime import datetime as dt

search_date = sys.argv[1]

# Извлекаем дату.
# Подробнее про даты в мини-курсе Дата и время в Python 3.
search_date = dt.strptime(search_date, "%d.%m.%Y")

paths = {}
# Анализ файла логов
with open("server.log") as server_log:
    for line in server_log:
        ip, date, get, path, http, answer = line.strip().split(" ")
        date = date[1:-1]
        date = dt.strptime(date, "%d/%b/%Y:%H:%M:%S")

        # Сравниваем даты
        if date.strftime("%d.%m.%Y") == search_date.strftime("%d.%m.%Y"):
            if path not in paths:
                paths[path] = 0

            paths[path] += 1

# Формирования финального результата
max_path_count = 0
max_path = ""
for path in paths.keys():
    if paths[path] > max_path_count:
        max_path_count = paths[path]
        max_path = path

print(max_path, max_path_count)
"""