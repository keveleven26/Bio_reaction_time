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


running = True
while running: 
    pygame.event.get()
    if Start == False:
        delay = random.randint(3,5)
        time.sleep(delay)
        Start = True
    elif Start == True:
        screen.fill(saturated)
        pygame.display.flip()
        start_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Start == False
                    end_time = pygame.time.get_ticks()
                    screen.fill(black)
                    pygame.display.flip()
                    print(float(end_time-start_time))
                    break

pygame.quit()