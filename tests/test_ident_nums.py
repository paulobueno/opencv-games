import unittest

import identifier.ident_nums


class MyTestCase(unittest.TestCase):
    game = identifier.ident_nums.Identify('sudoku_example.jpg')

    def test_image_loaded(self):
        self.game.load_image()
        self.assertIsNotNone(self.game.loaded_image)

    def test_image_preview(self):
        self.assertEqual(ord('y'), self.game.preview(test=True))


if __name__ == '__main__':
    unittest.main()
