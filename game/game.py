from game.coordinate import Coordinate
from game.decorators import robot_required
from game.robot import Robot
from game.table import Table
from utilities.utils import Faces


class Game:
    _table = None
    _robot = None

    def __init__(self):
        self._table = Table()

    @property
    def table(self):
        return self._table

    @property
    def robot(self):
        return self._robot

    def place(self, x=0, y=0, facing=Faces.NORTH):
        coordinate = Coordinate(x, y)
        if not self._is_valid_coordinate(coordinate):
            return self._robot

        if self._robot is not None:
            self._robot.update(x=x, y=y, facing=facing)
        else:
            self._robot = Robot(x=x, y=y, facing=facing)

        return self._robot

    @robot_required
    def move(self):
        next_coordinate = Coordinate(*self._robot.move(commit=False))

        if not self._is_valid_coordinate(next_coordinate):
            return (self._robot.x, self._robot.y)

        return self._robot.move(commit=True)

    @robot_required
    def left(self):
        return self._robot.left()

    @robot_required
    def right(self):
        return self._robot.right()

    @robot_required
    def report(self):
        return self._robot.report()

    def _is_valid_coordinate(self, coordinate):
        if not self._table.is_valid_coordinate(coordinate):
            return False

        return True
