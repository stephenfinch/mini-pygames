import pygame
import os

os.environ['SDL_VIDEO_CENTERED']='1'
pygame.init()

width, height = 600, 600
fps = 60
win = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

### COLORS
WHITE = (255,255,255)
BLACK = (0,0,0)

###

# YOUR CODE HERE

###

run = True
while run:
    clock.tick(fps)
    pygame.display.update()
    win.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    ###

    # YOUR CODE HERE

    ###

pygame.quit()