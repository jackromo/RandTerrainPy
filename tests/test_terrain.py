import unittest
from randterrainpy import *


class TerrainTesterPy(unittest.TestCase):

    def setUp(self):
        self.ter1 = Terrain(1, 1)
        self.ter2 = Terrain(2, 4)
        self.ter3 = Terrain(1, 1)

    def test_getitem(self):
        self.assertEqual(self.ter1[0, 0], 0)
        self.assertEqual(self.ter2[1, 2], 0)

    def test_eq(self):
        self.assertEqual(self.ter1, self.ter3)
        self.assertNotEqual(self.ter1, self.ter2)

    def test_setitem(self):
        self.ter1[0, 0] = 1
        self.assertEqual(self.ter1[0, 0], 1)
        self.ter2[1, 2] = 0.5
        self.assertEqual(self.ter2[1, 2], 0.5)

    def test_add(self):
        self.assertRaises(InvalidDimensionsError, self.ter1.__add__, self.ter2)
        self.assertEqual(self.ter1+self.ter3, self.ter1)


if __name__ == "__main__":
    unittest.main()
