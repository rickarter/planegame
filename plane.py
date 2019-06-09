import pygame
from pygame.locals import *
class Plane:
	def __init__(self, color):
		# Переменный, хранящие координаты по осям x и y
		self.x = 10
		self.y = 10
		# Переменная жизней
		self.health = 100
		# Переменные, хранящие размеры
		self.height = 60
		self.width = 60
		# Переменная хранящая скорость
		self.speed = 10
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
		self.bullets = []

		# Переманная направления персонажа
		self.facing = "right"

		# Список хранящицй нажатые кнопки
		self.keys = []

	# Функция анимации самолета
	def Animation(self, win):
		self.keys = pygame.key.get_pressed()

		# Смена анимаций при нажатии клавиш
		if self.color == "yellow":
			if self.keys[K_w]:
				self.facing = "up"
				self.y -= self.speed
			elif self.keys[K_d]:
				self.facing = "right"
				self.x += self.speed
			elif self.keys[K_s]:
				self.facing = "down"
				self.y += self.speed
			elif self.keys[K_a]:
				self.facing = "left"
				self.x -= self.speed

		if self.color == "green":
			if self.keys[K_UP]:
				self.facing = "up"
				self.y -= self.speed
			elif self.keys[K_RIGHT]:
				self.facing = "right"
				self.x += self.speed
			elif self.keys[K_DOWN]:
				self.facing = "down"
				self.y += self.speed
			elif self.keys[K_LEFT]:
				self.facing = "left"
				self.x -= self.speed

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


	def Shoot(self, win, plane):
		if self.color == "yellow":
			if self.keys[K_SPACE]:
			# Добавляем пулю если их меньше восьми
				if len(self.bullets) < 8:
					if self.facing == "up":
						self.bullets.append(self.Bullet(round(self.x + self.width / 4 - 2), self.y, (255, 0, 0), self.facing))
						self.bullets.append(self.Bullet(round(self.x + self.width - self.width / 4 - 2), self.y, (255, 0, 0), self.facing))
					if self.facing == "right":
						self.bullets.append(self.Bullet(self.x + self.width, round(self.y + self.height / 4), (255, 0, 0), self.facing))
						self.bullets.append(self.Bullet(self.x + self.width, round(self.y + self.height - self.height / 4 - 3), (255, 0, 0), self.facing))
					if self.facing == "down":
						self.bullets.append(self.Bullet(round(self.x + self.width / 4 - 3), self.y + self.height, (255, 0, 0), self.facing))
						self.bullets.append(self.Bullet(round(self.x + self.width - self.width / 4 - 2), self.y + self.height, (255, 0, 0), self.facing))
					if self.facing == "left":
						self.bullets.append(self.Bullet(self.x, round(self.y + self.height / 4), (255, 0, 0), self.facing))
						self.bullets.append(self.Bullet(self.x, round(self.y + self.height - self.height / 4 - 3), (255, 0, 0), self.facing))
					'''if self.facing == "up":
						self.bullets.append(self.Bullet(round(self.x + self.width / 2), round(self.y - 10), (255, 0, 0), self.facing))
					elif self.facing == "right":
						self.bullets.append(self.Bullet(round(self.x + self.width + 10), round(self.y + self.height / 2), (255, 0, 0), self.facing))
					elif self.facing == "down":
						self.bullets.append(self.Bullet(round(self.x + self.width / 2), round(self.y + self.height + 10), (255, 0, 0), self.facing))
					elif self.facing == "left":
						self.bullets.append(self.Bullet(round(self.x - 10), round(self.y + self.height / 2), (255, 0, 0), self.facing))'''

		if self.color == "green":
			if self.keys[K_RSHIFT]:
			# Добавляем пулю если их меньше восьми
				if len(self.bullets) < 8:
					if self.facing == "up":
						self.bullets.append(self.Bullet(round(self.x + self.width / 4 - 2), self.y, (255, 0, 0), self.facing))
						self.bullets.append(self.Bullet(round(self.x + self.width - self.width / 4 - 2), self.y, (255, 0, 0), self.facing))
					if self.facing == "right":
						self.bullets.append(self.Bullet(self.x + self.width, round(self.y + self.height / 4), (255, 0, 0), self.facing))
						self.bullets.append(self.Bullet(self.x + self.width, round(self.y + self.height - self.height / 4 - 3), (255, 0, 0), self.facing))
					if self.facing == "down":
						self.bullets.append(self.Bullet(round(self.x + self.width / 4 - 3), self.y + self.height, (255, 0, 0), self.facing))
						self.bullets.append(self.Bullet(round(self.x + self.width - self.width / 4 - 2), self.y + self.height, (255, 0, 0), self.facing))
					if self.facing == "left":
						self.bullets.append(self.Bullet(self.x, round(self.y + self.height / 4), (255, 0, 0), self.facing))
						self.bullets.append(self.Bullet(self.x, round(self.y + self.height - self.height / 4 - 3), (255, 0, 0), self.facing))

		# Проверка каждой пули, её отрисовка и проверка на попадание
		for bullet in self.bullets:
			if 0 < bullet.x < 1440 and 0 < bullet.y < 900:
				if bullet.facing == "up":
					bullet.y -= bullet.velocity
				if bullet.facing == "right":
					bullet.x += bullet.velocity
				if bullet.facing == "down":
					bullet.y += bullet.velocity
				if bullet.facing == "left":
					bullet.x -= bullet.velocity
			else:
				self.bullets.pop(self.bullets.index(bullet))
			bullet.Draw(win)

			if plane.x <= bullet.x <= (plane.x + plane.width) and plane.y <= bullet.y <= (plane.y + plane.height):
				self.health -= bullet.power

	def Health(self, win):
		pass


	class Bullet:
		def __init__(self, x, y, color, facing):
			# Переменные координаты пули
			self.x = x
			self.y = y
			# Переменная скорости пули
			self.velocity = 20
			# Переменная цвета пули
			self.color = color
			# Переменная направления пули
			self.facing = facing
			# Переменная радиуса пули
			self.radius = 6
			# Перемиенная мощности пули
			self.power = 10
			
		# Функция отрисовки пули
		def Draw(self, win):
			# pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
			if self.facing == "up" or self.facing == "down":
				pygame.draw.rect(win, self.color, (self.x, self.y, 4, 10))
			if self.facing == "right" or self.facing == "left":
				pygame.draw.rect(win, self.color, (self.x, self.y, 10, 4))