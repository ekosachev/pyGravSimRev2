from math import sqrt


class Vector2D(object):
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def len(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, other):
        temp = Vector2D(self.x + other.x, self.y + other.y)
        return temp

    def __sub__(self, other):
        temp = Vector2D(self.x - other.x, self.y - other.y)
        return temp

    def __abs__(self):
        return Vector2D(self.x / self.len(), self.y / self.len())

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __mul__(self, coefficient: float):
        temp = Vector2D(self.x * coefficient, self.y * coefficient)
        return temp
