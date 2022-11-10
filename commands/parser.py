import re

from commands import (
    CommandToClassMap,
    CommandTypes,
)
from exceptions import CommandParserException
from utilities.utils import Faces


class CommandParser:
    _commands = []
    _errors = []

    def parse(self, raw_commands):
        self._commands = []
        self._errors = []

        if not raw_commands:
            self._errors.append("No raw commands found.")
            return

        for raw_command in raw_commands:
            try:
                first_word = self._get_first_word(raw_command)
                command = self._convert_word_to_command(first_word)
                self._parse_command_params(command, raw_command)
                self._commands.append(command)
            except CommandParserException as e:
                self._errors.append(e)

    def get_commands(self):
        return self._commands

    def get_errors(self):
        return [str(error) for error in self._errors]

    def _get_first_word(self, raw_command):
        searches = re.findall(r"^\w+", raw_command)
        if not searches:
            raise CommandParserException(f"Invalid command: {raw_command}.")

        return searches[0]

    def _convert_word_to_command(self, first_word):
        valid_commands = [ct.value for ct in CommandTypes]

        if first_word not in valid_commands:
            raise CommandParserException(
                f"Invalid command: {first_word}. Should be one of the ff: {valid_commands}."
            )

        command = CommandToClassMap.get(CommandTypes[first_word])()
        return command

    def _parse_command_params(self, command, raw_command):
        for param in command.params_parser():
            matches = re.findall(param.get("regex"), raw_command)
            if not matches:
                raise CommandParserException(
                    f"Parameter missing for command {command.type.value}."
                )

            command = self._set_command_params_value(
                command, param.get("name"), param.get("type")(matches[0])
            )

        return command

    def _set_command_params_value(self, command, param_name, value):
        setattr(command, param_name, value)
        return command
