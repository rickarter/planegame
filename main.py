# Версия 1
# Подключаем библиотеки
import pygame
from pygame.locals import * 
from control import Control
from plane import Plane
from fuel import Fuel
from bullet import Bullet
from gui import GUI
from heart import Heart

# Задаем разрешение экрана
win = pygame.display.set_mode((1440, 900), FULLSCREEN)
# win = pygame.display.set_mode((500, 500))
# Задаем название окна
pygame.display.set_caption("Plane Game")

# Переменная типа Control
control = Control()
# Объекты типа Plane
plane1 = Plane("yellow")
plane2 = Plane("green")
# Объект типа GUI
gui = GUI()

# Объекты типа Fuel
fuels = []
for i in range(0, 2):
	fuels.append(Fuel())
# Объекты типа Bullet
bullets = []
for i in range(0, 10):
	bullets.append(Bullet())
# Объекты типа Heart
hearts = [] 
for i in range(0, 2):
	hearts.append(Heart())

while control.flag_game: 
	control.Control()
	control.DrawBackground(win)

	plane1.Animation(win)
	plane1.Shoot(win, plane2)
	plane1.Fuel()
	plane1.Health(win, control)
	# plane1.Health(win, (243, 224, 119))
	# plane1.Fuel(win, (243, 224, 119))
	if plane1.bexplosion:
		plane1.Explosion(win, control)

	plane2.Animation(win)
	plane2.Shoot(win, plane1)
	plane2.Fuel()
	plane2.Health(win, control)

	# plane2.Health(win, (119, 200, 176))
	# plane2.Fuel(win, (119, 200, 176))

	for fuel in fuels:
		fuel.Draw(win, plane1, plane2)

	for bullet in bullets:
		bullet.Draw(win, plane1, plane2)

	for heart in hearts:
		heart.Draw(win, plane1, plane2)


	gui.Draw(win, plane1, plane2)

exit()