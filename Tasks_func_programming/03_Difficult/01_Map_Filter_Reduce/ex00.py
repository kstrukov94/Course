# для случаев, когда лямбду можно заменить на более "громоздкую" функцию
l1 = list(map(lambda x: x * 2, range(10)))
print(l1)

# лучше и быстрее
l2 = [x * 2 for x in range(10) if x % 2 == 0]
print(l2)
