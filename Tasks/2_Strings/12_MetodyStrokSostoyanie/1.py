# Напишите программу, которая первым аргументом командной строки принимает телефонный номер,
# а после выводит True если номер начинается на +7 и False в противном случае.
#
# Пример использования в командной строке Windows:
# > python program.py +7813514514
# > True
# > python program.py 8981514514
# > False


import sys
tel_number = sys.argv[1]
print(tel_number.startswith("+7"))
