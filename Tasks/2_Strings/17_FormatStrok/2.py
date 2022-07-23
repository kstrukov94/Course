# Отформатируйте строку hello так, чтобы она получила осмысленный вид. Выводить строку с помощью print не надо.

# age = 18
# street = 'Ленина'
# first_name = 'Олег'
# house = 58
# city_r = 'Москве'
#
# hello = 'Привет! Меня зовут N, мне M лет. Я живу в X, на улице Y, дом Z.'

age = 18
street = 'Ленина'
first_name = 'Олег'
house = 58
city_r = 'Москве'

hello = 'Привет! Меня зовут %s, мне %d лет. Я живу в %s, на улице %s, дом %d.' % (first_name, age, city_r, street, house)

