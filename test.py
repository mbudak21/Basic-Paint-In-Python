import pygame
import os
import sys
import time
pygame.font.init()
pygame.mixer.init()

FPS = 120
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint!")

RED = (255, 0, 0)

class cursor_brush():
	def __init__(self):
		self.x = 0 
		self.y = 0 
		self.w = 10
		self.h = 10
		self.color =  RED
		self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

	def draw(self, win):
		pygame.draw.rect(win, self.color, self.rect)

	def set_cursor(self):
		x, y = pygame.mouse.get_pos()
		x, y = x-(self.w//2), y-(self.h//2)
		self.rect.update((x, y), (self.w, self.h))
		
a = cursor_brush()

def draw_window():
	WIN.fill((245,245,245))
	a.set_cursor()
	a.draw(WIN)
	pygame.display.flip()


def main():


	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()

		#if pygame.mouse.get_pressed()[0]:
		pos = pygame.mouse.get_pos()

		

		draw_window()


if __name__ == "__main__":
	main()
