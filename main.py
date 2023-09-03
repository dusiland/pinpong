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

    def move(self):
        self.rect.x += self.x_sp
        self.rect.y += self.y_sp
        if self.rect.bottom == win_height:
            self.y_sp *= -1
        if self.rect.top == 0:
            self.y_sp *= -1

    def colide(self, item):
        if self.rect.colliderect(item.rect):
            return True
        else:
            return False

class Player():
    def __init__(self, x, y, w, h, image, speed):
        super().__init__()
        self.rect = pygame.Rect(x, y, w, h)
        self.image = pygame.transform.scale(image, (w, h))
        self.speed = speed

    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, down, up):
        k = pygame.key.get_pressed()
        if k[down] and (win_height - self.rect.y) >= self.rect.h:
            self.rect.y += self.speed
        if k[up] and self.rect.y >= 0:
            self.rect.y -= self.speed


ball_pic = pygame.image.load('pic/ball.png')

ball = Ball(300, 300, 75, 75, ball_pic, 5, 5)

player_pic = pygame.image.load('pic/block.png')

player1 = Player(75, 250, 50,100, player_pic, 5)
player2 = Player(775, 250, 50,100, player_pic, 5)

font = pygame.font.SysFont('Mistral', 40)

gamemode = 'menu'
game = True
while game:
    if gamemode == 'menu':
        window.fill((27, 242, 235))
        new_lb =font.render ("Натисніть ENTER щоб почати знову", True, (255,255,255)) 
        window.blit(new_lb,(190,270))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                gamemode = 'game'

    if gamemode == 'game':

        window.fill((27, 242, 235))
        player1.update()
        player2.update()
        ball.update()

        player1.move(pygame.K_s, pygame.K_w)
        player2.move(pygame.K_DOWN, pygame.K_UP)
        ball.move()

        if ball.colide(player1) or ball.colide(player2):
            ball.x_sp *= -1

        if ball.rect.x > win_width or ball.rect.x < 0:
            ball.rect.x = 300
            gamemode = 'menu'

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
    
    pygame.display.update()
    clock.tick(FPS)