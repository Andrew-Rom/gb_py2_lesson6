"""
HW 6_1
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на высокосность вынести в отдельную защищённую функцию.
"""

__all__ = ['date_exist']


def __is_valid(value: str):
    if type(value) is not str:
        return False
    elif not value.__contains__('.'):
        return False
    elif value.count('.') != 2:
        return False
    else:
        values = value.split('.')
        _day, _month, _year = value.split('.')
        if any(len(values[i]) == 0 for i in range(len(values))):
            return False
        elif len(_day) > 2 or len(_month) > 2 or len(_year) > 4:
            return False
        elif not all(values[i].isdigit() for i in range(len(values))):
            return False
        elif not 1 <= int(_day) <= 31 or not 1 <= int(_month) <= 12 or not 1 <= int(_year) <= 9999:
            return False
        else:
            return True


def __is_leap_year(value: int):
    if value % 400 == 0:
        return True
    elif value % 100 == 0:
        return False
    elif value % 4 == 0:
        return True
    else:
        return False


def date_exist(value: str):
    days_leap_year = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    days_leap_non_year = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if not __is_valid(value):
        return False
    else:
        day, month, year = map(int, value.split('.'))
        if __is_leap_year(year):
            return True if day <= days_leap_year.get(month) else False
        else:
            return True if day <= days_leap_non_year.get(month) else False


if __name__ == '__main__':
    print(date_exist(input('Введите дату в формате DD.MM.YYYY: ')))
