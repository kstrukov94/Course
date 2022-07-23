"""СУММА ЭЛЕМЕНТОВ СПИСКА"""
# Посчитайте и выведете на экран сумму элементов списка numbers. Используйте цикл while.

numbers = [1, 7, 8, 34, 56, 14, 9]
i = 0
num_sum = 0
while i < len(numbers):
    num_sum += numbers[i]
    i += 1
print(num_sum)