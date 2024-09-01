from constants import *
import pymunk
import pymunk.pygame_util
import pygame

import ball
import solid
import wall
import pendulum

import ui
import PID_controller

surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()
clock = pygame.time.Clock()


space = pymunk.Space()
space.gravity = (0, 981)  # Example for Earth-like gravity, adjust as needed

static_body = space.static_body

options = pymunk.pygame_util.DrawOptions(surface)


pendulum = pendulum.Pendulum(600, 600, RED, space)
left_wall = wall.Wall((0, 0, 20, GAME_HEIGHT), WHITE, space)
right_wall = wall.Wall((GAME_WIDTH - 20, 0, 20, GAME_HEIGHT), WHITE, space)


ui = ui.UI(surface)

sp, p, i, d = ui.get_values()


pid = PID_controller.PID_Controller(sp, p, i, d, -10000, 10000)


def main():
    running = True
    global pendulum
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
                    pendulum.reset()
                if event.key == pygame.K_q:
                    running = False

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     pendulum.body.apply_impulse_at_local_point((10, 0), (0, -255))


        draw()
        update(events)
        pygame.display.update()

    pygame.quit()




def draw():
    surface.fill((75, 75, 75))#background

    # pendulum.draw(surface)
    space.debug_draw(options)
    # pygame.display.update()



def update(events):
    pendulum.update()
    ui.update(events)

    if ui.toggle_pid.getValue():
        sp, p, i, d = ui.get_values()
        pid.update_pid(sp, p, i, d)
        pendulum.set_setpoint_angle(sp)
        values = pid.calc(pendulum.get_current_angle(), clock.tick(60) / 1000.0)
        ui.update_pid_values(values)
        pendulum.move(values["output"])




if __name__ == "__main__":
    main()
