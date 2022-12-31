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


screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
player_image = pygame.image.load(r'/home/dog7t/Documents/Python Files/platformin/images_platformin/gamin.png').convert()

moving_right = False
moving_left = False

player_location = [50, 50]
player_y_momentum = 0

player_rect = pygame.Rect(player_location[0], player_location[1], player_image.get_height(), player_image.get_width())
            # rectangles use (x, y, height, width) as parameters 
test_rect = pygame.Rect(100, 100, 100, 50)

while True:
    screen.fill((0,0,0))

    screen.blit(player_image, player_location)

    if player_location[1] > WINDOW_SIZE[1] - player_image.get_height():
        player_y_momentum = -player_y_momentum
    else:
        player_y_momentum += 0.5
    player_location[1] += player_y_momentum

    if moving_right == True:
        player_location[0] += 4
    if moving_left == True:
        player_location[0] -= 4

    player_rect.x = player_location[0]
    player_rect.y = player_location[1]

    if player_rect.colliderect(test_rect):
        pygame.draw.rect(screen, (255, 0, 0), test_rect)
    else:
        pygame.draw.rect(screen, (0, 180, 0), test_rect)

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