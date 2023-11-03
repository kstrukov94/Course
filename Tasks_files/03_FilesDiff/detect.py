"""#258: PNG, JPEG ИЛИ GIF"""
"""Сложность: 8 из 10
Напишите программу detect.py, которая первым аргументом принимает имя файла, 
а затем анализирует его и выводит на экран формат изображения: png, jpeg или gif. 
Если файл не является изображением, то программа должна вывести None. 
Сам файл с изображением находится в папке с программой.

Пример использования программы:
> python detect.py image.jpg
> jpeg"""

import sys

image_name = sys.argv[1]
# image_name = "image.gif"

jpeg_hex = ["ff d8 ff db", "ff d8 ff e0", "ff d8 ff e1"]
gif_hex = ["47 49 46 38 37 61", "47 49 46 38 39 61"]
png_hex = "89 50 4e 47 0d 0a 1a 0a"

with open(image_name, "rb") as image_file:
    image = image_file.read()
    image_hex = image[:8].hex(sep=" ")
    if image_hex[:11] in jpeg_hex:
        print("jpeg")
    elif image_hex[:17] in gif_hex:
        print("gif")
    elif image_hex == png_hex:
        print("png")
    else:
        print(None)

"""Решение преподавателя"""
"""
import sys

filename = sys.argv[1]

with open(filename, "rb") as image_file:
    # Читаем начало файла
    data = image_file.read(50)

    # Сравниваем начало с signature форматов
    if data[:6] in (b'GIF87a', b'GIF89a'):
        image_type = 'gif'
    elif data.startswith(b'\x89PNG\r\n\x1a\n'):
        image_type = 'png'
    elif data.startswith(b'\xff\xd8'):
        image_type = 'jpeg'
    else:
        image_type = None
    print(image_type)
"""
