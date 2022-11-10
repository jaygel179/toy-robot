import unittest

from commands import (
    CommandParser,
    CommandTypes,
    PlaceCommand,
)
from utilities.utils import Faces

PLACE_COMMAND_PARSER_PARAM_X = PlaceCommand.params_parser()[0]
PLACE_COMMAND_PARSER_PARAM_Y = PlaceCommand.params_parser()[1]
PLACE_COMMAND_PARSER_PARAM_FACE = PlaceCommand.params_parser()[2]

class CommandParserTests(unittest.TestCase):
    def setUp(self):
        super(CommandParserTests, self).setUp()

        self.parser = CommandParser()

    def test_parse_empty_command(self):
        raw_commands = []

        self.parser.parse(raw_commands)

        self.assertEqual(len(self.parser.get_commands()), 0)
        self.assertEqual(self.parser.get_errors(), ["No raw commands found."])

    def test_valid_command(self):
        raw_commands = ["PLACE 1,2,NORTH"]

        self.parser.parse(raw_commands)

        self.assertEqual(len(self.parser.get_commands()), 1)
        self.assertEqual(self.parser.get_errors(), [])

    def test_empty_string_command(self):
        raw_commands = [""]

        self.parser.parse(raw_commands)

        self.assertEqual(len(self.parser.get_commands()), 0)
        self.assertEqual(self.parser.get_errors(), ["Invalid command: ."])

    def test_invalid_command(self):
        raw_commands = ["UNKNOWN"]

        self.parser.parse(raw_commands)

        self.assertEqual(len(self.parser.get_commands()), 0)
        self.assertEqual(
            self.parser.get_errors(),
            [
                "Invalid command: UNKNOWN. Should be one of the ff: "
                "['PLACE', 'MOVE', 'RIGHT', 'LEFT', 'REPORT']."
            ],
        )

    def test_valid_place_command(self):
        raw_commands = ["PLACE 1,2,NORTH"]

        self.parser.parse(raw_commands)

        self.assertEqual(len(self.parser.get_commands()), 1)
        self.assertEqual(self.parser.get_errors(), [])
        command = self.parser.get_commands()[0]
        self.assertEqual(command.type, CommandTypes.PLACE)
        self.assertEqual(command.x, 1)
        self.assertEqual(command.y, 2)
        self.assertEqual(command.face, Faces.NORTH)

    def test_place_command_parser_param_x_data_type(self):
        raw_commands = ["PLACE 1,2,NORTH"]

        self.parser.parse(raw_commands)

        place_command = self.parser.get_commands()[0]
        self.assertEqual(
            type(place_command.x),
            PLACE_COMMAND_PARSER_PARAM_X.get("type"),
        )

    def test_place_command_parser_param_y_data_type(self):
        raw_commands = ["PLACE 1,2,NORTH"]

        self.parser.parse(raw_commands)

        place_command = self.parser.get_commands()[0]
        self.assertEqual(
            type(place_command.y),
            PLACE_COMMAND_PARSER_PARAM_Y.get("type"),
        )

    def test_place_command_parser_param_face_data_type(self):
        raw_commands = ["PLACE 1,2,NORTH"]

        self.parser.parse(raw_commands)

        place_command = self.parser.get_commands()[0]
        self.assertEqual(
            type(place_command.face),
            PLACE_COMMAND_PARSER_PARAM_FACE.get("type"),
        )

    def test_missing_params_place_command(self):
        raw_commands = ["PLACE"]

        self.parser.parse(raw_commands)

        self.assertEqual(len(self.parser.get_commands()), 0)
        self.assertEqual(
            self.parser.get_errors(), ["Parameter missing for command PLACE."]
        )

    def test_move_command(self):
        raw_commands = ["MOVE"]

        self.parser.parse(raw_commands)

        self.assertEqual(len(self.parser.get_commands()), 1)
        self.assertEqual(self.parser.get_errors(), [])
        command = self.parser.get_commands()[0]
        self.assertEqual(command.type, CommandTypes.MOVE)

    def test_right_command(self):
        raw_commands = ["RIGHT"]

        self.parser.parse(raw_commands)

        self.assertEqual(len(self.parser.get_commands()), 1)
        self.assertEqual(self.parser.get_errors(), [])
        command = self.parser.get_commands()[0]
        self.assertEqual(command.type, CommandTypes.RIGHT)

    def test_left_command(self):
        raw_commands = ["LEFT"]

        self.parser.parse(raw_commands)

        self.assertEqual(len(self.parser.get_commands()), 1)
        self.assertEqual(self.parser.get_errors(), [])
        command = self.parser.get_commands()[0]
        self.assertEqual(command.type, CommandTypes.LEFT)

    def test_report_command(self):
        raw_commands = ["REPORT"]

        self.parser.parse(raw_commands)

        self.assertEqual(len(self.parser.get_commands()), 1)
        self.assertEqual(self.parser.get_errors(), [])
        command = self.parser.get_commands()[0]
        self.assertEqual(command.type, CommandTypes.REPORT)

    def test_combinations_and_invalid_commands_removed(self):
        raw_commands = [
            "PLACE 1,2,NORTH",  #  valid
            "UNKNOWN",  # invalid
            "MOVE",  # valid
            "RIGHT",  # valid
            "",  # invalid
            "PLACE",  # invalid
            "LEFT",  # valid
            "REPORT",  # valid
        ]

        self.parser.parse(raw_commands)

        self.assertEqual(len(self.parser.get_commands()), 5)
        self.assertEqual(len(self.parser.get_errors()), 3)

        # test valid commands
        commands = self.parser.get_commands()
        self.assertEqual(commands[0].type, CommandTypes.PLACE)
        self.assertEqual(commands[1].type, CommandTypes.MOVE)
        self.assertEqual(commands[2].type, CommandTypes.RIGHT)
        self.assertEqual(commands[3].type, CommandTypes.LEFT)
        self.assertEqual(commands[4].type, CommandTypes.REPORT)

        # test error messages
        errors = self.parser.get_errors()
        self.assertEqual(
            errors[0],
            "Invalid command: UNKNOWN. Should be one of the ff: "
            "['PLACE', 'MOVE', 'RIGHT', 'LEFT', 'REPORT'].",
        )
        self.assertEqual(errors[1], "Invalid command: .")
        self.assertEqual(errors[2], "Parameter missing for command PLACE.")
