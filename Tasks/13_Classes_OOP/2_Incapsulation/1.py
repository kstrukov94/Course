"""ЧЕЛОВЕК"""
# Создайте класс People, конструктор* которого принимает аргумент name — имя человека.
# Класс должен содержать метод get_name, который возвращает имя заглавными буквами.
#
# * Метод __init__(), который мы изучили в первом уроке про классы, называется конструктором.
#
# Пример использования класса:
# people = People("Виктор")
# print(people.get_name())
# ВИКТОР

class People:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name.upper()


# people = People("Виктор")
# print(people.get_name())


