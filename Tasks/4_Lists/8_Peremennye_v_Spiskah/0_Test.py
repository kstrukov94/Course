# Копирование значения Михаил в список names
first_name = "Михаил"
names = ["Иван", "Алёна", first_name, "Сергей", "Лиза"]

print(names)
print(first_name)

# Замена значением "Олег", но переменная first_name не поменялась
first_name = "Михаил"
names = ["Иван", "Алёна", first_name, "Сергей", "Лиза"]
names[2] = "Олег"
print(names)
print(first_name)

# Если изменение идет через основной список, то это затрагивает исходный объект, т.к. они связаны
# изменение списка через [2_Strings][0] заменило значение first_name
first_name = ["Михаил"]
names = ["Иван", "Алёна", first_name, "Сергей", "Лиза"]
names[2][0] = "Олег"
print(names)
print(first_name)

# Разорвали связь между списками first_name и names и теперь значения для каждой перменной неизменяемые
first_name = ["Михаил"]
names = ["Иван", "Алёна", first_name, "Сергей", "Лиза"]
names[2][0] = "Олег"
first_name[0] = "Светлана"
print(names)
print(first_name)

# Значение "Светлана" заменила "Олег", потому что мы меняем не перменную, а содержимое изменяемого списка
first_name = ["Михаил"]
names = ["Иван", "Алёна", first_name, "Сергей", "Лиза"]
names[2] = "Олег"
# first_name[0] = "Светлана"
print(names)
print(first_name)
