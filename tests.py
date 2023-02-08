import unittest

from functions import game_grid


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here

    def game_grid_test(self):

        self.assertEqual(game_grid("3X3XXXO0O"),open("game_grid_test.txt", "r"))




if __name__ == '__main__':
    unittest.main()
