import time
import pygame
pygame.init()
window = pygame.display.set_mode((1000,800))
clock = time.Clock()

while True:
    for event in event.get():
        if event.type == QUIT:
            quit()
    display.update()
    clock.tick(60)