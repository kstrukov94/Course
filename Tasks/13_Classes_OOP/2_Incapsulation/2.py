"""ИМЯ ЧЕЛОВЕКА"""


# Создайте объект people класса People, а затем выведете на экран имя человека заглавными буквами с помощью метода get_name.

class People:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name.upper()

people = People("Кирилл")
print(people.get_name())
