import os
import unittest

from main import GameRunner


class IntegrationTests(unittest.TestCase):
    def setUp(self):
        super(IntegrationTests, self).setUp()

        self.path = os.path.dirname(os.path.realpath(__file__))

    def test_input_1(self):
        game_runner = GameRunner()
        file_location = os.path.join(self.path, "resources/input1.txt")

        game_runner.run_file(file_location)
        reports = game_runner.get_reports()

        self.assertEqual(len(reports), 1)
        self.assertEqual(reports[0], "Output: 0,1,NORTH")

    def test_input_2(self):
        game_runner = GameRunner()
        file_location = os.path.join(self.path, "resources/input2.txt")

        game_runner.run_file(file_location)
        reports = game_runner.get_reports()

        self.assertEqual(len(reports), 1)
        self.assertEqual(reports[0], "Output: 0,0,WEST")

    def test_input_3(self):
        game_runner = GameRunner()
        file_location = os.path.join(self.path, "resources/input3.txt")

        game_runner.run_file(file_location)
        reports = game_runner.get_reports()

        self.assertEqual(len(reports), 1)
        self.assertEqual(reports[0], "Output: 3,3,NORTH")

    def test_input_stress(self):
        game_runner = GameRunner()
        file_location = os.path.join(self.path, "resources/input_stress.txt")

        game_runner.run_file(file_location)
        reports = game_runner.get_reports()

        self.assertEqual(len(reports), 18)
        self.assertEqual(reports[0], "Output: 0,0,NORTH")  # place 0,0,NORTH
        self.assertEqual(reports[1], "Output: 0,1,NORTH")  # move
        self.assertEqual(reports[2], "Output: 0,1,EAST")  # right
        self.assertEqual(reports[3], "Output: 1,1,EAST")  # move
        self.assertEqual(reports[4], "Output: 1,1,NORTH")  # left
        self.assertEqual(reports[5], "Output: 1,2,NORTH")  # move
        self.assertEqual(reports[6], "Output: 1,2,WEST")  # left
        self.assertEqual(reports[7], "Output: 0,2,WEST")  # move
        self.assertEqual(reports[8], "Output: 0,2,SOUTH")  # left
        self.assertEqual(reports[9], "Output: 0,1,SOUTH")  # move
        self.assertEqual(reports[10], "Output: 0,0,SOUTH")  # place 0,0,SOUTH
        self.assertEqual(reports[11], "Output: 0,0,SOUTH")  # move (should not fall from table)
        self.assertEqual(reports[12], "Output: 0,4,WEST")  # place 0,0,SOUTH
        self.assertEqual(reports[13], "Output: 0,4,WEST")  # move (should not fall from table)
        self.assertEqual(reports[14], "Output: 4,4,NORTH")  # place 4,4,NORTH
        self.assertEqual(reports[15], "Output: 4,4,NORTH")  # move (should not fall from table)
        self.assertEqual(reports[16], "Output: 4,0,EAST")  # place 4,0,EAST
        self.assertEqual(reports[17], "Output: 4,0,EAST")  # move (should not fall from table)
