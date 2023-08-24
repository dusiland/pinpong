import pygame
import time
pygame.init()

win_width, win_height = 900, 600

window = pygame.display.set_mode((win_width, win_height))

FPS = 60
clock = pygame.time.Clock()

class Ball():
    def __init__(self, x, y, w, h, image, x_sp, y_sp):
        super().__init__()
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.transform.scale(image, (w, h))
        self.x_sp = x_sp
        self.y_sp = y_sp

    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player():
    def __init__(self, x, y, w, h, image, speed):
        super().__init__()
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.transform.scale(image, (w, h))
        self.speed = speed

    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


ball_pic = pygame.image.load('pic/ball.png')

ball = Ball(300, 300, 75, 75, ball_pic, 5, 5)




game = True
while game:

    window.fill((27, 242, 235))

    ball.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    pygame.display.update()
    clock.tick(FPS)