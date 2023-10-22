from time import sleep


""" читаем содержимое файла и добавляем +1 вместо предыдщуего значения
def inc_visitors():
    with open('visitors.txt', 'r+', encoding='UTF-8') as visitors_file:
        visitors = int(visitors_file.read().strip())
        visitors_file.seek(0)
        visitors_file.write(str(visitors + 1))


inc_visitors()"""


""" Пример Race condition (одна функция еще не завершила действие, а вторая уже просится прочитать файл => пропуски счетчика)

from time import *


def inc_visitors():
    with open('visitors.txt', 'r+', encoding='UTF-8') as visitors_file:
        visitors = int(visitors_file.read().strip())
        print(visitors)
        sleep(3)
        visitors_file.seek(0)
        visitors_file.write(str(visitors + 1))


inc_visitors()"""

from time import *
from os import remove


def inc_visitors():
    while True:
        try:
            with open('visitors.lock', 'x'):
                with open('visitors.txt', 'r+', encoding='UTF-8') as visitors_file:
                    visitors = int(visitors_file.read().strip())
                    print(visitors)
                    sleep(3)
                    visitors_file.seek(0)
                    visitors_file.write(str(visitors + 1))
            remove('visitors.lock')
            break
        except FileExistsError:
            continue


inc_visitors()

