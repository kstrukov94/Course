"""COBOL COWBOYS
Говорят ИИ скоро лишит программистов работы, но практика показывает,
что даже для редких языков, вроде COBOL, нужны программисты.

Один из сотрудников «COBOL Cowboys» решил написать небольшую функцию get_name(),
которая принимает имя и фамилию сотрудника, а затем возвращает строку вида "Имя Фамилия (Название компании)".

Но почему-то функция работает не так как задумано. Исправьте ошибки.

Правильный пример использования функции:
print(get_name("Bill", "Hinshaw"))
Bill Hinshaw (COBOL Cowboys)"""


# Название компании
COMPANY_NAME = "COBOL Cowboys"

def get_name(first_name, last_name):
    """
    Возвращает имя, фамилию и названия компании.
    """
    person_name = f"{first_name} {last_name}"
    return f"{person_name} ({COMPANY_NAME})"

# Не удаляйте код ниже, он нужен для проверки вашей функции
import sys

# Получаем данны
fn = sys.argv[1]
ln = sys.argv[2]

# Формируем и выводим данные для сайта
data = get_name(fn, ln)
print(data)