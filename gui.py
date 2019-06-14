import pygame

class GUI:
	def __init__(self):
		self.yellow_plane_image = pygame.image.load("gui/yplane.png")
		self.green_plane_image = pygame.image.load("gui/gplane.png")
		# self.heart_image = pygame.image.load("heart.png")
		self.heart_image = pygame.image.load("newheart.png")
		self.fuel_image = pygame.image.load("bigfuel.png")
		self.plane_width = 80
		self.plane_height = 80
		self.heart_height = 35
		self.heart_width = 35
		self.fuel_width = 35
		self.fuel_height = 35
	def Draw(self, win, plane1, plane2):
		# pygame.draw.rect(win, (162, 32, 150), (0, 0, 80 + 150 + 10, 80 + 5))
		# pygame.draw.rect(win, (234, 51, 35), (1440 - 80 - 150 - 10, 0, 80 + 150 + 10, 80 + 5))
		# pygame.draw.rect(win, (162, 32, 150), (1440 - 80 - 150 - 10, 0, 80 + 150 + 10, 80 + 5))

		win.blit(self.yellow_plane_image, (0, 0))
		win.blit(self.green_plane_image, (1440 - self.plane_width, 0))

		# Статистика жизней первого самолета
		win.blit(self.heart_image, (self.plane_width + 5, 0))
		pygame.draw.rect(win, (243, 224, 119), (self.plane_width + self.heart_width + 15, 10, 150, 10), 1)
		if plane1.health > 0:
			pygame.draw.rect(win, (243, 224, 119), (self.plane_width + self.heart_width + 15, 10, 150 / 100 * plane1.health, 10))

		# Статистика жизней второго самолета
		win.blit(self.heart_image, (1440 - self.plane_width - self.heart_width - 5, 0))
		pygame.draw.rect(win, (119, 200, 176), (1440 - self.plane_width - 150 - self.heart_width - 15, 10, 150, 10), 1)
		if plane2.health > 0:
			pygame.draw.rect(win, (119, 200, 176), (1440 - self.plane_width - 150 - self.heart_width - 15, 10, 150 / 100 * plane2.health, 10))

		# Статистика вывода топлива первого самолета
		win.blit(self.fuel_image, (self.plane_width + 5, 35))
		pygame.draw.rect(win, (119, 200, 176), (self.plane_width + self.fuel_width + 15, 50, 150, 10), 1)
		if plane1.ifuel > 0:
			pygame.draw.rect(win, (119, 200, 176), (self.plane_width + self.fuel_width + 15, 50, 150 / 100 * plane1.ifuel, 10))

		# Статистикаа вывода второго самолета
		win.blit(self.fuel_image, (1440 - self.plane_width - self.fuel_width - 5, 35))
		pygame.draw.rect(win, (243, 224, 119), (1440 - self.plane_width - 150 - self.fuel_width - 15, 50, 150, 10), 1)
		if plane1.ifuel > 0:
			pygame.draw.rect(win, (243, 224, 119), (1440 - self.plane_width - 150 - self.fuel_width - 15, 50, 150 / 100 * plane2.ifuel,10))