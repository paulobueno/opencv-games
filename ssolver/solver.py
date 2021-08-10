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
    game[0, 0] = [[0, 2, 1], [0, 3, 5], [0, 4, 8]]
    game[0, 1] = [[4, 7, 0], [6, 1, 8], [0, 0, 9]]
    game[0, 2] = [[5, 9, 8], [7, 2, 0], [0, 0, 0]]
    game[1, 0] = [[1, 0, 9], [2, 0, 0], [0, 0, 7]]
    game[1, 1] = [[0, 0, 0], [1, 0, 0], [0, 0, 6]]
    game[1, 2] = [[4, 7, 0], [8, 0, 3], [0, 0, 0]]
    game[2, 0] = [[8, 0, 0], [0, 0, 2], [0, 0, 0]]
    game[2, 1] = [[0, 0, 0], [7, 3, 0], [0, 6, 2]]
    game[2, 2] = [[0, 3, 0], [0, 0, 0], [9, 0, 7]]
    return game


class Sudoku:

    def __init__(self, game=None):
        if not game:
            game = mockup_game()
        self.game = game
        self.options = self._gen_all_opts()

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