# imports
import pygame
from pygame import *
import sys
import random
import player1
from player1 import *
import player2
from player2 import *
import ball
from ball import *
import math
import time



# start pygame
pygame.init()

#pygame var/game var
WIDTH = 800
HEIGHT = 600

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
run = True

paddle1 = PlayerKey(0, 270)
paddle2 = PlayerArrow(768, 270)
pong = Ball(400, 295, SCREEN)

font = pygame.font.SysFont('Georgia',20)

clock = pygame.time.Clock()


# images
BACKGROUND = pygame.image.load("assets/background.jpg")


# Main Game loop
def game():
    global run
    while run:

        SCREEN.fill((250, 250, 250))
        SCREEN.blit(BACKGROUND, (0, 0))

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_w:
                    paddle1.up_pressed = True
                if event.key == pygame.K_s:
                    paddle1.down_pressed = True
                if event.key == pygame.K_UP:
                    paddle2.up_pressed = True
                if event.key == pygame.K_DOWN:
                    paddle2.down_pressed = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    paddle1.up_pressed = False
                if event.key == pygame.K_s:
                    paddle1.down_pressed = False
                if event.key == pygame.K_UP:
                    paddle2.up_pressed = False
                if event.key == pygame.K_DOWN:
                    paddle2.down_pressed = False
        
        paddle1.draw(SCREEN)
        paddle1.update()

        paddle2.draw(SCREEN)
        paddle2.update()

        if pygame.sprite.collide_rect(pong, paddle1):
            pong.bounce(1)
        if pygame.sprite.collide_rect(pong, paddle2):
            pong.bounce(2)

        
        score_text1 = font.render("Score: " + str(pong.score1), True, (255, 255, 255))
        SCREEN.blit(score_text1, (50, 50))

        score_text2 = font.render("Score: " + str(pong.score2), True, (255, 255, 255))
        SCREEN.blit(score_text2, (550, 50))
         
        pong.draw()

        pong.update()


    
        
        pygame.display.flip()
        clock.tick(240)

if __name__ == "__main__":
    game()