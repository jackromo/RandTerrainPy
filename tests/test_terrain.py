import unittest
from randterrainpy import *


class TerrainTester(unittest.TestCase):

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
        self.ter1[0, 0] = 0.9
        self.assertEqual(self.ter1[0, 0], 0.9)
        self.ter2[1, 2] = 0.5
        self.assertEqual(self.ter2[1, 2], 0.5)

    def test_add(self):
        self.assertRaises(InvalidDimensionsError, self.ter1.__add__, self.ter2)
        self.assertEqual(self.ter1+self.ter3, self.ter1)
        test_ter = Terrain(1, 1)
        test_ter[0, 0] = 1
        self.assertEqual((self.ter1+test_ter)[0, 0], 1)     # capped at 1

    def test_sub(self):
        self.assertRaises(InvalidDimensionsError, self.ter1.__sub__, self.ter2)
        self.assertEqual(self.ter1-self.ter3, self.ter1)
        test_ter = Terrain(1, 1)
        test_ter[0, 0] = 1
        self.assertEqual((self.ter1-test_ter)[0, 0], 0)     # capped at 0

    def test_mul(self):
        self.assertEqual(self.ter1*0, Terrain(self.ter1.width, self.ter1.length))
        self.assertEqual(self.ter2*1, self.ter2)
        self.assertNotEqual(self.ter2*0.5, self.ter2)


class VoronoiTerrainTester(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
