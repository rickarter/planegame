# Версия 1
# Подключаем библиотеки
import pygame
from pygame.locals import * 
from control import Control
from plane import Plane

# Задаем разрешение экрана
win = pygame.display.set_mode((1440, 900), FULLSCREEN)
# win = pygame.display.set_mode((500, 500))
# Задаем название окна
pygame.display.set_caption("Plane Game")

# Переменная типа Control
control = Control()
# Переменные типа Plane
plane1 = Plane("yellow")
plane2 = Plane("green")


while control.flag_game: 
	control.Control()
	control.DrawBackground(win)

	plane1.Animation(win)
	plane1.Shoot(win, plane2)
	plane1.Health(win, (243, 224, 119))

	plane2.Animation(win)
	plane2.Shoot(win, plane1)
	plane2.Health(win, (119, 200, 176))

exit()