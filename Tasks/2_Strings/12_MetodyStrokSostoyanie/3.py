# Напишите программу, которая первым аргументом командной строки принимает название файла,
# а после выводит True если это png изображение, и False в противном случае.
# Определять png это или нет нужно по расширению файла.
# Учитывайте, что имя может быть набрано в разных регистрах.
#
# Пример использования в командной строке Windows:
# > python program.py photo.png
# > True
# > python program.py photo.jpg
# > False
# > python program.py ROOM.PNG
# > True

import sys
file_name = sys.argv[1]
print(file_name.lower().endswith(".png"))
