import pygame
from pygame.locals import *
class Plane:
	def __init__(self, color):
		# Переменный, хранящие координаты по осям x и y
		self.x = 10
		self.y = 10
		# Переменная хранящая скорость
		self.speed = 20
		# Переменная, которая хранит номер анимации
		self.anim_count = 0
		self.color = color
		# Объявляем кортеж, кторый хранит путь до изображений, и передаем значение в зависимости от цвета
		self.animation = ("",)
		if self.color == "yellow":
			self.animation  = ("yp/plane0.png", "yp/plane1.png", "yp/plane2.png", "yp/plane3.png")
		elif self.color == "green":
			self.animation  = ("gp/plane0.png", "gp/plane1.png", "gp/plane2.png", "gp/plane3.png")

		# Переменная, хранящая изображения
		self.plane = pygame.image.load(self.animation[self.anim_count])

		# Список хранящий пули
		self.bulllets = []

		# Переманная направления персонажа
		self.facing = "right"

	# Функция анимации самолета
	def Animation(self, win):
		keys = pygame.key.get_pressed()

		# Смена анимаций при нажатии клавиш
		if self.color == "yellow":
			if keys[K_w]:
				self.facing = "up"
				self.y -= self.speed
			elif keys[K_d]:
				self.facing = "right"
				self.x += self.speed
			elif keys[K_s]:
				self.facing = "down"
				self.y += self.speed
			elif keys[K_a]:
				self.facing = "left"
				self.x -= self.speed
			if keys[K_SPACE]:
				self.Shoot()

		if self.color == "green":
			if keys[K_UP]:
				self.facing = "up"
				self.y -= self.speed
			elif keys[K_RIGHT]:
				self.facing = "right"
				self.x += self.speed
			elif keys[K_DOWN]:
				self.facing = "down"
				self.y += self.speed
			elif keys[K_LEFT]:
				self.facing = "left"
				self.x -= self.speed
			if keys[K_LSHIFT]:
				self.Shoot()

		if self.facing == "up":
			self.anim_count = 0
		elif self.facing == "right":
			self.anim_count = 1
		elif self.facing == "down":
			self.anim_count = 2
		elif self.facing == "left":
			self.anim_count = 3

		# Загрузка изображения в переменную
		self.plane = pygame.image.load(self.animation[self.anim_count])
		# Вывод изображения на экран
		win.blit(self.plane, (self.x, self.y))



	def Shoot(self):
		pass

	class bulllet:
		def __init__(self, x, y, color, facing):
			# Переменные координаты пули
			self.x = x
			self.y = y
			# Переменная скорости пули
			self.velocity = 12
			# Переменная цвета пули
			self.color = color
			# Переменная направления пули
			self.facing = facing
			# Переменная радиуса пули
			self.radius = 15

		# Функция отрисовки пули
		def Draw(self, win):
			pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)