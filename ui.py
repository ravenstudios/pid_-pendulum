import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.toggle import Toggle
import pygame

class UI():


    def __init__(self, surface, pos, title, slider_values):

        self.GAME_WIDTH = surface.get_width() #1680
        self.GAME_HEIGHT = surface.get_height()#1050
        self.pos = pos

        if self.pos == 1:
            self.x = int(self.GAME_WIDTH * 0.35)
        else:
            self.x = int(self.GAME_WIDTH * 0.03)
        self.y = int(self.GAME_HEIGHT * 0.03)

        self.title_text = title

        self.slider_values = slider_values

        self.width = int(self.GAME_WIDTH * 0.06)
        self.height = int(self.GAME_HEIGHT * 0.02)
        self.y_gap = int(self.GAME_HEIGHT * 0.04)
        self.x_gap = int(self.GAME_WIDTH * 0.08)
        self.font_size = int(self.GAME_HEIGHT * 0.02)
        self.txt_length = int(self.GAME_WIDTH * 0.12)
        self.txt_height = int(self.GAME_HEIGHT * 0.04)
        self.slider_y_gap = int(self.GAME_HEIGHT * 0.01)

        self.set_point_slider = Slider(surface, self.x, (self.y + self.slider_y_gap), self.width, self.height, min=self.slider_values[0][0], max=self.slider_values[0][1], step=self.slider_values[0][2], initial=self.slider_values[0][3])
        self.p_slider = Slider(surface, self.x, (self.y + self.slider_y_gap) + (self.y_gap * 1), self.width, self.height, min=self.slider_values[1][0], max=self.slider_values[1][1], step=self.slider_values[1][2], initial=self.slider_values[1][3])
        self.i_slider = Slider(surface, self.x, (self.y + self.slider_y_gap) + (self.y_gap * 2), self.width, self.height, min=self.slider_values[2][0], max=self.slider_values[2][1], step=self.slider_values[2][2], initial=self.slider_values[2][3])
        self.d_slider = Slider(surface, self.x, (self.y + self.slider_y_gap) + (self.y_gap * 3), self.width, self.height, min=self.slider_values[3][0], max=self.slider_values[3][1], step=self.slider_values[3][2], initial=self.slider_values[3][3])


        self.set_point_gain = TextBox(surface, self.x + self.x_gap, self.y + (self.y_gap * 0), self.txt_length, self.txt_height, fontSize=self.font_size)
        self.p_gain = TextBox(surface, self.x + self.x_gap, self.y + (self.y_gap * 1), self.txt_length, self.txt_height, fontSize=self.font_size)
        self.i_gain = TextBox(surface, self.x + self.x_gap, self.y + (self.y_gap * 2), self.txt_length, self.txt_height, fontSize=self.font_size)
        self.d_gain = TextBox(surface, self.x + self.x_gap, self.y + (self.y_gap * 3), self.txt_length, self.txt_height, fontSize=self.font_size)

        self.toggle_pid_output = TextBox(surface, self.x + self.x_gap, self.y + (self.y_gap * 4), self.txt_length, self.height * 2, fontSize=self.font_size)
        self.toggle_pid_output.setText("Toggle PID")
        self.toggle_pid = Toggle(surface, self.x, (self.y + self.slider_y_gap) + (self.y_gap * 4), self.height, self.height)

        self.error = TextBox(surface, self.x + (self.x_gap * 2), self.y + (self.y_gap * 0), self.txt_length, self.txt_height, fontSize=self.font_size)
        self.p_output = TextBox(surface, self.x + (self.x_gap * 2), self.y + (self.y_gap * 1), self.txt_length, self.txt_height, fontSize=self.font_size)
        self.i_output = TextBox(surface, self.x + (self.x_gap * 2), self.y + (self.y_gap * 2), self.txt_length, self.txt_height, fontSize=self.font_size)
        self.d_output = TextBox(surface, self.x + (self.x_gap * 2), self.y + (self.y_gap * 3), self.txt_length, self.txt_height, fontSize=self.font_size)
        self.out_output = TextBox(surface, self.x + (self.x_gap * 2), self.y + (self.y_gap * 4), self.txt_length, self.txt_height, fontSize=self.font_size)


        self.title = TextBox(surface, self.x + self.x_gap, self.y + (self.y_gap * 5), self.txt_length, self.txt_height, fontSize=self.font_size)


        self.p_output.setText(f"P Output: {0}")
        self.i_output.setText(f"I Output: {0}")
        self.d_output.setText(f"D Output: {0}")
        self.out_output.setText(f" Output: {0}")
        self.error.setText(f" Error: {0}")
        self.title.setText(self.title_text)



    def make_ui(self, surface):
        self.width = int(self.GAME_WIDTH * 0.06)
        self.height = int(self.GAME_HEIGHT * 0.02)
        self.y_gap = int(self.GAME_HEIGHT * 0.04)
        self.x_gap = int(self.GAME_WIDTH * 0.08)
        self.font_size = int(self.GAME_HEIGHT * 0.02)
        self.txt_length = int(self.GAME_WIDTH * 0.12)
        self.txt_height = int(self.GAME_HEIGHT * 0.04)
        self.slider_y_gap = int(self.GAME_HEIGHT * 0.01)

        self.set_point_slider = Slider(surface, self.x, (self.y + self.slider_y_gap), self.width, self.height, min=self.slider_values[0][0], max=self.slider_values[0][1], step=self.slider_values[0][2], initial=self.slider_values[0][3])
        self.p_slider = Slider(surface, self.x, (self.y + self.slider_y_gap) + (self.y_gap * 1), self.width, self.height, min=self.slider_values[1][0], max=self.slider_values[1][1], step=self.slider_values[1][2], initial=self.slider_values[1][3])
        self.i_slider = Slider(surface, self.x, (self.y + self.slider_y_gap) + (self.y_gap * 2), self.width, self.height, min=self.slider_values[2][0], max=self.slider_values[2][1], step=self.slider_values[2][2], initial=self.slider_values[2][3])
        self.d_slider = Slider(surface, self.x, (self.y + self.slider_y_gap) + (self.y_gap * 3), self.width, self.height, min=self.slider_values[3][0], max=self.slider_values[3][1], step=self.slider_values[3][2], initial=self.slider_values[3][3])


        self.set_point_gain = TextBox(surface, self.x + self.x_gap, self.y + (self.y_gap * 0), self.txt_length, self.txt_height, fontSize=self.font_size)
        self.p_gain = TextBox(surface, self.x + self.x_gap, self.y + (self.y_gap * 1), self.txt_length, self.txt_height, fontSize=self.font_size)
        self.i_gain = TextBox(surface, self.x + self.x_gap, self.y + (self.y_gap * 2), self.txt_length, self.txt_height, fontSize=self.font_size)
        self.d_gain = TextBox(surface, self.x + self.x_gap, self.y + (self.y_gap * 3), self.txt_length, self.txt_height, fontSize=self.font_size)

        self.toggle_pid_output = TextBox(surface, self.x + self.x_gap, self.y + (self.y_gap * 4), self.txt_length, self.height * 2, fontSize=self.font_size)
        self.toggle_pid_output.setText("Toggle PID")
        self.toggle_pid = Toggle(surface, self.x, (self.y + self.slider_y_gap) + (self.y_gap * 4), self.height, self.height)

        self.error = TextBox(surface, self.x + (self.x_gap * 2), self.y + (self.y_gap * 0), self.txt_length, self.txt_height, fontSize=self.font_size)
        self.p_output = TextBox(surface, self.x + (self.x_gap * 2), self.y + (self.y_gap * 1), self.txt_length, self.txt_height, fontSize=self.font_size)
        self.i_output = TextBox(surface, self.x + (self.x_gap * 2), self.y + (self.y_gap * 2), self.txt_length, self.txt_height, fontSize=self.font_size)
        self.d_output = TextBox(surface, self.x + (self.x_gap * 2), self.y + (self.y_gap * 3), self.txt_length, self.txt_height, fontSize=self.font_size)
        self.out_output = TextBox(surface, self.x + (self.x_gap * 2), self.y + (self.y_gap * 4), self.txt_length, self.txt_height, fontSize=self.font_size)


        self.title = TextBox(surface, self.x + self.x_gap, self.y + (self.y_gap * 5), self.txt_length, self.txt_height, fontSize=self.font_size)


        self.p_output.setText(f"P Output: {0}")
        self.i_output.setText(f"I Output: {0}")
        self.d_output.setText(f"D Output: {0}")
        self.out_output.setText(f" Output: {0}")
        self.error.setText(f" Error: {0}")
        self.title.setText(self.title_text)

    def update(self, events):
        self.set_point_gain.setText(f"SP:{self.set_point_slider.getValue():0.2f}")
        self.p_gain.setText(f"P:{self.p_slider.getValue():0.2f}")
        self.i_gain.setText(f"I:{self.i_slider.getValue():0.2f}")
        self.d_gain.setText(f"D:{self.d_slider.getValue():0.2f}")
        pygame_widgets.update(events)

    def get_values(self):
        return[
            self.set_point_slider.getValue(),
            self.p_slider.getValue(),
            self.i_slider.getValue(),
            self.d_slider.getValue()
        ]

    def update_pid_values(self, values):
        self.p_output.setText(f"P Output: {values['P']:0.2f}")
        self.i_output.setText(f"I Output: {values['I']:0.2f}")
        self.d_output.setText(f"D Output: {values['D']:0.2f}")
        self.out_output.setText(f" Output: {values['output']:0.2f}")
        self.error.setText(f" Error: {values['error']:0.2f}")



    def screen_resize(self, surface, space):
        self.GAME_WIDTH = surface.get_width()
        self.GAME_HEIGHT = surface.get_height()
        if self.pos == 1:
            self.x = int(self.GAME_WIDTH * 0.35)
        else:
            self.x = int(self.GAME_WIDTH * 0.03)
        self.y = int(self.GAME_HEIGHT * 0.03)
        
        self.make_ui(surface)
        # self.update(events)# self.set_point_slider.x = 0
