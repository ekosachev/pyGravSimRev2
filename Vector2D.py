from math import sqrt


class Vector2D(object):
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def len(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __abs__(self):
        return Vector2D(self.x / self.len(), self.y / self.len())

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __mul__(self, coefficient: float):
        return Vector2D(self.x * coefficient, self.y * coefficient)

    def __truediv__(self, denominator: int):
        if denominator == 0:
            raise ZeroDivisionError
        return Vector2D(self.x / denominator, self.y / denominator)

    def stretch(self, newlength: float):
        if self.len() == 0:
            return Vector2D(0, 0)
        factor = newlength / self.len()
        return Vector2D(self.x * factor, self.y * factor)

