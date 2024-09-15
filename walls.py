import pygame
import pymunk


class Walls():


    def __init__(self, surface, space):
        self.GAME_WIDTH = surface.get_width()
        self.GAME_HEIGHT = surface.get_height()
        self.width = self.GAME_WIDTH * self.GAME_HEIGHT * 0.00001



        self.left_wall = Wall((0, 0, self.width, self.GAME_HEIGHT), space)
        self.right_wall = Wall((self.GAME_WIDTH - self.width, 0, self.width, self.GAME_HEIGHT), space)
        self.top_wall = Wall((0, 0, self.GAME_WIDTH, self.width), space)
        self.bottom_wall = Wall((0, self.GAME_HEIGHT - self.width, self.GAME_WIDTH, self.GAME_HEIGHT), space)




    def screen_resize(self, surface, space):
        self.GAME_WIDTH = surface.get_width()
        self.GAME_HEIGHT = surface.get_height()
        self.width = self.GAME_WIDTH * self.GAME_HEIGHT * 0.00001
        print(self.GAME_HEIGHT)
        self.left_wall.screen_resize((self.width // 2, self.GAME_HEIGHT // 2), (self.width, self.GAME_HEIGHT), space)
        self.right_wall.screen_resize((self.GAME_WIDTH - self.width // 2, self.GAME_HEIGHT // 2), (self.width, self.GAME_HEIGHT), space)
        self.top_wall.screen_resize((self.GAME_WIDTH // 2, self.width // 2), (self.GAME_WIDTH, self.width), space)
        self.bottom_wall.screen_resize((self.GAME_WIDTH // 2, self.GAME_HEIGHT - self.width // 2), (self.GAME_WIDTH, self.width), space)



class Wall:
    def __init__(self, rect, space):
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



        # Add the body and shape to the space
        space.add(self.body, self.shape)



    def update(self):
        # Static objects don't need to update their position
        pass



    def screen_resize(self, pos, size, space):
        space.remove(self.shape)
        self.shape = pymunk.Poly.create_box(self.body, size)
        self.body.position = pos
        space.add(self.shape)
