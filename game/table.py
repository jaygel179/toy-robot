class Table:
    _length = 5
    _width = 5

    def __init__(self, length=5, width=5):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    def is_valid_coordinate(self, coordinate):
        if self._is_outside(coordinate):
            return False

        return True

    def _is_outside(self, coordinate):
        return (
            coordinate.x < 0
            or coordinate.y < 0
            or coordinate.x >= self.length
            or coordinate.y >= self.width
        )
