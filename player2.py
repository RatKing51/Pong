import pygame
from pygame import *

class PlayerArrow(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = int(x)
        self.y = int(y)
        self.rect = Rect(self.x, self.y, 32, 100)
        self.color  = (255, 255, 255)
        self.velY = 0
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4
    
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
    
    def update(self):
        self.velY = 0
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed

        self.y += self.velY

        if self.y <= 0:
            self.y = 0
        if self.y >= 500:
            self.y = 500

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 100)
    