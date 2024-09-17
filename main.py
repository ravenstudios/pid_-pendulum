from constants import *
import pymunk
import pymunk.pygame_util
import pygame

import walls
import drone_balance
import ui
import PID_controller



pygame.init()


screen_info = pygame.display.Info()
screen_width = int(screen_info.current_w)
screen_height = int(screen_info.current_h)


surface = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
GAME_WIDTH = surface.get_width()
GAME_HEIGHT = surface.get_height()

clock = pygame.time.Clock()


space = pymunk.Space()
space.gravity = (0, 10000)  # Example for Earth-like gravity, adjust as needed

static_body = space.static_body

options = pymunk.pygame_util.DrawOptions(surface)


drone_balance = drone_balance.Drone_balance(GAME_WIDTH // 2, GAME_HEIGHT // 2, surface, space)
walls = walls.Walls(surface, space)
# Min, Max, step, Init
blance_pid_slider_values = [
    [-10, 10, 0.5, 0],#Setpoint
    [0, 10, 0.1, 11],#P
    [0, 5, 0.1, 0],#I
    [0, 3, 0.1, 1]#D
    ]

althold_pid_slider_values = [
    [0, GAME_HEIGHT, 1, GAME_HEIGHT // 2],#Setpoint
    [0, 50, 0.01, 5],#P
    [0, 20, 0.01, 0.25],#I
    [0, 10, 0.01, 0.25]#D
    ]

balance_pid_ui = ui.UI(surface, 0, "Balance Pid", blance_pid_slider_values)
althold_pid_ui = ui.UI(surface, 1, "Althold Pid", althold_pid_slider_values)

# sp, p, i, d = balance_pid_ui.get_values()
balance_pid = PID_controller.PID_Controller(balance_pid_ui.get_values(), -10000, 10000)
althold_pid = PID_controller.PID_Controller(althold_pid_ui.get_values(), -10000, 10000)


objects = [drone_balance, walls, balance_pid_ui, althold_pid_ui]


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


            if event.type == pygame.VIDEORESIZE:
                screen_width, screen_height = event.w, event.h
                screen_height = (screen_width / 16) * 9
                surface = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

                for obj in objects:
                    obj.screen_resize(surface, space)
                althold_pid_ui.slider_values[0] = [0, screen_width, 1, screen_height // 2]
                althold_pid_ui.update(events)
                balance_pid_ui.update(events)



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
    pygame.display.set_caption(f"Drone Y:{GAME_HEIGHT - drone_balance.body.position.y:0.2f}")
    drone_balance.update()
    althold_pid_ui.update(events)
    balance_pid_ui.update(events)

    delta_time = clock.tick(TICK_RATE) / 1000.0


    # Update pid settings from the UI
    balance_pid.update_pid(balance_pid_ui.get_values())
    # Calculate pid output
    balance_pid_output = balance_pid.calc(drone_balance.get_current_angle(), delta_time)
    # Update UI pid output
    balance_pid_ui.update_pid_values(balance_pid_output)

    if balance_pid_ui.toggle_pid.getValue():
        # Balance Drone
        drone_balance.balance(balance_pid_output["output"])



    # Update pid settings from the UI
    althold_pid.update_pid(althold_pid_ui.get_values())
    # Calculate pid output
    althold_pid_output = althold_pid.calc(GAME_HEIGHT - drone_balance.body.position.y, delta_time)
    # Update UI pid output
    althold_pid_ui.update_pid_values(althold_pid_output)

    if althold_pid_ui.toggle_pid.getValue():
        # Balance Drone
        drone_balance.altHold_move(althold_pid_output["output"])




if __name__ == "__main__":
    main()
