"""ЛИЧНЫЙ КАБИНЕТ СБЕРА"""
# В прошлой задаче мы научились разбивать числа на классы.
# Теперь давайте усложним задачу и поможем Сберу вывести баланс в личном кабинете:
#
#
#
# Чтобы всё получилось нужно учесть следующие условия:
#
# Числа разбиваются пробелами на классы как в прошлой задаче.
# Десятичная часть отбивается запятой, а не точкой.
# Все числа округляются до двух знаков после десятичной точки (запятой).
# Если десятичная часть в конце содержит два нуля, то нужно оставить только целую часть:
# 123,00 → 123
# Чтобы решить данную задачу, нужно использовать сразу два спецификатора форматирования:
# один для разбиения на классы {:,}, а второй для того, чтобы оставить два знака после десятичной точки {:.2f}.
# К сожалению, из официальной документации сложно понять как это правильно сделать, поэтому мы подскажем.
# Общая формула выглядит так: {:ab}, где a — это спецификатор для разделения на классы,
# а b — спецификатор для округления до двух знаков после десятичной точки.
# Важно использовать их именно в таком порядке, иначе не сработает.
#
# После применения такого форматирования вы получите строку примерно такого вида "10,388.66" и далее вам останется с помощью методов довести её до финального вида.
#
# Напишите программу, которая получает из аргументов командной строки вещественное число, а после приводит его в формат, который подойдет Сберу и выводит результат.
#
# Пример использования:
# > python program.py 10388.66
# > 10 388,66
# > python program.py 5000.00
# > 5 000

import sys
num = float(sys.argv[1])
result_str = "{:,.2f}".format(num).replace(",", " ").replace(".", ",").replace(",00", "")
print(result_str)