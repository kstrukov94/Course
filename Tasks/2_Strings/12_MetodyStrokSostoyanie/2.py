# Напишите программу, которая первым аргументом командной строки принимает телефонный номер,
# а после выводит True если номер не начинается на +7 и False если начинается с +7.
#
# Пример использования в командной строке Windows:
# > python program.py +7813514514
# > False
# > python program.py 8981514514
# > True

import sys
tel_number = sys.argv[1]
print(not tel_number.startswith("+7"))
