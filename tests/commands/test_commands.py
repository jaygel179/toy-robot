import unittest
from unittest.mock import MagicMock

from commands import (
    CommandTypes,
    LeftCommand,
    MoveCommand,
    PlaceCommand,
    ReportCommand,
    RightCommand,
)
from utilities.utils import Faces


class PlaceCommandTests(unittest.TestCase):
    def test_defaults(self):
        command = PlaceCommand()

        self.assertEqual(command.type, CommandTypes.PLACE)
        self.assertEqual(command.x, 0)
        self.assertEqual(command.y, 0)
        self.assertEqual(command.face, Faces.NORTH)

    def test_params_given(self):
        command = PlaceCommand(1, 2, Faces.SOUTH)

        self.assertEqual(command.type, CommandTypes.PLACE)
        self.assertEqual(command.x, 1)
        self.assertEqual(command.y, 2)
        self.assertEqual(command.face, Faces.SOUTH)

    def test_str(self):
        command = PlaceCommand(1, 2, Faces.SOUTH)

        self.assertTrue(str(command), "1,2,SOUTH")

    def test_apply_without_game(self):
        command = PlaceCommand(1, 2, Faces.SOUTH)

        res = command.apply(None)

        self.assertIsNone(res)

    def test_apply_without_game(self):
        mock_game = MagicMock()
        command = PlaceCommand(1, 2, Faces.SOUTH)

        res = command.apply(mock_game)

        self.assertIsNotNone(res)
        self.assertTrue(mock_game.place.called)


class MoveCommandTests(unittest.TestCase):
    def test_default(self):
        command = MoveCommand()

        self.assertEqual(command.type, CommandTypes.MOVE)

    def test_str(self):
        command = MoveCommand()

        self.assertTrue(str(command), "MOVE")

    def test_apply_without_game(self):
        command = MoveCommand()

        res = command.apply(None)

        self.assertIsNone(res)

    def test_apply_without_game(self):
        mock_game = MagicMock()
        command = MoveCommand()

        res = command.apply(mock_game)

        self.assertIsNotNone(res)
        self.assertTrue(mock_game.move.called)


class LeftCommandTests(unittest.TestCase):
    def test_default(self):
        command = LeftCommand()

        self.assertEqual(command.type, CommandTypes.LEFT)

    def test_str(self):
        command = LeftCommand()

        self.assertTrue(str(command), "MOVE")

    def test_apply_without_game(self):
        command = LeftCommand()

        res = command.apply(None)

        self.assertIsNone(res)

    def test_apply_without_game(self):
        mock_game = MagicMock()
        command = LeftCommand()

        res = command.apply(mock_game)

        self.assertIsNotNone(res)
        self.assertTrue(mock_game.left.called)


class RightCommandTests(unittest.TestCase):
    def test_default(self):
        command = RightCommand()

        self.assertEqual(command.type, CommandTypes.RIGHT)

    def test_str(self):
        command = RightCommand()

        self.assertTrue(str(command), "MOVE")

    def test_apply_without_game(self):
        command = RightCommand()

        res = command.apply(None)

        self.assertIsNone(res)

    def test_apply_without_game(self):
        mock_game = MagicMock()
        command = RightCommand()

        res = command.apply(mock_game)

        self.assertIsNotNone(res)
        self.assertTrue(mock_game.right.called)


class ReportCommandTests(unittest.TestCase):
    def test_default(self):
        command = ReportCommand()

        self.assertEqual(command.type, CommandTypes.REPORT)

    def test_str(self):
        command = ReportCommand()

        self.assertTrue(str(command), "MOVE")

    def test_apply_without_game(self):
        command = ReportCommand()

        res = command.apply(None)

        self.assertIsNone(res)

    def test_apply_without_game(self):
        mock_game = MagicMock()
        command = ReportCommand()

        res = command.apply(mock_game)

        self.assertIsNotNone(res)
        self.assertTrue(mock_game.report.called)
