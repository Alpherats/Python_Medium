# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# и возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# И весь период действует григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.
from sys import argv


def date_check(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    if 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 9999:
        return True
    return False


def _vis_year(date: str) -> bool:
    day, month, year = map(int, date.split('.'))
    if year % 4 == 0:
        return True
    return False


if __name__ == "__main__":
    date = list(map(str, argv[1::]))
    print(date_check(date[0]))
    print(_vis_year(date[0]))
