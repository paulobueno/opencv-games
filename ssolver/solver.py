import itertools


class Sudoku:
    def __init__(self, game_values=None):
        self.game = self.create_empty_game()
        if game_values:
            self.import_game(game_values)
        self.show()

    @staticmethod
    def create_empty_game():
        game = [[0] * 9 for _ in range(9)]
        return game

    def update(self, row, column, value):
        self.game[row][column] = value
        return self.game[row][column]

    def get_value(self, row, column):
        return self.game[row][column]

    def get_row_values(self, row):
        return self.game[row]

    def get_column_values(self, column):
        return [row_values[column] for row_values in self.game]

    def get_square_values(self, row, column):
        trunc_row = (row // 3)*3
        trunc_column = (column // 3)*3
        rows = range(trunc_row, trunc_row + 3)
        columns = range(trunc_column, trunc_column + 3)
        addresses = itertools.product(rows, columns)
        return [self.get_value(row, column) for row, column in addresses]

    def import_game(self, game_values):
        clean_game = [int(number) for number in game_values
                      if number.isnumeric()]
        clean_game.reverse()
        for i in range(9):
            for j in range(9):
                self.update(i, j, clean_game.pop())
        return self.game

    def check_valid_insertion(self, row, column, value):
        if value in self.get_row_values(row):
            return False
        if value in self.get_column_values(column):
            return False
        if value in self.get_square_values(row, column):
            return False
        return True

    def solve(self):
        for row in range(9):
            for column in range(9):
                if self.get_value(row, column) == 0:
                    for value in range(1, 10):
                        if self.check_valid_insertion(row, column, value):
                            self.update(row, column, value)
                            self.solve()
                            self.update(row, column, 0)
                    return
        print('Completed')
        self.show()
        input('More?')

    def show(self):
        for row in self.game:
            print(row)


if __name__ == '__main__':
    game_values = \
        "000600005439000000006074000007000900090000087000001000604000000058030002000580070"
    game = Sudoku(game_values)
    game.solve()

