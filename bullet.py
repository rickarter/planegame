import pygame
import random

class Bullet:
	def __init__(self):
		# Переменные ширины и высоты
		self.height = 35
		self.width = 35
		# Переменные координат
		self.x = random.randint(0, 1440 - self.width)
		self.y = random.randint(0, 900 - self.height)
		# Изображение
		self.bullet = pygame.image.load("bullet.png")


	def Draw(self, win, plane1, plane2):
		if self.x <= plane1.x <= self.x + self.width and self.y <= plane1.y <= self.y + self.height \
		or self.x <= plane1.x <= self.x + self.width and self.y <= plane1.y + plane1.height <= self.y + self.height \
		or self.x <= plane1.x + plane1.width <= self.x + self.width and self.y <= plane1.y + plane1.height <= self.y + self.height \
		or self.x <= plane1.x + plane1.width <= self.x + self.width and self.y <= plane1.y <= self.y + self.height \
		or plane1.x <= self.x <= plane1.x + plane1.width and plane1.y <= self.y + self.height <= plane1.y + plane1.height \
		or plane1.x <= self.x <= plane1.x + plane1.width and plane1.y <= self.y <= plane1.y + plane1.height \
		or plane1.x <= self.x + self.width <= plane1.x + plane1.width and plane1.y <= self.y <= plane1.y + plane1.height \
		or plane1.x <= self.x <= plane1.x + plane1.width and plane1.y <= self.y <= plane1.y + plane1.height:
			self.x = random.randint(0, 1440 - self.width)
			self.y = random.randint(0, 900 - self.height)
			plane1.bullets_count += 2

		if self.x <= plane2.x <= self.x + self.width and self.y <= plane2.y <= self.y + self.height \
		or self.x <= plane2.x <= self.x + self.width and self.y <= plane2.y + plane2.height <= self.y + self.height \
		or self.x <= plane2.x + plane2.width <= self.x + self.width and self.y <= plane2.y + plane2.height <= self.y + self.height \
		or self.x <= plane2.x + plane2.width <= self.x + self.width and self.y <= plane2.y <= self.y + self.height \
		or plane2.x <= self.x <= plane2.x + plane2.width and plane2.y <= self.y + self.height <= plane2.y + plane2.height \
		or plane2.x <= self.x <= plane2.x + plane2.width and plane2.y <= self.y <= plane2.y + plane2.height \
		or plane2.x <= self.x + self.width <= plane2.x + plane2.width and plane2.y <= self.y <= plane2.y + plane2.height \
		or plane2.x <= self.x <= plane2.x + plane2.width and plane2.y <= self.y <= plane2.y + plane2.height:
			self.x = random.randint(0, 1440 - self.width)
			self.y = random.randint(0, 900 - self.height)
			plane2.bullets_count += 2

		win.blit(self.bullet, (self.x, self.y))