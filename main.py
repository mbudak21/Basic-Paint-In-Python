import pygame
import os
import sys
import time
from util import *
pygame.font.init()
pygame.mixer.init()

GRID_X, GRID_Y = 80, 50

FPS = 120
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint!")
DD_WHITE, D_WHITE, WHITE = (150, 150, 150), (200, 200, 200), (255, 255, 255)
BLACK, L_BLACK, LL_BLACK = (0, 0, 0), (20, 20, 20), (50, 50, 50)



D_RED, RED, L_RED 		   = (235, 0, 0), (255, 0, 0), 	(255, 20, 20)
D_GREEN, GREEN, L_GREEN    = (0, 235, 0), (0, 255, 0), 	(20, 255, 20)
D_BLUE, BLUE, L_BLUE	   = (0, 0, 235), (0, 0, 255), 	(20, 20, 255)
PURPLE, CYAN, YELLOW, PINK = (128, 0, 128), (0, 255, 255), (255, 255, 0), (255, 0, 255)
def clear_grid():
	for i in spot.grid:
		for j in i:
			j.color = (255, 255, 255)
def change_brush_color(color):
	spot.brush_color = color
	cursor_brush.color = color
def change_brush_size(n):
	cursor_brush.size += n


b1  = Button(700, 500, 100, 50-1, DD_WHITE, D_WHITE, WHITE, clear_grid, "Clean")
b2  = Button(700, 550, 100, 50, DD_WHITE, D_WHITE, WHITE, lambda: change_brush_color((255,255,255)), "Erase")

b11 = Button(650, 500, 50-1, 50-1, DD_WHITE, D_WHITE, WHITE, lambda: change_brush_size(1), "+")
b12 = Button(650, 550, 50-1, 50-1, DD_WHITE, D_WHITE, WHITE, lambda: change_brush_size(-1), "-")

b3  = Button(0, 500, 50, 100, BLACK, D_WHITE, WHITE, lambda: change_brush_color(BLACK),)
b4  = Button(50, 500, 50, 100, RED, D_WHITE, WHITE, lambda: change_brush_color(RED),)
b5  = Button(100, 500, 50, 100, GREEN, D_WHITE, WHITE, lambda: change_brush_color(GREEN),)
b6  = Button(150, 500, 50, 100, BLUE, D_WHITE, WHITE, lambda: change_brush_color(BLUE),)
b7  = Button(200, 500, 50, 100, PURPLE, D_WHITE, WHITE, lambda: change_brush_color(PURPLE),)
b8  = Button(250, 500, 50, 100, CYAN, D_WHITE, WHITE, lambda: change_brush_color(CYAN),)
b9  = Button(300, 500, 50, 100, YELLOW, D_WHITE, WHITE, lambda: change_brush_color(YELLOW),)
b10 = Button(350, 500, 50, 100, PINK, D_WHITE, WHITE, lambda: change_brush_color(PINK),)

a = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12]

spot.init_grid(0, 0, 800, 500, GRID_X, GRID_Y)



def draw_window(a):
	WIN.fill((245,245,245))
	Button.handle_draw(a, WIN)
	spot.handle_draw(WIN)
	cursor_brush.draw(WIN)
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
		cursor_brush.set_cursor()
		spot.handle_spots(pygame.mouse.get_pressed()[0], pos)
		Button.handle_buttons(a, pygame.mouse.get_pressed()[0], pos)
		
		if pygame.mouse.get_pressed()[0]:
			col_rects = cursor_brush.check_collision_2D_array(spot.grid)
			spot.spots_clicked(col_rects)

		draw_window(a)


if __name__ == "__main__":
	main()
