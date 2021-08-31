import unittest

import identifier.img_loader


class MyTestCase(unittest.TestCase):
    game = identifier.img_loader.Identify('sudoku_example.jpg')
    game_numbers = """
    030000100500096020280340000
    094000800025879043076530912
    900600000000083501050000036
    """

    def test_image_loaded(self):
        self.game.load_image()
        self.assertIsNotNone(self.game.loaded_image)

    def test_sudoku_lines_located(self):
        """
        sudoku is recognize when there are 10 parallel vertical lines
        and 10 parallel horizontal lines, having in between them
        numbers from 1 to 9 or blank spaces
        :return:
        """
        qty_vl = len(self.game.get_vertical_lines())
        qty_hl = len(self.game.get_horizontal_lines())
        self.assertEqual(20, qty_vl + qty_hl)

if __name__ == '__main__':
    unittest.main()
