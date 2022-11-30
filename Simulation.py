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
        self.simLog = [[x.position for x in self.particles]]

    def run_step(self, draw_velocity_vectors: bool, draw_barycenter: bool, draw_trails: bool) -> ImageQt:
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
        self.simLog.append(self.calculatedPositions)
        self.calculatedPositions = []

        # Draw new frame
        self.frameDraw.rectangle(((0, 0), self.framesize),
                                 tuple(self.config["DRAWING"]["background_color"]))  # Clear the frame

        if draw_trails:
            for i in range(len(self.simLog)):
                if i == 0:
                    continue
                for j in range(len(self.simLog[i])):
                    self.frameDraw.line(xy=((self.simLog[i][j].x + self.framesize[0] // 2,
                                             self.simLog[i][j].y + self.framesize[0] // 2),
                                            (self.simLog[i - 1][j].x + self.framesize[0] // 2,
                                             self.simLog[i - 1][j].y + self.framesize[0] // 2)),
                                        fill=tuple(self.config["DRAWING"]["trail_color"]))

        for particle in self.particles:
            pos: Vector2D = Vector2D(self.framesize[0] // 2, self.framesize[1] // 2) + particle.position
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
                                        (pos.x + particle.velocity.x * (-self.config["DRAWING"]["vel_vect_multiplier"]),
                                         pos.y + particle.velocity.y * (
                                             -self.config["DRAWING"]["vel_vect_multiplier"]))),
                                    fill=tuple(self.config["DRAWING"]["velocity_vectors_color"]))

            if draw_barycenter:
                barycenter_position: Vector2D = sum([particle.position * particle.mass for particle in self.particles],
                                                    Vector2D(0, 0)) / sum(
                    [particle.mass for particle in self.particles])
                barycenter_position = Vector2D(self.framesize[0] // 2, self.framesize[1] // 2) + barycenter_position
                self.frameDraw.ellipse(xy=(barycenter_position.x - 5,
                                           barycenter_position.y - 5,
                                           barycenter_position.x + 5,
                                           barycenter_position.y + 5),
                                       fill=tuple(self.config["DRAWING"]["barycenter_color"]))

        return ImageQt(self.frameImage)

    def draw_force_heatmap(self) -> ImageQt:
        # Calculate the force applied to every pixel of the frame
        min_force = 1000000
        max_force = -1
        field = [0] * self.framesize[0] * self.framesize[1]
        for i in range(self.framesize[0]):
            for j in range(self.framesize[1]):
                forces = []
                for body in self.particles:
                    distance = body.position - Vector2D(i, j) + Vector2D(self.framesize[0] // 2, self.framesize[1] // 2)
                    try:
                        forces.append(
                            distance.stretch(body.mass / pow(max(distance.len(), body.radius), 2))
                        )
                    except ZeroDivisionError:
                        pass
                force = sum(forces, Vector2D(0, 0)).len()
                field[i * self.framesize[1] + j] = force
                min_force = min(min_force, force)
                max_force = max(max_force, force)
        print(max_force, min_force)

        # Map all the values to a range from 0 to 1
        field = list(map(lambda x: translate(x, min_force, max_force) ** 0.2, field))

        # Color the pixels:
        for i in range(self.framesize[0] * self.framesize[1]):

            c1 = self.config["DRAWING"]["heatmap_gradient_color_0"]
            c2 = self.config["DRAWING"]["heatmap_gradient_color_1"]
            color = [0, 0, 0]
            for component in range(3):
                color[component] = int(
                    c1[component] + (field[i] * (c2[component] - c1[component]))
                )
            self.frameImage.putpixel(xy=(i // self.framesize[0],
                                         i % self.framesize[1]), value=tuple(color))

        return ImageQt(self.frameImage)


def translate(value, Min, Max):
    # Figure out how 'wide' each range is
    span = Max - Min

    # Convert the left range into a 0-1 range (float)
    value_scaled = float(value - Min) / float(span)

    return value_scaled
