# Напишите программу, которая первым аргументом командной строки принимает название файла,
# а после выводит True если это изображение, и False в противном случае.
# Определять изображение это или нет нужно по расширению файла: png, jpeg, jpg или gif.
# Учитывайте, что имя может быть набрано в разных регистрах.
#
# Пример использования в командной строке Windows:
# > python program.py photo.png
# > True
# > python program.py photo.jpg
# > True
# > python program.py ROOM.PNG
# > True
# > python program.py video.mp4
# > False

import sys
file_name = sys.argv[1]
condition = file_name.lower().endswith(".png") or file_name.lower().endswith(".jpeg") or file_name.lower().endswith(".jpg") or file_name.lower().endswith(".gif")
print(condition)
