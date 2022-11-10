from game import Coordinate
from game.utils import (
    DIRECTION_FACE_MAP,
    Directions,
    Faces,
)


class Robot:
    _coordinate = None
    _facing = Faces.NORTH

    def __init__(self, x=0, y=0, facing=Faces.NORTH):
        self._facing = facing
        self._coordinate = Coordinate(x, y)

    def __str__(self):
        return f"{self._coordinate.x},{self._coordinate.y},{self._facing.value.upper()}"

    @property
    def x(self):
        return self._coordinate.x

    @x.setter
    def x(self, value):
        self._coordinate.x = value

    @property
    def y(self):
        return self._coordinate.y

    @y.setter
    def y(self, value):
        self._coordinate.y = value

    @property
    def facing(self):
        return self._facing

    def update(self, x=None, y=None, facing=None):
        self._coordinate.x = x if x is not None else self._coordinate.x
        self._coordinate.y = y if y is not None else self._coordinate.y
        self._facing = facing if facing is not None else _facing

    def right(self):
        self._facing = DIRECTION_FACE_MAP[self._facing][Directions.RIGHT]
        return self._facing

    def left(self):
        self._facing = DIRECTION_FACE_MAP[self._facing][Directions.LEFT]
        return self._facing

    def move(self, commit=True):
        x = self.x
        y = self.y

        if self._facing == Faces.NORTH:
            y += 1
        elif self._facing == Faces.SOUTH:
            y -= 1
        elif self._facing == Faces.EAST:
            x += 1
        elif self._facing == Faces.WEST:
            x -= 1

        if commit:
            self._coordinate.x = x
            self._coordinate.y = y

        return (x, y)

    def report(self):
        return str(self)
