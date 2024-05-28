#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jd0919889
#
# Created:     05/11/2019
# Copyright:   (c) jd0919889 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys, pygame
pygame.init()
pygame.surface
size = width, height = 320, 320
speed =[2, 2]
black = 0, 0, 0
yellow = 255, 255, 0
white = 255, 255, 255
green = 0, 128, 0

caption = pygame.display.set_caption("Smiley face")

screen= pygame.display.set_mode(size)



while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys. exit()

    surface((160, 160), flags=0, depth=0, masks=None)

    face = pygame.draw.circle(surface, yellow, (160, 160), 160)

    screen.fill(black)
    screen.blit(face)
    pygame.display.flip()