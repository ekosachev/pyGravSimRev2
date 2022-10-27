from typing import List
from Particle import Particle
from Vector2D import Vector2D
from json import load
from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt


class Simulation(object):
    def __init__(self, particles: List[Particle], framesize: tuple[int, int]) -> None:
        with open('config.json') as config:
            self.config = load(config)

        self.frameCounter = 0
        self.particles = particles
        self.framesize = framesize
        self.frameImage = Image.new("RGB", framesize, tuple(self.config["DRAWING"]["background_color"]))
        self.frameDraw = ImageDraw.Draw(self.frameImage)

    def run_step(self, draw_velocity_vectors: bool) -> ImageQt:
        # Calculate accelerations for all particles
        for attracted in self.particles:
            attracted.acceleration = Vector2D(0, 0)
            for attractor in self.particles:
                distance: Vector2D = attractor.position - attracted.position
                try:
                    attracted.acceleration += abs(distance) * (attractor.mass / distance.len() ** 2)
                except ZeroDivisionError:
                    continue
            attracted.velocity += attracted.acceleration
            attracted.position += attracted.velocity

        # Draw new frame
        self.frameDraw.rectangle(((0, 0), self.framesize),
                                 tuple(self.config["DRAWING"]["background_color"]))  # Clear the frame

        for particle in self.particles:
            pos: Vector2D = particle.position + Vector2D(self.framesize[0] // 2, self.framesize[1] // 2)
            self.frameDraw.ellipse(xy=((pos.x - particle.radius,
                                        pos.y - particle.radius),
                                       (pos.x + particle.radius,
                                        pos.y + particle.radius)),
                                   fill=tuple(self.config["DRAWING"]["particle_color"]))

            self.frameDraw.text((pos.x,
                                 pos.y),
                                str(particle.id),
                                fill=tuple(self.config["DRAWING"]["particle_label_color"]))

            if draw_velocity_vectors:
                self.frameDraw.line(xy=((pos.x, pos.y),
                                        (pos.x + particle.velocity.x, pos.y + particle.velocity.y)),
                                    fill=tuple(self.config["DRAWING"]["velocity_vectors_color"]))
        self.frameImage.save("frame.jpg")
        return ImageQt(self.frameImage)
