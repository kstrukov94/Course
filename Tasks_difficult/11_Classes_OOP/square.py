"""#135: КВАДРАТ
Сложность: 4 из 10
Создайте класс Square, который будет моделировать квадрат в прямоугольной системе координат на плоскости.
Так как квадрат — это частный случай прямоугольника, то Square должен наследоваться от Rectangle из задачи 133.

Конструктор Square должен принимать 3 аргумента: x, y, l:

x, y — координаты левого верхнего угла квадрата;
l — длина стороны квадрата.
Родительский класс Rectangle также должен находится в файле с решением.

Пример использования:
square = Square(1, 4, 2)
print(square.get_length())
2
print(square.get_width())
2
print(square.get_area())
4
print(square.get_perimeter())
8
print(square.is_square())
True"""


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


class Square(Rectangle):
    def __init__(self, sx1, sy1, l):
        sx2 = sx1 + l
        sy2 = sy1 - l
        super().__init__(sx1, sy1, sx2, sy2)

# sq = Square(-3, 2, 4)
# print(sq.x1, sq.y1, sq.x2, sq.y2)
# print(sq.get_length())
# print(sq.get_width())
# print(sq.get_area())
# print(sq.get_perimeter())
# print(sq.is_square())
