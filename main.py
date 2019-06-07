import pygame
from pygame.locals import *
from control import Control

win = pygame.display.set_mode((500, 500))
control = Control()

timer = pygame.time.Clock()

while control.flag_game:
	timer.tick(60)
	control.Control()


	pygame.display.update
exit()