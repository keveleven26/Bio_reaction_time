import time, random
import pygame
from pygame.locals import (KEYDOWN, K_DOWN)

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
saturated = (0,0,255)
black = (0,0,0)
Start = False

frame_num = 0

running = True
program_start_time = time.time()
display_time = random.randint(3, 5)
init_time = -1
end_time = -1

flipped = False
while running: 
    if time.time() >= program_start_time+display_time and not flipped:
        pygame.event.get()
        screen.fill(saturated)
        pygame.display.flip()
        init_time = time.perf_counter_ns()
        flipped = True
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and flipped: 
                print("received key down")
                end_time = time.perf_counter_ns()
                screen.fill(black)
                pygame.display.flip()

    if init_time != -1 and end_time != -1:
        print(str((end_time-init_time)/1000000000)+" s")
        break 

pygame.quit()