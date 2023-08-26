"""ПОСТРАНИЧНЫЙ ПРОСМОТР"""
# В произвольном списке находятся элементы, которые мы хотим выводить на сайте.
# Но мы не можем вывести все элементы сразу и решили сделать постраничный вывод.
# Например, на первой странице будет выводиться первые 10 элементов списка, на второй — вторая десятка и так далее.
#
# Напишите функцию products_range, которая принимает два аргумента.
# Первый отвечает за количество товаров на странице, а второй за номер страницы.
# Функция должна возвращать кортеж из двух элементов: начальный индекс и конечный индекс списка.
# Если мы возьмем срез с использованием полученных индексов, то получим товары, которые нужно вывести на странице.
#
# Пример использования функции (5 товаров на странице, 3 страница):
# indexes = products_range(5, 3)
# print(indexes)
# (10, 15)
# # Если взять срез [10:15] - то получим 5 товаров, которые должны быть выведены
# # на третьей странице.


def products_range(n_goods, n_page):
    range_end = n_goods * n_page
    range_start = range_end - n_goods
    return range_start, range_end

print(products_range(2, 3))


# def products_range(goods_on_page, page_num):
#     end_index = goods_on_page * page_num
#     start_index = end_index - goods_on_page
#     return (start_index, end_index,)
# print(products_range(4, 1))

# def products_range(products_per_page, page):
#     return products_per_page * (page - 1), products_per_page * page