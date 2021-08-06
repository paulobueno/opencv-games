import itertools as it
from collections import Counter

import numpy as np


def check_missing(array):
    look_values = range(1, 10)
    remain_values = [value for value in look_values if
                     value not in array.flatten()]
    return remain_values


def print_sudoku(game_array):
    template = '|' + 3 * '{:^3.0f}'
    row_template = 3 * template
    line_template = '+' + 9 * '-'
    print(3 * line_template + '+')
    for i in range(3):
        for j in range(3):
            row = game_array[i, :, j, :].flatten()
            print(row_template.format(*row) + '|')
        print(3 * line_template + '+')
    return None


def poss_dict(game):
    keys = list(it.product(*4 * [[0, 1, 2]]))
    values = list(range(1, 10))
    poss = {key: values for key in keys}
    for location in poss.keys():
        i, j, ii, jj = location
        if game[location] != 0:
            poss[location] = []
            continue
        missing_square = set(check_missing(game[i, j, :, :]))
        missing_row = set(check_missing(game[i, :, ii, :]))
        missing_column = set(check_missing(game[:, j, :, jj]))
        poss[location] = list(set.intersection(missing_square, missing_row,
                                               missing_column))
    return poss


def poss_square(poss):
    ij = list(it.product(*2 * [[0, 1, 2]]))
    for i, j in ij:
        values = [v for k, v in poss.items() if
                  k[0] == i and k[1] == j and len(v) > 0]
        c = Counter(values)
        unique_values = [k for k, v in c.items() if v == 1]
        for ii, jj in ij:
            if poss[i, j, ii, jj] in unique_values:
                poss[i, j, ii, jj] = list(
                        set(poss[i, j, ii, jj]) & set(unique_values))
    return poss


def fill_game(game):
    poss = poss_dict(game)
    poss = poss_square(poss)
    for k, v in poss.items():
        if len(v) == 1 and game[k] == 0:
            game[k] = v[0]
    return game


square = np.zeros((3, 3))
line = [square for _ in range(3)]
game = [line for _ in range(3)]
game = np.asarray(game)
game[0, 0] = [[0, 2, 1], [0, 3, 5], [0, 4, 8]]
game[0, 1] = [[4, 7, 0], [6, 1, 8], [0, 0, 9]]
game[0, 2] = [[5, 9, 8], [7, 2, 0], [0, 0, 0]]
game[1, 0] = [[1, 0, 9], [2, 0, 0], [0, 0, 7]]
game[1, 1] = [[0, 0, 0], [1, 0, 0], [0, 0, 6]]
game[1, 2] = [[4, 7, 0], [8, 0, 3], [0, 0, 0]]
game[2, 0] = [[8, 0, 0], [0, 0, 2], [0, 0, 0]]
game[2, 1] = [[0, 0, 0], [7, 3, 0], [0, 6, 2]]
game[2, 2] = [[0, 3, 0], [0, 0, 0], [9, 0, 7]]

game = fill_game(game)
print_sudoku(game)
