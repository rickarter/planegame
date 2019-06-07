import pygame
from pygame.locals import *
class Control:
	def __init__(self):
		self.flag_game = True 

	def Control(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.flag_game = False
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					self.flag_game = False