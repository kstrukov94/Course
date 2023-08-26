"""#46: ПРОВЕРКА СКОБОК"""
# Сложность: 2 из 10
# Напишите программу skobki.py, которая получает из первого аргумента командной строки строку,
# содержащую скобки, а затем проверяет правильно ли они расставлены.
#
# Рассматривайте только круглые скобки.
# Программа должна выводить 1 если скобки расставлены правильно, и 0 если порядок скобок нарушен
#
# Пример использования:
# > python skobki.py ((2+3)+(4-5))
# 1


import sys
text = sys.argv[1]
# text = "()"

stack = []
noErrors = True

for symbol in text:
    if symbol in "(":
        stack.append(symbol)
    elif symbol in ")":
        if stack:
            stack.pop()
        else:
            noErrors = False
noErrors = False if stack else True

print(int(noErrors))

# import sys
# string = sys.argv[1]
#
# # Заводим переменную для подсчета количества скобок.
# # Если скобка будет открывающей, то будем добавлять 1.
# # Если скобка закрывающая, то будем отнимать 1.
# # Если количество открывающих скобок равно количеству закрывающих,
# # то в конце программы в skobka будет 0.
# skobka = 0
#
#
# # Проходим в цикле по всем символам.
# for i in string:
#     # Увеличиваем или уменьшаем skobka к зависимости от типа скобки.
#     if i == "(":
#         skobka += 1
#     elif i == ")":
#         skobka -= 1
#     else:
#         pass
#
#     # Если skobka меньше 0, то значит попалась закрывающая скобка без открывающей.
#     # Сразу выходим из цикла, так как дальше нет смысла смотреть.
#     if skobka < 0:
#         break
#
# # Выводим результат
# if skobka == 0:
#     print("1")
# else:
#     print("0")
#
# # Альтернативный вывод с помощью однострочного if
# print("1" if skobka == 0 else "0")