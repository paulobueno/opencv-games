import itertools
import unittest
import img_transform.img_loader as ii


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.game_name = 'sudoku_example.jpg'
        cls.first_number_array = None
        cls.game_numbers = """
                030000100500096020280340000
                094000800025879043076530912
                900600000000083501050000036
                """

    def setUp(self) -> None:
        self.game = ii.Identify(self.game_name)

    def tearDown(self) -> None:
        self.game = None

    def test_image_loaded(self):
        game = ii.Identify(self.game_name, auto_load=False)
        game.load_image()
        self.assertIsNotNone(game.loaded_image)

    def test_sudoku_x_lines_number(self):
        x = len(self.game.get_clean_rho(axis=1))
        self.assertGreaterEqual(10, x)

    def test_sudoku_y_lines_number(self):
        y = len(self.game.get_clean_rho(axis=0))
        self.assertGreaterEqual(10, y)

    def test_image_crop_as_square(self):
        shape = self.game.loaded_image.shape
        self.assertAlmostEqual(shape[0], shape[1], delta=10)

    def test_get_each_number(self):
        for number_coord in itertools.product(range(9), range(9)):
            number = len(self.game.get_number(number_coord))
            self.assertGreater(number, 0)


if __name__ == '__main__':
    unittest.main()
