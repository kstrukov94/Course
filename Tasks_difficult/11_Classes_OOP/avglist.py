"""#136: СРЕДНИЕ ЗНАЧЕНИЯ СПИСКА
Сложность: 6 из 10
Создайте класс AvgList для получения среднего арифметического и медианы списка.

AvgList должен наследоваться от класса list, который является основным для списков в Python.

Класс должен содержать следующие методы:

mean() — возвращает среднее арифметическое.
median() — возвращает медиану или среднее значение из списка.
Если количество элементов в списке четное, то медиана возвращает среднее между двумя центральными.

median_low() — возвращает медиану, но если количество элементов в списке четное,
то возвращает меньшее (левое) из двух центральных элементов.

median_high() — возвращает медиану, но если количество элементов в списке четное,
то возвращает большее (правое) из двух центральных элементов.

Подробнее о медиане и среднем арифметическом.

Пример использования
avg = AvgList([1,2,3,4,5,9])
print(avg.mean())
4.0
print(avg.median_low())
3
print(avg.median_high())
4
print(avg.median())
3.5
avg.append(11)
print(avg.mean())
5.0
print(avg)
[1, 2, 3, 4, 5, 9, 11]"""


class AvgList(list):

    def mean(self):
        return sum(self) / len(self)

    def median(self):
        if len(self) % 2:
            self.sort()
            mid = int(len(self) // 2)
            return self[mid]
        else:
            return float((self.median_low() + self.median_high()) / 2)

    def median_low(self):
        if len(self) % 2:
            return self.median_high()
        else:
            self.sort()
            return self[(len(self) // 2) - 1]

    def median_high(self):
        self.sort()
        return self[len(self) // 2]


""" Тестирование
avg = AvgList([1, 2, 3, 4, 5, 9])
# avg = AvgList([7, 1, 3, 4, 9])
# avg = AvgList([7, 1, 3, 6, 9, 16])
print(avg)
print(avg.mean())
print(avg.median_low())
print(avg.median_high())
print(avg.median())
avg.append(11)
print(avg)

Решение преподавателя

# Наследуемся от list, так как list - это класс списка.
# Это сильно упрощает работу, так как AvgList получит все встроенные
# методы списков: insert, append и тд.


class AvgList(list):

    def mean(self):
        # self - это и есть список
        return sum(self) / len(self)

    def median(self):
        # Создаем копию списка
        sorted_list = self[:]
        sorted_list.sort()

        if len(sorted_list) % 2 == 0:
            right_index = int(len(sorted_list) / 2)
            left_index = right_index - 1
            return (sorted_list[left_index] + sorted_list[right_index]) / 2
        else:
            return sorted_list[int(len(sorted_list) / 2)]

    def median_low(self):
        sorted_list = self[:]
        sorted_list.sort()

        if len(sorted_list) % 2 == 0:
            right_index = int(len(sorted_list) / 2)
            left_index = right_index - 1
            return sorted_list[left_index]
        else:
            return sorted_list[int(len(sorted_list) / 2)]

    def median_high(self):
        sorted_list = self[:]
        sorted_list.sort()
        return sorted_list[len(sorted_list) // 2]
        
Получилось следующее решение. При этом "мозолит" глаза постоянный вызов метода .sort().
Возможно ли через конструктор класса AvgList сразу запустить сортировку листа, 
чтобы потом каждый раз не сортировать список при выборе методов median, median_low, median_high? Спасибо!  

Можно, но не надо, ведь после сортировки изначальный порядок элементов пропадет.

Если вы посмотрите в моё решение, 
то я там, вообще, создаю копию списка, чтобы а) получить медиану и б) не потерять начальные данные
"""
