import unittest

import ssolver.solver as s2


class MyTestCase(unittest.TestCase):
    game_test = """
    051090026
    900817000
    400000001
    060402010
    300001000
    007038204
    000000470
    030500100
    000700530
    """

    def test_create_empty_game(self):
        game = s2.Sudoku().game
        result = True
        for row in game:
            if len(row) != 9:
                result = False
            for number in row:
                if number != 0:
                    result = False
        if len(game) != 9:
            result = False
        self.assertEqual(result, True)

    def test_update_number_in_game(self):
        test_value = 8
        game = s2.Sudoku()
        game.update(0, 0, test_value)
        value = game.get_value(0, 0)
        self.assertEqual(value, test_value)

    def test_import_game(self):
        game = s2.Sudoku(self.game_test)
        self.assertEqual(9, game.get_value(1, 0))

    def test_check_valid_insertion_row(self):
        game = s2.Sudoku(self.game_test)
        self.assertEqual(False, game.check_valid_insertion(0, 0, 2))

    def test_check_valid_insertion_column(self):
        game = s2.Sudoku(self.game_test)
        self.assertEqual(False, game.check_valid_insertion(1, 1, 6))

    def test_check_valid_insertion_square(self):
        game = s2.Sudoku(self.game_test)
        self.assertEqual(False, game.check_valid_insertion(1, 1, 4))


if __name__ == '__main__':
    unittest.main()
