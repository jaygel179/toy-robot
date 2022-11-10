import unittest

from game import Coordinate


class CoordinateTests(unittest.TestCase):
    def test_defaults(self):
        coordinate = Coordinate()

        self.assertEqual(coordinate.value(), (0, 0))

    def test_values_given(self):
        coordinate = Coordinate(x=1, y=2)

        self.assertEqual(coordinate.value(), (1, 2))

    def test_setters(self):
        coordinate = Coordinate()

        coordinate.x = 2
        coordinate.y = 3

        self.assertEqual(coordinate.value(), (2, 3))

    def test_getters(self):
        coordinate = Coordinate(3, 4)

        x = coordinate.x
        y = coordinate.y

        self.assertEqual((x, y), (3, 4))
