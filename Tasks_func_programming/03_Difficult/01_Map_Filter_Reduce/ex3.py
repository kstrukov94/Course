from functools import reduce


def myreduce(func, obj, init=None):
    iter_obj = iter(obj)
    if init is None:
        first = next(iter_obj)
        for this in iter_obj:
            first = func(first, this)
    else:
        first = init
        for this in iter_obj:
            first = func(first, this)
    return first


# print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5], 0))
# print(myreduce(lambda x, y: x * y, [1, 2, 3, 4, 5], 0))
