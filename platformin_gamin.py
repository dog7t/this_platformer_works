# Make a basic platformer for now. Once you can do that, you can move on and add some more features and try out stuff
# make some epic cool pixelartin too ye
# 
import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption('platformin rn')

WIDTH = 1000
HEIGHT = 800
WINDOW_SIZE = (WIDTH, HEIGHT)


# Notes about how surfaces work:
# if you render an image onto a surface first, and then scale it up by rendering onto another surface,
# (in this case, the main window) you can initially use a small image with a few pixels, and then maintain
# the pixel look but actually have a big window you can actually play the game in
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
display = pygame.surface((300, 200))



player_image = pygame.image.load(r'/home/dog7t/Documents/Python Files/platformin/images_platformin/gamin.png').convert()

grass_image = pygame.image.load('grass.png')
dirt_image = pygame.image.load('dirt.png')

moving_right = False
moving_left = False

player_location = [50, 50]
player_y_momentum = 0

# collisions
# player_rect = pygame.Rect(player_location[0], player_location[1], player_image.get_height(), player_image.get_width())
#             # rectangles use (x, y, height, width) as parameters 
# test_rect = pygame.Rect(100, 100, 100, 50)



# game_map[y][x], basically first comes the y collumn, then comes the x collumnn when calling from the game map

game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','2','2','2','2','2','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2'],
            ['1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]

while True:
    screen.fill((0,0,0))

    screen.blit(player_image, player_location)


    player_y_momentum += 0.5
    player_location[1] += player_y_momentum

    if moving_right == True:
        player_location[0] += 4
    if moving_left == True:
        player_location[0] -= 4

    player_rect.x = player_location[0]
    player_rect.y = player_location[1]

    # if player_rect.colliderect(test_rect):
    #     pygame.draw.rect(screen, (255, 0, 0), test_rect)
    # else:
    #     pygame.draw.rect(screen, (0, 180, 0), test_rect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right = True
            if event.key == K_LEFT:
                moving_left = True

        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False
                        

    pygame.display.update()
    clock.tick(60) 