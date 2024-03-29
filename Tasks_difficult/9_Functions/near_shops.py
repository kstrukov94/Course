"""#79: МАГАЗИНЫ ПОБЛИЗОСТИ
Сложность: 4 из 10
Написать функцию near_shops, которая находит все магазины в радиусе R от заданной точки.

Функция принимает три аргумента:

Координаты точки, вокруг которой будем искать. В виде кортежа из двух элементов (X, Y).
Радиус поиска — R.
Список магазинов из кортежей вида ("название магазина", (Координата_X, Координата_Y))
Функция должна возвращать список из кортежей вида ("название магазина", Расстояние_до_магазина).
Кортежи в списке должны быть отсортированы по расстоянию до магазина (от близких к дальним).
В список должны попасть только магазины, которые расположены в пределах R.

Пример использования функции:
shops = [
    ("Магазин 1", (1, 1)),
    ("Магазин 2", (-1, 0)),
    ("Магазин 3", (2, -1)),
    ("Магазин 4", (2, 4)),
    ("Магазин 5", (2, 0)),
]
my_shops = near_shops((2, 3), 3, shops)
print(my_shops)
[('Магазин 4', 1.0), ('Магазин 1', 2.23606797749979), ('Магазин 5', 3.0)]"""

# shops = [
#     ("Магазин 1", (1, 1)),
#     ("Магазин 2", (-1, 0)),
#     ("Магазин 3", (2, -1)),
#     ("Магазин 4", (2, 4)),
#     ("Магазин 5", (2, 0)),
# ]


def near_shops(point: tuple, radius: float, shops_list: list):
    point_x, point_y = point
    result_list = []
    # перебираем магазины по порядку и добавляем при условии, что радиус больше либо равен l
    for shop in shops_list:
        l = ((point_x - shop[1][0]) ** 2 + (point_y - shop[1][1]) ** 2) ** 0.5
        if radius >= l:
            result_list.append((shop[0], l))
    # сортируем итоговый список по l (нужна лямбда функция)
    result_list.sort(key=lambda a: a[1])
    return result_list


# print(near_shops((2, 3), 3, shops))
