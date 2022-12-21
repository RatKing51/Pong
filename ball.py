import pygame 
from pygame import *
import random

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, win):
        super().__init__()
        self.x = int(x)
        self.y = int(y)
        self.screen = win
        self.velX = 0
        self.velY = 0
        self.color = (255, 0 ,0)
        self.speed = 2
        self.rect = Rect(self.x, self.y, 15, 15)
        self.score1 = 0
        self.score2 = 0

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        self.velX = 0
        self.velX = self.speed

        if self.x >= 785:
            self.speed = -2
            self.velY = random.randint(-1, 1)
            self.score1 += 1
        if self.x <= 0:
            self.speed = 2
            self.velY = random.randint(-1, 1)
            self.score2 += 1
        if self.y >= 585:
            self.velY = -random.randint(1, 2)
        if self.y <= 0:
            self.velY = random.randint(1, 2)
        self.x += self.velX
        self.y += self.velY

        self.rect = Rect(self.x, self.y, 15, 15)

    def bounce(self, paddle):
        if paddle == 1:
            self.speed = 3
            self.velY = random.randint(-1, 1)
        if paddle == 2:
            self.speed = -3
            self.velY = random.randint(-1, 1)
