import pygame
import random

class Fuel:
	def __init__(self):
		# Переменные ширины и высоты топлива
		self.height = 22
		self.width = 22
		# Переменные координат топлива
		self.x = random.randint(0, 1440 - self.width)
		self.y = random.randint(0, 900 - self.height)
		# Изображение топлива 
		self.fuel = pygame.image.load("fuel.png")


	'''def Draw(self, win, plane1, plane2):
		if self.x <= plane1.x <= self.x + self.width \
			and self.y <= plane1.y <= self.y + self.height \
			or self.x <= plane1.x <= self.x + self.width \
			and self.y <= plane1.y + self.height <= self.y + self.height \
			or self.x <= plane1.x + self.width <= self.x + self.width \
			and self.y <= plane1.y <= self.y + self.height:

			plane1.fuel += self.fuel_size

		if self.x <= plane2.x <= self.x + self.width \
			and self.y <= plane2.y <= self.y + self.height \
			or self.x <= plane2.x <= self.x + self.width \
			and self.y <= plane2.y + self.height <= self.y + self.height \
			or self.x <= plane2.x + self.width <= self.x + self.width \
			and self.y <= plane2.y <= self.y + self.height:

			plane2.fuel += self.fuel_size

		win.blit(self.fuel, (self.x, self.y))'''

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
			plane1.ifuel += random.randint(round((100 - plane1.ifuel) / 2), round(100 - plane1.ifuel))

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
			plane2.ifuel += random.randint(round((100 - plane2.ifuel) / 2), round(100 - plane2.ifuel))

		win.blit(self.fuel, (self.x, self.y))
