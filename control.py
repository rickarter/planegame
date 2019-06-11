import pygame
from pygame.locals import *
class Control:
	def __init__(self):
		# Флаг, отвечающий за работу цикла
		self.flag_game = True
		# Создаем таймер
		self.timer = pygame.time.Clock()
		# Картинка фона
		self.background = pygame.image.load("background.JPG")

	def Control(self):
		# Ограничиваем игру в 60 фпс
		self.timer.tick(60)
		for event in pygame.event.get():
			# Останавливаем основной цикл если была нажата кнопка выйти
			if event.type == QUIT:
				self.flag_game = False
			# Проверяем была ли нажата кнопка
			elif event.type == KEYDOWN:
				# если был нажат ESCAPE завершаем цикл
				if event.key == K_ESCAPE:
					self.flag_game = False
		pygame.display.update()

	# Функция, отрисовывающая задний фон
	def DrawBackground(self, win):
		# win.fill((0, 0, 0))
		win.blit(self.background, (0, 0))
