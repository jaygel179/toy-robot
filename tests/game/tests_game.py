import unittest
from collections import namedtuple

from game import Game
from game.utils import Directions
from utilities.utils import Faces

MoveCase = namedtuple("MoveCase", ["x", "y", "face", "expected"])
TurnCase = namedtuple("TurnCase", ["face", "direction", "expected"])


class GameTests(unittest.TestCase):
    def test_default(self):
        game = Game()

        self.assertIsNotNone(game.table)
        self.assertEqual(game.table.length, 5)
        self.assertEqual(game.table.width, 5)

    def test_place_with_default_params(self):
        game = Game()

        game.place()

        self.assertIsNotNone(game.robot)
        self.assertEqual(game.robot.x, 0)
        self.assertEqual(game.robot.y, 0)
        self.assertEqual(game.robot.facing, Faces.NORTH)

    def test_place_with_params_given(self):
        game = Game()

        game.place(1, 2, Faces.SOUTH)

        self.assertIsNotNone(game.robot)
        self.assertEqual(game.robot.x, 1)
        self.assertEqual(game.robot.y, 2)
        self.assertEqual(game.robot.facing, Faces.SOUTH)

    def test_place_with_invalid_location_given(self):
        game = Game()

        game.place(-1, -1, Faces.SOUTH)

        self.assertIsNone(game.robot)

    def test_place_performed_twice(self):
        game = Game()

        game.place(1, 2, Faces.SOUTH)
        game.place(2, 3, Faces.EAST)

        self.assertIsNotNone(game.robot)
        self.assertEqual(game.robot.x, 2)
        self.assertEqual(game.robot.y, 3)
        self.assertEqual(game.robot.facing, Faces.EAST)

    def test_move_without_robot(self):
        game = Game()

        res = game.move()

        self.assertIsNone(res)

    def test_move_with_robot(self):
        move_cases = [
            MoveCase(x=1, y=1, face=Faces.NORTH, expected=(1, 2)),
            MoveCase(x=1, y=1, face=Faces.SOUTH, expected=(1, 0)),
            MoveCase(x=1, y=1, face=Faces.EAST, expected=(2, 1)),
            MoveCase(x=1, y=1, face=Faces.WEST, expected=(0, 1)),
        ]

        for move_case in move_cases:
            game = Game()
            game.place(move_case.x, move_case.y, move_case.face)

            res = game.move()

            self.assertEqual(res, move_case.expected)

    def test_turn_without_robot(self):
        for turn in [Directions.LEFT, Directions.RIGHT]:
            game = Game()

            if turn == Directions.LEFT:
                res = game.left()
            else:
                res = game.right()

            self.assertIsNone(res)

    def test_turn_with_robot(self):
        turn_cases = [
            TurnCase(
                face=Faces.NORTH,
                direction=Directions.LEFT,
                expected=Faces.WEST,
            ),
            TurnCase(
                face=Faces.NORTH,
                direction=Directions.RIGHT,
                expected=Faces.EAST,
            ),
        ]

        for turn_case in turn_cases:
            game = Game()
            game.place(facing=turn_case.face)

            if turn_case.direction == Directions.LEFT:
                res = game.left()
            else:
                res = game.right()

            self.assertEqual(res, turn_case.expected)

    def test_report_without_robot(self):
        game = Game()

        res = game.report()

        self.assertIsNone(res)

    def test_report_with_robot(self):
        game = Game()
        game.place()

        res = game.report()

        self.assertEqual(res, "0,0,NORTH")
