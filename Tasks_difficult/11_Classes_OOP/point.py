"""
#76: ТОЧКА
Сложность: 3 из 10
Создайте класс Point, который будет моделировать поведение точки в прямоугольной системе координат на плоскости.

Конструктор класса должен принимать два аргумента x и y, которые отвечают за координаты точки.

Изменение координат точки должно происходить с помощью свойств (property). Каждая координата должна быть отдельным свойством точки.

Также нужно добавить метод set(x, y), с помощью которого можно изменить обе координаты.

Значения координат должны храниться как float, однако класс должен принимать координаты представленные как числами (int, float), так и строками (str), которые можно преобразовать к float.

Пример использования класса:
point = Point(12.34, "15.46")
print(type(point.x))
<class 'float'>
print(type(point.y))
<class 'float'>
point.x = "4"
point.y = 5.4
print(point.x)
4.0
print(point.y)
5.4
point.set(7, "99.8")
print(point.x)
7.0
print(point.y)
99.8
"""


class Point:
    def __init__(self, x, y):
        self._x = float(x) if (type(x) in (int, float, str)) else print('Неверно задан тип "x"')
        self._y = float(y) if (type(y) in (int, float, str)) else print('Неверно задан тип "y"')

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, new_x):
        self._x = float(new_x) if (type(new_x) in (int, float, str)) else print('Неверно задан тип "x"')

    @y.setter
    def y(self, new_y):
        self._y = float(new_y) if (type(new_y) in (int, float, str)) else print('Неверно задан тип "y"')

    def set(self, new_x, new_y):
        self.x = new_x
        self.y = new_y


# point1 = Point(5, 6)
#
# print(point1.x)
# print(point1.y)
#
# point1.x = 55
# point1.y = 66
#
# print(point1.x)
# print(point1.y)
#
# point1.set([22], (22, 33))
#
# print(point1.x)
# print(point1.y)