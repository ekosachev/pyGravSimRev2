from typing import Iterable

from Particle import Particle
from Vector2D import Vector2D
from json import load, dump

def save_initial_state(particles: Iterable[Particle],
                       filename: str) -> None:
    info = []
    for particle in particles:

        info.append({
            "id": particle.id,
            "position": [
                particle.position.x,
                particle.position.y
            ],
            "velocity": [
                particle.velocity.x,
                particle.velocity.y
            ],
            "mass": particle.mass,
            "radius": particle.radius
        })

    with open(filename, 'w') as f:
        dump(info, f, indent=4)

def load_initial_state(filename: str) -> Iterable[Particle]:
    with open(filename) as f:
        info = load(f)

    result = []

    for particle in info:
        result.append(Particle(id=particle["id"],
                               position=Vector2D(x=particle["position"][0],
                                                 y=particle["position"][1]),
                               velocity=Vector2D(x=particle["velocity"][0],
                                                 y=particle["velocity"][1]),
                               mass=particle["mass"],
                               radius=particle["radius"]))
    return result