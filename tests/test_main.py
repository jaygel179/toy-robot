import os
import unittest

from commands import (
    MoveCommand,
    PlaceCommand,
    ReportCommand,
    RightCommand,
)
from main import GameRunner
from utilities.utils import Faces


class GameRunnerTests(unittest.TestCase):
    def setUp(self):
        super(GameRunnerTests, self).setUp()

        self.path = os.path.dirname(os.path.realpath(__file__))

    def test_run_not_found_file(self):
        game_runner = GameRunner()
        file_location = os.path.join(self.path, "resources/not_found.txt")

        game_runner.run_file(file_location)

        self.assertEqual(len(game_runner.get_reports()), 0)

    def test_run_empty_file_path(self):
        game_runner = GameRunner()
        file_location = os.path.join(self.path, "")

        game_runner.run_file(file_location)

        self.assertEqual(len(game_runner.get_reports()), 0)

    def test_run_file(self):
        file_location = os.path.join(self.path, "resources/input1.txt")
        game_runner = GameRunner()

        game_runner.run_file(file_location)
        reports = game_runner.get_reports()

        self.assertEqual(len(reports), 1)

    def test_run_string_commands(self):
        raw_commands = [
            "PLACE 0,0,NORTH",
            "MOVE",
            "RIGHT",
            "MOVE",
            "REPORT",
        ]
        game_runner = GameRunner()

        game_runner.run_string_commands(raw_commands)
        reports = game_runner.get_reports()

        self.assertEqual(len(reports), 1)
        self.assertEqual(reports[0], "Output: 1,1,EAST")

    def test_run_commands(self):
        commands = [
            PlaceCommand(1, 1, Faces.SOUTH),
            MoveCommand(),
            RightCommand(),
            MoveCommand(),
            ReportCommand(),
        ]
        game_runner = GameRunner()

        game_runner.run_commands(commands)
        reports = game_runner.get_reports()

        self.assertEqual(len(reports), 1)
        self.assertEqual(reports[0], "Output: 0,0,WEST")
