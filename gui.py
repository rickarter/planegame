import pygame

class GUI:
	def __init__(self):
		self.yellow_plane_image = pygame.image.load("gui/yplane.png")
		# self.green_plane_image = pygame.image.load("gui/gplane.png")

	def Draw(self, win, plane1, plane2):
		win.blit(self.yellow_plane_image,(0, 0))