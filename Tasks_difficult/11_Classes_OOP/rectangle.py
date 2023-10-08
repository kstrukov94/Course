"""
#133: ПРЯМОУГОЛЬНИК
Сложность: 4 из 10
Создайте класс Rectangle, который будет моделировать прямоугольник в прямоугольной системе координат на плоскости.

Конструктор класса должен принимать четыре аргумента: x1, y1, x2, y2:

x1 и y1 отвечают за левую верхнюю точку прямоугольника;
x2 и y2 за правую нижнюю точку.
Класс должен содержать следующие методы:

get_length() - возвращает длину прямоугольника,
get_width() - возвращает ширину прямоугольника,
get_area() - возвращает площадь прямоугольника,
get_perimeter() - возвращает периметр прямоугольника,
is_square() - возвращает True если прямоугольник является квадратом и False в противном случае.
Как вычислять параметры прямоугольника можно посмотреть в статье Прямоугольник.

Для простоты считаем, что все стороны прямоугольника параллельны осям координат.

Иллюстрация к задаче

Пример использования:
rectangle = Rectangle(-3, 2, 4, -2)
print(rectangle.get_length())
7
print(rectangle.get_width())
4
print(rectangle.get_area())
28
print(rectangle.get_perimeter())
22
print(rectangle.is_square())
False"""


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

    def get_x1(self):
        return float(self._x1)

    def get_y1(self):
        return float(self._y1)

    def get_x2(self):
        return float(self._x2)

    def get_y2(self):
        return float(self._y2)

    def get_length(self):
        if (self.x1 >= 0 and self.x2 >= 0) or (self.x1 <= 0 and self.x2 <= 0):
            return abs(self.x1 - self.x2)
        else:
            return abs(self.x1) + abs(self.x2)

    def get_width(self):
        if (self.y1 >= 0 and self.y2 >= 0) or (self.y1 <= 0 and self.y2 <= 0):
            return abs(self.y1 - self.y2)
        else:
            return abs(self.y1) + abs(self.y2)

    def get_area(self):
        return self.get_length() * self.get_width()

    def get_perimeter(self):
        return (self.get_length() + self.get_width()) * 2

    def is_square(self):
        return self.get_length() == self.get_width()

    x1 = property(get_x1)
    y1 = property(get_y1)
    x2 = property(get_x2)
    y2 = property(get_y2)


# rect = Rectangle(-3, 2, 4, -2) # 1, 4, 6, 1 # -3, 2, 4, -2
# print(rect.x1, rect.y1, rect.x2, rect.y2)
# print(rect.get_length())
# print(rect.get_width())
# print(rect.get_area())
# print(rect.get_perimeter())
# print(rect.is_square())
