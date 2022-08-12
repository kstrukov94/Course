"""ПРИМЕРЫ ИЗ УРОКА «»"""
months = ["январь", "февраль", "март", "апрель", "май", "июнь",
          "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]

# Классический вариант
counter = 0
for month in months:
    print(counter, month)
    counter += 1

# Вариант через range
for month_idx in range(len(months)):
    month = months[month_idx]
    print(month_idx + 1, month)

# Вариант через enumerate
for counter, month in enumerate(months):
    print(counter, month)

# Вывод кварталов
for counter, month in enumerate(months, start=1):
    if counter % 3 == 1: # Целочисленный остаток от деления на 3 = 1
        print("Квартал", counter // 3 + 1)
    print("    {}".format(month))
