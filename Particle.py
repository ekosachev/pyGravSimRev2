from Vector2D import Vector2D


class Particle(object):
    def __init__(self,
                 id: int,
                 position: Vector2D,
                 velocity: Vector2D,
                 mass: int,
                 radius: int):

        self.id = id
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.radius = radius

    def __repr__(self) -> str:
        return f"Тело {self.id}; XY0={repr(self.position)}; V0={repr(self.velocity)}; m={self.mass}"
