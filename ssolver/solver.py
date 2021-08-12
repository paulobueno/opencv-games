import itertools as it
from collections import Counter

import numpy as np


def check_missing(array):
    """
    Check missing numbers of an array.
    The array can be a row, column or a square,
    where each one has to have 1 to 9, with no duplicated number.
    :param array:
    :return: list of missing numbers
    """
    look_values = range(1, 10)
    remain_values = [value for value in look_values if
                     value not in array.flatten()]
    return remain_values


def mockup_game():
    square = np.zeros((3, 3))
    line = [square for _ in range(3)]
    game = [line for _ in range(3)]
    game = np.asarray(game)
    # game[0, 0] = [[0, 2, 1], [0, 3, 5], [0, 4, 8]]
    # game[0, 1] = [[4, 7, 0], [6, 1, 8], [0, 0, 9]]
    # game[0, 2] = [[5, 9, 8], [7, 2, 0], [0, 0, 0]]
    # game[1, 0] = [[1, 0, 9], [2, 0, 0], [0, 0, 7]]
    # game[1, 1] = [[0, 0, 0], [1, 0, 0], [0, 0, 6]]
    # game[1, 2] = [[4, 7, 0], [8, 0, 3], [0, 0, 0]]
    # game[2, 0] = [[8, 0, 0], [0, 0, 2], [0, 0, 0]]
    # game[2, 1] = [[0, 0, 0], [7, 3, 0], [0, 6, 2]]
    # game[2, 2] = [[0, 3, 0], [0, 0, 0], [9, 0, 7]]
    game[0, 0] = [[3, 7, 0], [0, 2, 9], [0, 0, 0]]
    game[0, 1] = [[1, 4, 0], [6, 7, 3], [0, 9, 0]]
    game[0, 2] = [[9, 6, 0], [1, 0, 0], [0, 7, 4]]
    game[1, 0] = [[0, 0, 2], [7, 4, 0], [1, 0, 0]]
    game[1, 1] = [[5, 0, 0], [0, 0, 0], [0, 2, 0]]
    game[1, 2] = [[0, 0, 0], [0, 0, 8], [7, 0, 0]]
    game[2, 0] = [[9, 0, 0], [0, 5, 7], [6, 1, 0]]
    game[2, 1] = [[7, 6, 2], [3, 0, 1], [0, 0, 0]]
    game[2, 2] = [[0, 3, 1], [6, 0, 9], [0, 0, 7]]
    return game


class Sudoku:

    def __init__(self, game=None):
        if not game:
            game = mockup_game()
        self.game = game
        self.options = self._gen_all_opts()
        self.update_opts()

    def update_opts(self):
        coords = self.options.keys()
        for coord in coords:
            i, j, ii, jj = coord
            value = self.game[i, j, ii, jj]
            if value == 0:
                poss = self.check_opts_rule_one(coord)
                self.options[coord] = poss
                poss = self.check_opts_rule_two(coord)
                self.options[coord] = poss
            else:
                self.options[coord] = []
        return None

    def check_opts_rule_one(self, coord):
        i, j, ii, jj = coord
        opts = self.options[coord]
        row = self.get_row(i, ii)
        column = self.get_column(j, jj)
        square = self.get_square(i, j)
        denied_list = row + column + square
        poss = [num for num in opts if num not in denied_list]
        return poss

    def check_opts_rule_two(self, coord):
        i, j, ii, jj = coord
        original_poss = self.options[coord]
        square_addrs = [a for a in self.options.keys()
                        if a[0] == i and a[1] == j and a != coord]
        poss = []
        for address in square_addrs:
            poss += self.options[address]
        unique = [p for p in original_poss if p not in poss]
        if len(unique) == 1:
            original_poss = unique
        return original_poss

    def print_sudoku(self):
        """
        Print sudoku game as a string in the terminal
        """
        template = '|' + 3 * '{:^3.0f}'
        row_template = 3 * template
        line_template = '+' + 9 * '-'
        print(3 * line_template + '+')
        for i in range(3):
            for j in range(3):
                row = self.game[i, :, j, :].flatten()
                print(row_template.format(*row) + '|')
            print(3 * line_template + '+')
        return None

    @staticmethod
    def _get_valid_numbers(array):
        clean_numbers = [int(number) for number in array.flatten()
                         if number in range(1, 10)]
        return sorted(clean_numbers)

    @staticmethod
    def _gen_all_opts():
        """
        Create a dict with all possible numbers
        (1 to 9) for each possible address
        :return: dict listing all possible options
        """
        keys = list(it.product(*4 * [[0, 1, 2]]))
        values = list(range(1, 10))
        opts = {key: values for key in keys}
        return opts

    def get_row(self, i, ii):
        numbers = self.game[i, :, ii, :]
        return self._get_valid_numbers(numbers)

    def get_column(self, j, jj):
        numbers = self.game[:, j, :, jj]
        return self._get_valid_numbers(numbers)

    def get_square(self, i, j):
        numbers = self.game[i, j, :, :]
        return self._get_valid_numbers(numbers)

    def update_game(self, value, coord):
        i, j, ii, jj = coord
        self.game[i, j, ii, jj] = value
        self.options[coord] = [value]
        return self.game[i, j, ii, jj]

    def fill_by_options(self):
        c = 0
        for coord, value in self.options.items():
            if len(value) == 1:
                c += 1
                v = value[0]
                self.update_game(v, coord)
        self.update_opts()
        return c

    def filler(self):
        c = 0
        while True:
            add = self.fill_by_options()
            c += add
            if add == 0:
                break
        return f'Filled {c} option(s)'
