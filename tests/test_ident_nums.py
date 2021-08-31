import unittest

import identifier.database_creator


class MyTestCase(unittest.TestCase):
    game = identifier.database_creator.Identify('sudoku_example.jpg')

    def test_image_loaded(self):
        self.game.load_image()
        self.assertIsNotNone(self.game.loaded_image)

    def test_image_preview(self):
        self.assertEqual(ord('y'), self.game.preview(test=True))


if __name__ == '__main__':
    unittest.main()
