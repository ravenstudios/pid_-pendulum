from constants import *
import pymunk
import pymunk.pygame_util
import pygame

import ball
import solid
import wall
import drone_balance

import ui
import PID_controller

surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()
clock = pygame.time.Clock()


space = pymunk.Space()
space.gravity = (0, 1981)  # Example for Earth-like gravity, adjust as needed

static_body = space.static_body

options = pymunk.pygame_util.DrawOptions(surface)


drone_balance = drone_balance.Drone_balance(600, 600, RED, space)
left_wall = wall.Wall((0, 0, 20, GAME_HEIGHT), WHITE, space)
right_wall = wall.Wall((GAME_WIDTH - 20, 0, 20, GAME_HEIGHT), WHITE, space)
top_wall = wall.Wall((0, 0, GAME_WIDTH, 20), WHITE, space)
bottom_wall = wall.Wall((0, GAME_HEIGHT - 20, GAME_WIDTH, GAME_HEIGHT), WHITE, space)


blance_pid_slider_values = [[-5, 5, 0.5, 0], [0, 10, 0.1, 0], [0, 5, 0.1, 0], [0, 3, 0.1, 0]]
althold_pid_slider_values = [[0, GAME_HEIGHT, 1, GAME_HEIGHT // 2], [0, 10, 0.1, 0], [0, 5, 0.1, 0], [0, 3, 0.1, 0]]

balance_pid_ui = ui.UI(surface, 50, 50, "Balance Pid", blance_pid_slider_values)
althold_pid_ui = ui.UI(surface, 600, 50, "Althold Pid", althold_pid_slider_values)

# sp, p, i, d = balance_pid_ui.get_values()


balance_pid = PID_controller.PID_Controller(balance_pid_ui.get_values(), -10000, 10000)
althold_pid = PID_controller.PID_Controller(althold_pid_ui.get_values(), -10000, 10000)

def main():
    running = True
    global drone_balance
    while running:

        clock.tick(TICK_RATE)
        space.step(1 / TICK_RATE)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if event.key == pygame.K_r:
                    drone_balance.reset()
                if event.key == pygame.K_q:
                    running = False

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     drone_balance.body.apply_impulse_at_local_point((10, 0), (0, -255))


        draw()
        update(events)
        pygame.display.update()

    pygame.quit()




def draw():
    surface.fill((75, 75, 75))#background

    # drone_balance.draw(surface)
    space.debug_draw(options)
    # pygame.display.update()



def update(events):
    drone_balance.update()
    althold_pid_ui.update(events)
    balance_pid_ui.update(events)


    # if ui.toggle_pid.getValue():
    if True:

        # sp, p, i, d = balance_pid_ui.get_values()
        values = balance_pid_ui.get_values()
        balance_pid.update_pid(values)
        drone_balance.set_setpoint_angle(values[0])


        values = balance_pid.calc(drone_balance.get_current_angle(), clock.tick(60) / 1000.0)
        balance_pid_ui.update_pid_values(values)
        drone_balance.move(values["output"])




if __name__ == "__main__":
    main()
