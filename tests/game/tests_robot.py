import unittest
from collections import namedtuple

from game import Robot
from game.utils import Directions
from utilities.utils import Faces

MoveCase = namedtuple("MoveCase", ["x", "y", "face", "expected"])
TurnCase = namedtuple("TurnCase", ["face", "direction", "expected"])


class RobotTests(unittest.TestCase):
    def test_defaults(self):
        robot = Robot()

        self.assertEqual(robot.x, 0)
        self.assertEqual(robot.y, 0)
        self.assertEqual(robot.facing, Faces.NORTH)

    def test_values_given(self):
        robot = Robot(1, 2, Faces.SOUTH)

        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 2)
        self.assertEqual(robot.facing, Faces.SOUTH)

    def test_update(self):
        robot = Robot()

        robot.update(1, 2, Faces.SOUTH)

        self.assertEqual(robot.x, 1)
        self.assertEqual(robot.y, 2)
        self.assertEqual(robot.facing, Faces.SOUTH)

    def test_turns(self):
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
            TurnCase(
                face=Faces.SOUTH,
                direction=Directions.LEFT,
                expected=Faces.EAST,
            ),
            TurnCase(
                face=Faces.SOUTH,
                direction=Directions.RIGHT,
                expected=Faces.WEST,
            ),
            TurnCase(
                face=Faces.EAST,
                direction=Directions.LEFT,
                expected=Faces.NORTH,
            ),
            TurnCase(
                face=Faces.EAST,
                direction=Directions.RIGHT,
                expected=Faces.SOUTH,
            ),
            TurnCase(
                face=Faces.WEST,
                direction=Directions.LEFT,
                expected=Faces.SOUTH,
            ),
            TurnCase(
                face=Faces.WEST,
                direction=Directions.RIGHT,
                expected=Faces.NORTH,
            ),
        ]

        for turn_case in turn_cases:
            robot = Robot(facing=turn_case.face)

            if turn_case.direction == Directions.LEFT:
                robot.left()
            elif turn_case.direction == Directions.RIGHT:
                robot.right()

            self.assertEqual(robot.facing, turn_case.expected)

    def test_moves(self):
        move_cases = [
            MoveCase(x=1, y=1, face=Faces.NORTH, expected=(1, 2)),
            MoveCase(x=1, y=1, face=Faces.SOUTH, expected=(1, 0)),
            MoveCase(x=1, y=1, face=Faces.EAST, expected=(2, 1)),
            MoveCase(x=1, y=1, face=Faces.WEST, expected=(0, 1)),
        ]

        for move_case in move_cases:
            robot = Robot(move_case.x, move_case.y, move_case.face)

            robot.move()

            self.assertEqual((robot.x, robot.y), move_case.expected)

    def test_report(self):
        robot = Robot(1, 2, Faces.SOUTH)

        self.assertEqual(robot.report(), "1,2,SOUTH")
