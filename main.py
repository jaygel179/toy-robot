from commands import (
    CommandParser,
    CommandTypes,
)
from exceptions import FileReaderException
from file_io.handler import InputOutputHandler
from game import Game


class GameRunner:
    _game = None
    _file_io = None
    _reports = []
    _errors = []

    def __init__(self):
        self._game = Game()
        self.file_io = InputOutputHandler()
        self._reports = []

    def run_file(self, file_location=None):
        try:
            raw_commands = self.file_io.read(file_location)
        except FileReaderException as e:
            self.file_io.write(e)
            return

        self.run_string_commands(raw_commands)

    def run_string_commands(self, raw_commands=[]):
        command_parser = CommandParser()
        command_parser.parse(raw_commands)
        commands = command_parser.get_commands()
        self._errors = command_parser.get_errors()
        self.show_errors()
        self.run_commands(commands)

    def run_commands(self, commands=[]):
        for command in commands:
            self._apply_command(command)

    def _apply_command(self, command):
        res = command.apply(self._game)
        # showing all commands
        self.file_io.write(f"{command}")

        if command.type == CommandTypes.REPORT and res is not None:
            output = f"Output: {res}"
            self.file_io.write(output)
            self._reports.append(output)

    def get_reports(self):
        return self._reports

    def get_errors(self):
        return self._errors

    def show_errors(self):
        if self._errors:
            self.file_io.write("-" * 99)
            self.file_io.write("Errors:")
            for error in self._errors:
                self.file_io.write(f"> {error}")
            self.file_io.write("-" * 99)


if __name__ == "__main__":
    game_runner = GameRunner()
    game_runner.run_file("sample_input.txt")
