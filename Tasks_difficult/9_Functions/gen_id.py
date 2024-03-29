"""#259: ИДЕНТИФИКАТОРЫ
Сложность: 6 из 10
Часто для названия статьи на сайте или товара в интернет-магазине нужно сгенерировать уникальный идентификатор,
который потом можно будет вставить в URL. Напишите функцию gen_id, которая генерирует такой идентификатор.

Первым аргументом функция принимает название товара на английском языке, а также список уже существующих идентификаторов.
Новый идентификатор генерируется по следующим правилам:

Исходное имя преобразуется к нижнему регистру.
Пробелы справа и слева от названия удаляются.
Все пробелы заменяются на черточки.
Все символы, кроме символов латинского алфавита, цифр и знака «черточка», должны быть удалены.
Если полученный идентификатор уже существует, то функция должна прибавить в конец черточку и сгенерированное число,
которое начинается с двойки. Если идентификатор с двойкой также существует, то число увеличивается на 1.
И так до тех пор пока не будет найден идентификатор, которого не существует.

Пример использования функции:
print(gen_id("Alpen Gold", ["snickers", "bounty", "mars"]))
alpen-gold
# Идентификатор существует
print(gen_id("Mars", ["snickers", "bounty", "mars"]))
mars-2
# Идентификатор с двойкой существует
print(gen_id("Mars", ["snickers", "bounty", "mars", "mars-2"]))
mars-3
print(gen_id("M&Ms", ["snickers", "bounty", "mars"]))
mms"""
import string
from string import ascii_lowercase


def gen_id(name: str, ids: type(list)) -> str:
    # 1-2. приводим к нижнему регистру и удаляем пробелы по краям
    name = name.lower().strip(' ')
    # 3. меняем пробелы на черточки
    new_name = ''
    delete_list = ascii_lowercase + string.digits + '-'
    for symb in name:
        # 3. меняем пробелы на черточки
        if symb == ' ':
            new_name += '-'
        # 4. удаляем ненужные символы
        elif symb not in delete_list:
            new_name += ''
        else:
            new_name += symb
    # 5. проверяем на повторы и добавляем концовку
    counter = 2
    while new_name in ids:
        new_name = f'{new_name.rstrip("-123456789")}-{counter}'
        counter += 1
    return new_name


print(gen_id("M&Ms", ["snickers", "bounty", "mars"]))


"""РЕШЕНИЕ ПРЕПОДАВАТЕЛЯ
# Импортируем встроенный модуль string, в нем содержатся разные алфавиты
import string

# Разрешенные символы: цифры, латинский алфавит и черточка
ALLOWED_CHARS = string.digits + string.ascii_lowercase + "-"


def gen_id(name, ids):
    # Очищаем, приводим к нижему регистру, заменяем пробелы черточкой
    name = name.strip().lower().replace(" ", "-")

    # Отсекаем все лишние символы
    eng_name = ""
    for c in name:
        if c in ALLOWED_CHARS:
            eng_name += c

    # Начинаем генерацию
    new_name = eng_name
    i = 2
    # Проверяем до тех пор, пока не найдем уникальное значение
    while new_name in ids:
        new_name = u"{}-{}".format(eng_name, i)
        i += 1

    return new_name
"""