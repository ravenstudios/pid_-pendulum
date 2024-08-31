import pygame
import pymunk

class Solid:
    def __init__(self, rect, color, space):
        self.x = rect[0]
        self.y = rect[1]
        self.width = rect[2]
        self.height = rect[3]

        # Create a static body and set its position
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = (self.x + (self.width // 2), self.y + (self.height // 2))

        # Create a shape for the static body
        self.shape = pymunk.Poly.create_box(self.body, (self.width, self.height))
        self.shape.elasticity = 0.8
        self.shape.friction = 0.5  # Optional: Set friction if needed

        # Assign color
        self.color = color

        # Add the body and shape to the space
        space.add(self.body, self.shape)

    def update(self):
        # Static objects don't need to update their position
        pass

    def draw(self, surface):
        # Draw the rectangle shape based on the body's position
        rect_x = int(self.body.position.x - self.width / 2)
        rect_y = int(self.body.position.y - self.height / 2)
        pygame.draw.rect(surface, self.color, (rect_x, rect_y, self.width, self.height))
