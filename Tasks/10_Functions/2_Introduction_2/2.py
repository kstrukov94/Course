"""УВАЖАЕМЫЙ(АЯ)!"""
# Часто, когда люди не знают какого пола человек, то они пишут универсальное слово "Уважаемый(ая)!".
# Но мы не такие. Напишите функцию wellcome, которая принимает имя человека и выводит "Уважаемый <name>!" если это мужчина,
# "Уважаемая <name>!" если это женщина и "Здравствуйте, <name>!" если пол не определен.
# Вместо <name> должно быть вставлено передаваемое в функцию имя.
#
# Список мужчин хранится в файле man.txt, а список женщин в файле woman.txt.
# Оба файла находятся рядом с программой. Каждое имя в этих файлах записано с новой строки.
#
# Пример использования функции:
# result = wellcome("Иван")
# print(result)
# Уважаемый Иван!

def wellcome(name):
    name_found = False
    men = []
    women = []
    for line in open("man.txt", "r", encoding="utf-8"):
        men.append(line.strip())
    if name in men:
        name_found = True
        return f"Уважаемый {name}!"
    for line in open("woman.txt", "r", encoding="utf-8"):
        women.append(line.strip())
    if name in women:
        name_found = True
        return f"Уважаемая {name}!"
    if name_found == False:
        return f"Здравствуйте, {name}!"

print(wellcome("Алекс"))

def wellcome(name):
    # Сперва открываем файлы и сохраняем их данные в списки.
    man_file = open("man.txt")
    man = man_file.read().split("\n")

    woman_file = open("woman.txt")
    woman = woman_file.read().split("\n")

    # Проверяем нет ли искомого имени в списках.
    if name in man:
        text = "Уважаемый {}!".format(name)
    elif name in woman:
        text = "Уважаемая {}!".format(name)
    else:
        text = "Здравствуйте, {}!".format(name)

    return text