import pygame, sys
from pygame import mixer
from pygame.locals import*
import random

from grid import Grid

pygame.init()

# set up game screen
# screen = pygame.display.set_mode((300,600))
screen = pygame.display.set_mode((500,800))
pygame.display.set_caption("Pygame Tetris")
fps = 60
clock = pygame.time.Clock()

dark_blue = (44, 44, 127)

print('running file')



game_grid = Grid()
#game_grid.print_grid()

game_grid.grid[0][0] = 1  3 32:13
game_grid.grid[3][5] = 4
game_grid.grid[17][8] = 7

run = True
while run:
    clock.tick(fps)

    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
            run = False

    screen.fill(dark_blue)
    game_grid.draw(screen)



    pygame.display.update()




pygame.quit()
print("Good bye")
sys.exit()
