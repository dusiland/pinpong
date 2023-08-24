import pygame
import time
pygame.init()

win_width, win_height = 700, 500

window = pygame.display.set_mode((win_width, win_height))

FPS = 60
clock = pygame.time.Clock()

game = True

while game:

    window.fill((27, 242, 235))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    pygame.display.update()
    clock.tick(FPS)