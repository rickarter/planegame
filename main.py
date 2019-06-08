# Подключаем библиотеки
import pygame
from pygame.locals import *
from control import Control
from plane import Plane

# Задаем разрешение экрана
win = pygame.display.set_mode((500, 500))
# Задаем название окна
pygame.display.set_caption("Plane Game")

# Переменная типа Control
control = Control()
# Переменные типа Plane
plane1 = Plane("yellow")


while control.flag_game: 
	control.Control()
	control.DrawBackground(win)
	plane1.Animation(win)

exit()