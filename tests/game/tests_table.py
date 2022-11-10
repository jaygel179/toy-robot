import unittest
from collections import namedtuple

from game import (
    Coordinate,
    Table,
)
from utilities.utils import Faces

CoordinateCase = namedtuple("CoordinateCase", ["x", "y", "expected"])


class TableTests(unittest.TestCase):
    def test_defaults(self):
        table = Table()

        self.assertEqual(table.length, 5)
        self.assertEqual(table.width, 5)

    def test_is_valid_coordinate(self):
        coordinate_cases = [
            CoordinateCase(x=-1, y=-1, expected=False),
            CoordinateCase(x=-1, y=0, expected=False),
            CoordinateCase(x=-1, y=1, expected=False),
            CoordinateCase(x=-1, y=2, expected=False),
            CoordinateCase(x=-1, y=3, expected=False),
            CoordinateCase(x=0, y=-1, expected=False),
            CoordinateCase(x=0, y=0, expected=True),
            CoordinateCase(x=0, y=1, expected=True),
            CoordinateCase(x=0, y=2, expected=True),
            CoordinateCase(x=0, y=3, expected=False),
            CoordinateCase(x=1, y=-1, expected=False),
            CoordinateCase(x=1, y=0, expected=True),
            CoordinateCase(x=1, y=1, expected=True),
            CoordinateCase(x=1, y=2, expected=True),
            CoordinateCase(x=1, y=3, expected=False),
            CoordinateCase(x=2, y=-1, expected=False),
            CoordinateCase(x=2, y=0, expected=True),
            CoordinateCase(x=2, y=1, expected=True),
            CoordinateCase(x=2, y=2, expected=True),
            CoordinateCase(x=2, y=3, expected=False),
            CoordinateCase(x=3, y=-1, expected=False),
            CoordinateCase(x=3, y=0, expected=False),
            CoordinateCase(x=3, y=1, expected=False),
            CoordinateCase(x=3, y=2, expected=False),
            CoordinateCase(x=3, y=3, expected=False),
        ]

        for coordinate_case in coordinate_cases:
            table = Table(length=3, width=3)

            result = table.is_valid_coordinate(
                Coordinate(x=coordinate_case.x, y=coordinate_case.y)
            )

            self.assertEqual(result, coordinate_case.expected)
