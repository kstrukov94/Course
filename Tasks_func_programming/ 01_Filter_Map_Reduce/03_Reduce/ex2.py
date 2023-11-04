"""ПЛОЩАДЬ КВАРТИРЫ"""
# Используйте map и reduce, чтобы посчитать площадь квартиры, состоящей из комнат rooms.

from functools import reduce

rooms = [
    {"name": "кухня", "length": 6, "width": 4},
    {"name": "комната 1", "length": 5.5, "width": 4.5},
    {"name": "комната 2", "length": 5, "width": 4},
    {"name": "комната 3", "length": 7, "width": 6.3},
]


def room_square(room: dict):
    return room["length"] * room["width"]


def flat_square(room1, room2):
    return room1 + room2


rooms = map(room_square, rooms)
square = reduce(flat_square, rooms)