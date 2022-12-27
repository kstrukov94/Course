"""ПЛОЩАДЬ КОМНАТ"""
# Создайте функцию map,
# которая добавит к каждой комнате в списке rooms элемент с именем square содержащий её площадь.

rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
]


def add_square(room_dict):
    room_dict["square"] = room_dict["length"] * room_dict["width"]
    # альтернативный вариант
    # room_dict.update({"square": room_dict["length"] * room_dict["width"]})
    return room_dict


rooms = map(add_square, rooms)

print(list(rooms))
