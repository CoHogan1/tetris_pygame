import pygame, sys
from pygame import mixer
from pygame.locals import*
import random

pygame.init()

# set up game screen
screen = pygame.display.set_mode((300,600))
pygame.display.set_caption("Pygame Tetris")
fps = 60
clock = pygame.time.Clock()

dark_blue = (44, 44, 127)




print('running file')





run = True
while run:
    clock.tick(fps)

    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
            run = False

    screen.fill(dark_blue)
    pygame.display.update()




pygame.quit()
print("Good bye")
sys.exit()
