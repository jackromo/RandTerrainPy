import unittest
from randterrainpy import *


class Terrain2DTester(unittest.TestCase):

    def setUp(self):
        self.ter1 = Terrain(100, 100)   # all black
        self.ter2 = Terrain(200, 200)   # all white
        for x in range(self.ter2.width):
            for y in range(self.ter2.length):
                self.ter2[x, y] = 1
        self.ter3 = Terrain(100, 100)   # main diagonal is increasing brightness downwards
        for x in range(self.ter3.width):
            for y in range(self.ter3.length):
                if x == y:
                    self.ter3[x, y] = float(y) / self.ter1.length
        self.ter4 = Terrain(200, 100)   # checkerboard pattern
        for x in range(self.ter4.width):
            for y in range(self.ter4.length):
                self.ter4[x, y] = 1 if (x + y) % 2 == 0 else 0

    def test_display(self):
        self.ter1.display_2d()
        self.assertEqual(input("Was the display all black? (y/n): "), "y")
        self.ter2.display_2d()
        self.assertEqual(input("Was the display all white? (y/n): "), "y")
        self.ter3.display_2d()
        self.assertEqual(input("Did the display have a whitening diagonal downwards? (y/n): "), "y")
        self.ter4.display_2d()
        self.assertEqual(input("Was the display a checkerboard? (y/n): "), "y")


class Terrain3DTester(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
