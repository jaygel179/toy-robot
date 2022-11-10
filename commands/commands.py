from enum import Enum

from commands.decorators import game_required
from utilities.utils import Faces


class CommandTypes(Enum):
    PLACE = "PLACE"
    MOVE = "MOVE"
    RIGHT = "RIGHT"
    LEFT = "LEFT"
    REPORT = "REPORT"


class BaseCommand:
    _type = None
    _params_parser = []

    @classmethod
    def params_parser(self):
        return self._params_parser

    @property
    def type(self):
        return self._type

    @game_required
    def apply(self, game):
        raise NotImplementedError

    def __str__(self):
        return f"{self._type.value}"


class PlaceCommand(BaseCommand):
    _type = CommandTypes.PLACE
    x = 0
    y = 0
    face = Faces.NORTH

    _params_parser = [
        {"name": "x", "regex": "^\D*([\d]+)", "type": int},
        {"name": "y", "regex": "^\D*[\d]+[\D]+([\d]+)", "type": int},
        {"name": "face", "regex": "(\w+)$", "type": Faces},
    ]

    def __init__(self, x=0, y=0, face=Faces.NORTH):
        self.x = x
        self.y = y
        self.face = face

    def __str__(self):
        return (
            f"{self._type.value} {self.x},{self.y},{self.face.value.upper()}"
        )

    @game_required
    def apply(self, game):
        return game.place(x=int(self.x), y=int(self.y), facing=self.face)


class MoveCommand(BaseCommand):
    _type = CommandTypes.MOVE

    @game_required
    def apply(self, game):
        return game.move()


class LeftCommand(BaseCommand):
    _type = CommandTypes.LEFT

    @game_required
    def apply(self, game):
        return game.left()


class RightCommand(BaseCommand):
    _type = CommandTypes.RIGHT

    @game_required
    def apply(self, game):
        return game.right()


class ReportCommand(BaseCommand):
    _type = CommandTypes.REPORT

    @game_required
    def apply(self, game):
        return game.report()


CommandToClassMap = {
    CommandTypes.PLACE: PlaceCommand,
    CommandTypes.MOVE: MoveCommand,
    CommandTypes.LEFT: LeftCommand,
    CommandTypes.RIGHT: RightCommand,
    CommandTypes.REPORT: ReportCommand,
}
