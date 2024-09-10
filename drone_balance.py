import pygame
import pymunk
from constants import *
import math
import random


class Drone_balance:
    def __init__(self, x, y, color, space):
        self.x = x
        self.y = y
        self.initial_x = self.x
        self.initial_y = self.y
        self.initial_angle = 0
        self.color = color
        self.radius = 40
        self.left_arm_length = -255
        self.right_arm_length = 255

        # Create the pivot (rotation center)
        self.rotation_center_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.rotation_center_body.position = (self.x, self.y)

        # Create the pendulum body
        self.body = pymunk.Body()
        self.body.position = self.rotation_center_body.position

        # Define the left_arm and bob of the pendulum
        self.left_arm = pymunk.Segment(self.body, (0, 0), (self.left_arm_length, 0), 5)
        self.left_motor = pymunk.Circle(self.body, self.radius, (self.left_arm_length, 0))

        # Set physics properties
        # self.left_arm.friction = 100
        # self.left_motor.friction = 100
        self.left_arm.mass = 1
        self.left_motor.mass = 10000
        self.left_motor.elasticity = 0.90


        self.right_arm = pymunk.Segment(self.body, (0, 0), (self.right_arm_length, 0), 5)
        self.right_motor = pymunk.Circle(self.body, self.radius, (self.right_arm_length, 0))

        # Set physics properties
        # self.right_arm.friction = 100
        # self.right_motor.friction = 100
        self.right_arm.mass = 10
        self.right_motor.mass = 10000
        self.right_motor.elasticity = 0.90



        # Attach the pendulum to the pivot using a pin joint
        self.rotation_center_joint = pymunk.PivotJoint(self.body, self.rotation_center_body, (0, 0), (0, 0))
        space.add(self.body, self.left_arm, self.left_motor, self.right_arm, self.right_motor, self.rotation_center_body)

        # Control parameters
        self.force_magnitude = 100000000.0  # Force magnitude to apply
        self.setpoint_angle = 0


    def set_setpoint_angle(self, sp):
        self.setpoint_angle = sp


    def get_current_angle(self):
        angle_degrees = math.degrees(self.body.angle)
        return ((angle_degrees + 180) % 360) - 180


    def move(self, move):
        print(move)
        if self.body.position.y > GAME_HEIGHT // 3:
            if move > 0:
                self.body.apply_force_at_local_point((0, -abs(move) * self.force_magnitude // 10), (self.left_arm_length, 0))
            else:
                self.body.apply_force_at_local_point((0, -abs(move) * self.force_magnitude // 10), (self.right_arm_length, 0))



    def update(self):
        # Example control: Move left or right


        if pygame.key.get_pressed()[pygame.K_LEFT]:
            # self.rotation_center_body.position -= (self.force_magnitude, 0)
            self.body.apply_force_at_local_point((0, -self.force_magnitude), (self.left_arm_length, 0))
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            # self.rotation_center_body.position += (self.force_magnitude, 0)
            self.body.apply_force_at_local_point((0, -self.force_magnitude), (self.right_arm_length, 0))

        if self.body.position.y > GAME_HEIGHT  * 0.7:
            self.body.apply_force_at_local_point((0, -self.force_magnitude * 0.3), (self.left_arm_length, 0))
            self.body.apply_force_at_local_point((0, -self.force_magnitude * 0.3), (self.right_arm_length, 0))



    def reset(self):
        # Reset the position and angle
        # self.body.position = (self.initial_x, self.initial_y)
        self.body.velocity = (0, 0)
        self.body.angular_velocity = 0
        self.body.angle = self.initial_angle

        # Reset the pivot position
        self.rotation_center_body.position = (self.initial_x, self.initial_y)
        self.body.position = self.rotation_center_body.position



    def draw(self, surface):
        # Offset used when creating the circle
        offset = pymunk.Vec2d(0, self.left_arm_length)

        # Rotate the offset by the body's current angle
        rotated_offset = offset.rotated(self.body.angle)

        # Calculate the bob's position
        bob_position = self.body.position + rotated_offset

        # Draw bob
        self.center = (int(bob_position.x), int(bob_position.y))
        pygame.draw.circle(surface, self.color, self.center, self.radius, width=0)

        # Draw Pivot
        self.center = (int(self.rotation_center_body.position.x), int(self.rotation_center_body.position.y))
        pygame.draw.circle(surface, self.color, self.center, self.radius / 2, width=0)

        # Draw left_arm
        left_arm_start = self.body.position + self.left_arm.a.rotated(self.body.angle)
        left_arm_end = self.body.position + self.left_arm.b.rotated(self.body.angle)

        # Convert to integers for pygame
        left_arm_start_int = (int(left_arm_start.x), int(left_arm_start.y))
        left_arm_end_int = (int(left_arm_end.x), int(left_arm_end.y))

        # Draw the line representing the left_arm
        pygame.draw.line(surface, BLUE, left_arm_start_int, left_arm_end_int, int(self.left_arm.radius))
