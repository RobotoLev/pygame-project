import random
import pygame
# import system_functions

FPS = 50
WIDTH = 200
HEIGHT = 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
running = True
iteration = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if iteration % FPS == 0:
        screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    iteration += 1

    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()
