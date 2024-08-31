import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame_widgets.toggle import Toggle
import pygame

class UI():


    def __init__(self, surface):


        self.set_point_slider = Slider(surface, 100, 50, 200, 20, min=0, max=359, step=1, initial=90)
        self.p_slider = Slider(surface, 100, 100, 200, 20, min=0, max=10, step=0.1, initial=0.1)
        self.i_slider = Slider(surface, 100, 150, 200, 20, min=0, max=5, step=0.01, initial=0)
        self.d_slider = Slider(surface, 100, 200, 200, 20, min=0, max=1, step=0.01, initial=0)


        self.set_point_gain = TextBox(surface, 350, 35, 250, 50, fontSize=30)
        self.p_gain = TextBox(surface, 350, 85, 250, 50, fontSize=30)
        self.i_gain = TextBox(surface, 350, 135, 250, 50, fontSize=30)
        self.d_gain = TextBox(surface, 350, 185, 250, 50, fontSize=30)

        self.toggle_pid_output = TextBox(surface, 1000, 50, 120, 40, fontSize=20)
        self.toggle_pid_output.setText("Toggle PID")
        self.toggle_pid = Toggle(surface, 950, 60, 25, 25)

        self.error = TextBox(surface, 650, 35, 250, 50, fontSize=30)
        self.p_output = TextBox(surface, 650, 85, 250, 50, fontSize=30)
        self.i_output = TextBox(surface, 650, 135, 250, 50, fontSize=30)
        self.d_output = TextBox(surface, 650, 185, 250, 50, fontSize=30)
        self.out_output = TextBox(surface, 650, 235, 250, 50, fontSize=30)

        self.p_output.setText(f"P Output: {0}")
        self.i_output.setText(f"I Output: {0}")
        self.d_output.setText(f"D Output: {0}")
        self.out_output.setText(f" Output: {0}")
        self.error.setText(f" Error: {0}")


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
        self.p_output.setText(f"P Output: {values["P"]:0.2f}")
        self.i_output.setText(f"I Output: {values["I"]:0.2f}")
        self.d_output.setText(f"D Output: {values["D"]:0.2f}")
        self.out_output.setText(f" Output: {values["output"]:0.2f}")
        self.error.setText(f" Error: {values["error"]:0.2f}")
