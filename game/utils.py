from enum import Enum

from utilities.utils import Faces


class Directions(Enum):
    LEFT = "left"
    RIGHT = "right"


# Dictionary that will determine the next facing direction
DIRECTION_FACE_MAP = {
    Faces.NORTH: {
        Directions.LEFT: Faces.WEST,
        Directions.RIGHT: Faces.EAST,
    },
    Faces.SOUTH: {
        Directions.LEFT: Faces.EAST,
        Directions.RIGHT: Faces.WEST,
    },
    Faces.EAST: {
        Directions.LEFT: Faces.NORTH,
        Directions.RIGHT: Faces.SOUTH,
    },
    Faces.WEST: {
        Directions.LEFT: Faces.SOUTH,
        Directions.RIGHT: Faces.NORTH,
    },
}
