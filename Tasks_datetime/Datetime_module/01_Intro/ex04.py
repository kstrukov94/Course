"""РАСЧЕТ ЗАРПЛАТЫ"""
# Один час работы программиста оценивается в 1000 рублей.
# При этом если разработчик трудится в выходные, то стоимость часа возрастает в 1.5 раза.
# Для фиксации отработанных часов, программист ведет файл days.txt, который расположен в каталоге с программой, которую вам нужно написать.
#
# Каждый отработанный день хранится в отдельной строке в формате ГГГГ-ММ-ДД,Ч, где ГГГГ-ММ-ДД — это дата, а Ч — отработанные часы.
# Вот пример одного из таких файлов:
#
# 2020-04-02,3
# 2019-12-02,4
# 2018-01-01,5
# 2019-04-27,5
# 2020-02-11,2
# 2020-03-12,6
# Напишите программу, которая анализирует данный файл и выводит зарплату программиста за все дни.
# Финальный результат нужно выводить как целое число.
#
# Пример использования (на основе данных выше):
# > python program.py
# > 27500

from datetime import date


working_hours = []
for line in open('ex04_days.txt', 'r', encoding='utf-8'):
    work_date, work_hours = line.strip().split(sep=',')
    work_year, work_month, work_day = map(int, work_date.split(sep='-'))
    work_date = date(work_year, work_month, work_day)
    # print(work_date)
    # print(work_date.isoweekday())
    # print('---------------')
    working_hours.append(1000 * 1.5 * int(work_hours)) if work_date.isoweekday() > 5 else working_hours.append(1000 * int(work_hours))
print(int(sum(working_hours)))


from datetime import date, datetime

BASE_SALARY = 1000

with open("days.txt") as file:
    salary = 0
    for line in file.readlines():
        # Получаем данные
        f_date, f_hours = line.split(",")

        # Получаем дату.
        f_date = datetime.strptime(f_date, '%Y-%m-%d').date()

        # Альтернативный вариант
        # year, month, day = f_date.split("-")
        # f_date = date(int(year), int(month), int(day))

        # Преобразуем отработанные часы.
        f_hours = int(f_hours)

        # Считаем зарплату.
        if f_date.weekday() in (5, 6):
            salary += BASE_SALARY * 1.5 * f_hours
        else:
            salary += BASE_SALARY * f_hours

    print(int(salary))
