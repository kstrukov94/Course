"""#49: ШИФР ЦЕЗАРЯ"""
# Сложность: 3 из 10
# Напишите функцию code, которая кодирует переданную в неё строку с помощью шифра Цезаря.
#
# Функция принимает два аргумента:
#
# текст для кодирования;
# необязательный аргумент key (ключ сдвига) со значением по умолчанию 1.
# Для решения данной задачи вам потребуются python-функции ord и chr.
#
# text_007 = code("Агент 007, срочно выйдите на связь")
# print(text_007)
# Бджоу!118-!тспшоп!гькейуж!об!тгѐиэ
import timeit


def code1(line: str, key=1):
    arr_chr = list(line)
    for pos, char in enumerate(arr_chr):
        arr_chr[pos] = chr(ord(char) + key)
    return ''.join(arr_chr)


# print(code("Агент 007, срочно выйдите на связь"))
# print(code("Программист - лучшая профессия", key=3))

def code2(text, key=1):
    """
    Цифр Цезаря
    """
    new_text = ""
    # Идем по тексту
    for char in text:
        # Формируем новый текст со сдвигом.
        new_text += chr(ord(char) + key)
    return new_text

