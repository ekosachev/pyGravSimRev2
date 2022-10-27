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
        self.calculatedPositions = []

    def run_step(self, draw_velocity_vectors: bool, draw_barycenter: bool) -> ImageQt:
        # Calculate accelerations for all particles
        for attracted in self.particles:
            for attractor in self.particles:
                distance: Vector2D = attractor.position - attracted.position
                try:
                    attracted.velocity += distance.stretch(attractor.mass / pow(distance.len(), 2))
                except ZeroDivisionError:
                    continue
            self.calculatedPositions.append(attracted.position + attracted.velocity)

        for i in range(len(self.particles)):
            self.particles[i].position = self.calculatedPositions[i]
        self.calculatedPositions = []

        # Draw new frame
        self.frameDraw.rectangle(((0, 0), self.framesize),
                                 tuple(self.config["DRAWING"]["background_color"]))  # Clear the frame

        for particle in self.particles:
            pos: Vector2D = Vector2D(self.framesize[0] // 2, self.framesize[1] // 2) - particle.position
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

            if draw_barycenter:
                barycenter_position: Vector2D = sum([particle.position * particle.mass for particle in self.particles],
                                                    Vector2D(0, 0)) / sum([particle.mass for particle in self.particles])
                barycenter_position = Vector2D(self.framesize[0] // 2, self.framesize[1] // 2) - barycenter_position
                self.frameDraw.ellipse((barycenter_position.x - 5,
                                        barycenter_position.y - 5,
                                        barycenter_position.x + 5,
                                        barycenter_position.y + 5),
                                       "red")
        return ImageQt(self.frameImage)
