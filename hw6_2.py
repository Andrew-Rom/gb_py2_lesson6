"""
HW 6_2
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
Напишите функцию в шахматный модуль.

Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""

import random


def is_valid_coordinate(values):
    for value in values:
        if value[0] > 8 or value[0] < 1 or value[1] > 8 or value[1] < 1:
            return False
    else:
        return True


def eight_figures(places):
    """The function of checking the placement of 8 queens on the board 8 by 8"""
    figures = {}
    figure_coordinate = {}
    for i, place in enumerate(places, start=1):
        figures.update({i: place})

    field = [[0 for _ in range(8)] for _ in range(8)]

    for key, value in figures.items():
        x = value[0] - 1
        y = value[1] - 1
        coordinates = []
        for i in range(8):
            coordinates.append((i, y))
            coordinates.append((x, i))
            xx, yy = x, y
            while 0 <= xx < len(field) and 0 <= yy < len(field[0]):
                coordinates.append((xx, yy))
                xx += 1
                yy += 1
            xx, yy = x, y
            while 0 <= xx < len(field) and 0 <= yy < len(field[0]):
                coordinates.append((xx, yy))
                xx += 1
                yy -= 1
            xx, yy = x, y
            while 0 <= xx < len(field) and 0 <= yy < len(field[0]):
                coordinates.append((xx, yy))
                xx -= 1
                yy += 1
            xx, yy = x, y
            while 0 <= xx < len(field) and 0 <= yy < len(field[0]):
                coordinates.append((xx, yy))
                xx -= 1
                yy -= 1
        figure_coordinate.update({key: coordinates})

    for key, value in figures.items():
        x = value[0] - 1
        y = value[1] - 1
        for fig_key, fig_value in figure_coordinate.items():
            if key != fig_key:
                for i in range(0, len(fig_value)):
                    if x == fig_value[i][0] and y == fig_value[i][1]:
                        return False
    else:
        return True


def gen_combinations():
    """The function of generating the list of coordinates of 8 queens"""
    combination = []
    used_x = []
    used_y = []
    counter = 0
    while counter < 8:
        x = random.randint(1, 8)
        y = random.randint(1, 8)
        if len(combination) == 0:
            combination.append((x, y))
            counter += 1
            used_x.append(x)
            used_y.append(y)
        else:
            if x not in used_x and y not in used_y:
                combination.append((x, y))
                counter += 1
                used_x.append(x)
                used_y.append(y)
    return combination


def gen_init():
    """The function of searching of 4 success generated combinations of placements"""
    counter = 0
    while counter < 4:
        value = gen_combinations()
        if eight_figures(value):
            print(value)
            counter += 1


if __name__ == '__main__':
    # # True
    # value = [(1, 3), (2, 6), (3, 4), (4, 1), (5, 8), (6, 5), (7, 7), (8, 2)]
    #
    # # False
    # # value = [(1, 2), (2, 8), (3, 6), (4, 3), (4, 4), (5, 1), (8, 3), (7, 5)]
    #
    # print(eight_figures(value))

    gen_init()
