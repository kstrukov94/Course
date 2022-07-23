# Для перевода строк в HTML служит тег <br>. Напишите программу, которая первым аргументом командной строки принимает HTML-текст,
# а затем преобразовывает <br>-теги к переводам строк на Python и выводит результат.
#
# Пример использования:
# > python title.py "Leading growth:<br>why strategy matters"
# > Leading growth:
# > why strategy matters

import sys
text = sys.argv[1]
text = text.replace("<br>", "\n")
print(text)
