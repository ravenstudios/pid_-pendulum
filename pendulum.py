import pygame
import pymunk
from constants import *
import math



class Pendulum:
    def __init__(self, x, y, color, space):
        self.x = x
        self.y = y
        self.initial_x = self.x
        self.initial_y = self.y
        self.initial_angle = 0
        self.color = color
        self.radius = 40
        self.rod_length = -255

        # Create the pivot (rotation center)
        self.rotation_center_body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
        self.rotation_center_body.position = (self.x, self.y)

        # Create the pendulum body
        self.body = pymunk.Body()
        self.body.position = self.rotation_center_body.position

        # Define the rod and bob of the pendulum
        self.rod = pymunk.Segment(self.body, (0, 0), (0, self.rod_length), 5)
        self.bob = pymunk.Circle(self.body, self.radius, (0, self.rod_length))

        # Set physics properties
        self.rod.friction = 1
        self.bob.friction = 1
        self.rod.mass = 1
        self.bob.mass = 100
        # self.bob.elasticity = 0.95

        # Attach the pendulum to the pivot using a pin joint
        self.rotation_center_joint = pymunk.PivotJoint(self.body, self.rotation_center_body, (0, 0), (0, 0))
        space.add(self.body, self.rod, self.bob, self.rotation_center_joint, self.rotation_center_body)

        # Control parameters
        self.force_magnitude = 100000.0  # Force magnitude to apply
        self.setpoint_angle = 0


    def set_setpoint_angle(self, sp):
        self.setpoint_angle = sp


    def get_current_angle(self):
        angle_degrees = math.degrees(self.body.angle)
        return ((angle_degrees + 180) % 360) - 180


    def move(self, move):
        self.rotation_center_body.position += (-move, 0)
        # self.body.position = self.rotation_center_body.position
        # self.body.apply_force_at_local_point((move, 0), (0, self.rod_length))

    def update(self):
        # Example control: Move left or right
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            # self.rotation_center_body.position -= (self.force_magnitude, 0)
            self.body.apply_force_at_local_point((-self.force_magnitude, 0), (0, self.rod_length))
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            # self.rotation_center_body.position += (self.force_magnitude, 0)
            self.body.apply_force_at_local_point((self.force_magnitude, 0), (0, self.rod_length))
        # Screen constraints
        x = max(0, min(self.rotation_center_body.position.x, GAME_WIDTH))
        y = self.rotation_center_body.position.y
        self.rotation_center_body.position = (x, y)

        # Angle constraints
        # max_angle = 45 * (math.pi / 180)  # 45 degrees in radians
        # self.body.angle = max(-max_angle, min(self.body.angle, max_angle))


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
        offset = pymunk.Vec2d(0, self.rod_length)

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

        # Draw rod
        rod_start = self.body.position + self.rod.a.rotated(self.body.angle)
        rod_end = self.body.position + self.rod.b.rotated(self.body.angle)

        # Convert to integers for pygame
        rod_start_int = (int(rod_start.x), int(rod_start.y))
        rod_end_int = (int(rod_end.x), int(rod_end.y))

        # Draw the line representing the rod
        pygame.draw.line(surface, BLUE, rod_start_int, rod_end_int, int(self.rod.radius))
