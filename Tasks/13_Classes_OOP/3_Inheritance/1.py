"""МУЖЧИНА И ЖЕНЩИНА"""
# Создайте классы Man и Woman унаследованные от People.
# Классы должны содержать дополнительный метод get_sex, который возвращает 'm' для мужчин и 'w' для женщин.

class People:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name.lower()

class Man(People):
    def get_sex(self):
        return "m"

class Woman(People):
    def get_sex(self):
        return "w"
