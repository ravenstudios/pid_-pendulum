import pygame
from constants import *
import random
import pymunk

class Ball:
    def __init__(self, x, y, color, space, static_body):
        self.x = x
        self.y = y
        self.radius = 32

        self.body = pymunk.Body(10, 1, pymunk.Body.DYNAMIC)
        self.body.position = (x, y)

        self.shape = pymunk.Circle(self.body, self.radius)
        self.shape.mass = 5
        self.shape.elasticity = 0.8

        self.center = (int(self.body.position.x), int(self.body.position.y))
        self.color = color
        print(f'self.body:{self.shape}')

        # Friction
        self.pivot = pymunk.PivotJoint(static_body, self.body, (0, 0), (0, 0))
        self.pivot.max_bias = 0
        self.pivot.max_force = 100

        space.add(self.body, self.shape, self.pivot)


    def update(self):
        pass



    def draw(self, surface):
        self.center = (int(self.body.position.x), int(self.body.position.y))
        pygame.draw.circle(surface, self.color, self.center, self.radius, width=0)
