"""СУММА ЭЛЕМЕНТОВ СПИСКА, 2_Strings"""
# Посчитайте и выведете на экран сумму элементов списка numbers. Используйте цикл for.

numbers = [41, 5, 83, 4, 16, 14, 59]

num_sum = 0
for num in numbers:
    num_sum += num
print(num_sum)