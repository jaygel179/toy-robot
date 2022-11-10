class Coordinate:
    _x = 0
    _y = 0

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def value(self):
        return (
            self._x,
            self._y,
        )

    def __eq__(self, other):
        return self.x == other.x and self.y == self.y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
