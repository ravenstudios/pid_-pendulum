import pygame
import pymunk
# from constants import *
import math
import random


class Drone_balance:
    def __init__(self, x, y, surface, space):
        self.x = x
        self.y = y
        self.initial_angle = 0

        self.GAME_WIDTH = surface.get_width()
        self.GAME_HEIGHT = surface.get_height()
        self.max_vel = self.GAME_WIDTH * 0.186
        self.radius = self.GAME_WIDTH * self.GAME_HEIGHT * 0.00002
        self.arm_length = self.GAME_WIDTH * 0.232
        self.arm_radius = self.GAME_HEIGHT * 0.01

        self.body = pymunk.Body()
        self.body.position = (self.x, self.y)
        self.body_vis = pymunk.Circle(self.body, self.radius // 2, (0, 0))
        # Define the left_arm and bob of the pendulum
        self.left_arm = pymunk.Segment(self.body, (0, 0), (-self.arm_length, 0), self.arm_radius)
        self.left_motor = pymunk.Circle(self.body, self.radius, (-self.arm_length, 0))
        self.left_arm.mass = self.GAME_WIDTH * 0.01
        self.left_motor.mass = self.GAME_WIDTH * 0.1
        self.left_motor.elasticity = self.GAME_WIDTH * 0.0003
        self.left_motor.friction = 0.5


        self.right_arm = pymunk.Segment(self.body, (0, 0), (self.arm_length, 0), self.arm_radius)
        self.right_motor = pymunk.Circle(self.body, self.radius, (self.arm_length, 0))
        self.right_arm.mass = self.GAME_WIDTH * 0.01
        self.right_motor.mass = self.GAME_WIDTH * 0.1
        self.right_motor.elasticity = self.GAME_WIDTH * 0.0003
        self.right_motor.friction = 0.5

        space.add(self.body, self.left_arm, self.left_motor, self.right_arm, self.right_motor, self.body_vis)

        # Control parameters
        self.force_magnitude = self.GAME_WIDTH * 9.3
        self.setpoint_angle = 0



    def get_current_angle(self):
        angle_degrees = math.degrees(self.body.angle)
        return ((angle_degrees + 180) % 360) - 180


    def balance(self, move):
        if self.body.position.y > self.GAME_HEIGHT // 3:
            if move > 0:
                self.body.apply_force_at_local_point((0, -abs(move) * self.force_magnitude), (-self.arm_length, 0))
            else:
                self.body.apply_force_at_local_point((0, -abs(move) * self.force_magnitude), (self.arm_length, 0))



    def altHold_move(self, move):
        # Clamp to a negitive number, if positive, drone gets stuck and wont fall back down
        move = min(max(0, move), self.max_vel)
        self.body.apply_force_at_local_point((0, -abs(move) * self.force_magnitude), (self.arm_length, 0))
        self.body.apply_force_at_local_point((0, -abs(move) * self.force_magnitude), (-self.arm_length, 0))




    def update(self):
        x = max(0, min(self.body.position.x, self.GAME_WIDTH))
        y = max(0, min(self.body.position.y, self.GAME_HEIGHT))

        self.body.position = (x, y)
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.body.apply_force_at_local_point((0, -self.force_magnitude * 300), (-self.arm_length, 0))
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.body.apply_force_at_local_point((0, -self.force_magnitude * 300), (self.arm_length, 0))


    def reset(self):
        self.body.velocity = (0, 0)
        self.body.angular_velocity = 0
        self.body.angle = self.initial_angle
        self.body.position = (int(self.GAME_WIDTH // 2), int(self.GAME_HEIGHT // 2))



    def screen_resize(self, surface, space):
        self.GAME_WIDTH = int(surface.get_width())
        self.GAME_HEIGHT = int(surface.get_height())

        # Recalculate dimensions
        self.radius = self.GAME_WIDTH * self.GAME_HEIGHT * 0.00002
        self.arm_length = self.GAME_WIDTH * 0.232
        self.arm_radius = self.GAME_HEIGHT * 0.005

        self.left_motor.unsafe_set_radius(self.radius)
        self.right_motor.unsafe_set_radius(self.radius)

        self.left_motor.unsafe_set_offset((-self.arm_length, 0))
        self.right_motor.unsafe_set_offset((self.arm_length, 0))


        self.body_vis.unsafe_set_radius(self.radius // 2)

        self.left_arm.unsafe_set_endpoints((0, 0), (-self.arm_length, 0))
        self.right_arm.unsafe_set_endpoints((0, 0), (self.arm_length, 0))

        self.left_arm.unsafe_set_radius(self.arm_radius)
        self.right_arm.unsafe_set_radius(self.arm_radius)\

        self.reset()
