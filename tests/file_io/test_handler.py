import os
import unittest
from unittest.mock import patch

from exceptions import FileReaderException
from file_io.handler import InputOutputHandler


class InputOutputHandlerTests(unittest.TestCase):
    def setUp(self):
        super(InputOutputHandlerTests, self).setUp()

        self.file_handler = InputOutputHandler()
        self.path = os.path.dirname(os.path.realpath(__file__))

    def test_read_with_file_not_found(self):
        with self.assertRaises(FileReaderException):
            data = self.file_handler.read(
                os.path.join(self.path, "resources/not_found.txt")
            )

    def test_read(self):
        data = self.file_handler.read(
            os.path.join(self.path, "resources/input.txt")
        )

        self.assertEqual(data, ["PLACE 1,2,SOUTH", "REPORT"])

    @patch("builtins.print")
    def test_write(self, mock_print):
        self.file_handler.write("OUTPUT: 1,2,SOUTH")

        self.assertTrue(mock_print.called)

        mock_print.assert_called_with("OUTPUT: 1,2,SOUTH")
