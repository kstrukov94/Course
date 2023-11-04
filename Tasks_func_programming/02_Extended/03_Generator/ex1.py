"""МЕДАЛИСТЫ"""
"""В переменной students содержится список учеников класса с их средними годовыми оценками.

Поместите в переменную gold имена золотых медалистов, а в silver — серебряных.

Золото получают ученики, которые имеют среднюю оценку 4.9 или 5.0, 
а серебро — ученики со средним баллом от 4.5 до 4.8 (включительно).

Используйте генераторы списков."""

students = [
    {"name": "Светлана", "avg_ball": 4.7},
    {"name": "София", "avg_ball": 5.0},
    {"name": "Егор", "avg_ball": 4.4},
    {"name": "Марина", "avg_ball": 4.2},
    {"name": "Дима", "avg_ball": 3.8},
    {"name": "Антон", "avg_ball": 4.0},
    {"name": "Милана", "avg_ball": 4.9},
    {"name": "Фёдор", "avg_ball": 4.5},
    {"name": "Татьяна", "avg_ball": 3.7}
]

gold = [student["name"] for student in students if student["avg_ball"] >= 4.9]
silver = [student["name"] for student in students if 4.5 <= student["avg_ball"] <= 4.8]
