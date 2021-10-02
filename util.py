import pygame

class Button():
	def __init__(self, x, y, w, h, idle_color, hover_color, pressed_color, func, text=""):
		self.x = x 
		self.y = y
		self.width = w 
		self.height = h 
		self.idle_color = idle_color
		self.hover_color = hover_color
		self.pressed_color = pressed_color		
		self.func = func
		self.text = text
		self.pressed = False
		self.hover = False


	def draw(self, win):
		
		if not self.hover and not self.pressed:
			pygame.draw.rect(win, self.idle_color, (self.x,self.y,self.width,self.height),0)

		elif self.hover and not self.pressed:			
			pygame.draw.rect(win, self.hover_color, (self.x,self.y,self.width,self.height),0)

		elif self.hover and self.pressed:			
			pygame.draw.rect(win, self.pressed_color, (self.x,self.y,self.width,self.height),0)

		#pygame.draw.rect(win, self.color1, (self.x,self.y,self.width,self.height),0)
					

		if self.text != '':
			font = pygame.font.SysFont('comicsans', 35)
			text = font.render(self.text, 1, (0,0,0))
			win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

	def isOver(self, pos):
		#Pos is the mouse position or a tuple of (x,y) coordinates
		if pos[0] > self.x and pos[0] < self.x + self.width:
			if pos[1] > self.y and pos[1] < self.y + self.height:
				return True
			else:
				return False
		else: return False


	@staticmethod
	def handle_buttons(buttons, isPressed, pos):
		for button in buttons:
			if button.isOver(pos):
				button.hover = True

				if isPressed:
					button.pressed = True
					button.func()
				else:
					button.pressed = False
			else:
				button.hover = False
	@staticmethod
	def handle_draw(buttons, win):
		if str(type(buttons)) =="<class 'list'>":
			for button in buttons:
				button.draw(win)
		else:
			buttons.draw(win)


class spot():
	brush_color = (255, 0, 0)
	grid = []

	def __init__(self, x, y, w, h, color = (255, 255, 255)):
		self.x = x 
		self.y = y 
		self.w = w 
		self.h = h 
		self.rect = pygame.Rect(x, y, w, h)
		self.color = color

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x,self.y,self.w,self.h),0)

	def isOver(self, pos):
		#Pos is the mouse position or a tuple of (x,y) coordinates
		if pos[0] > self.x and pos[0] < self.x + self.w:
			if pos[1] > self.y and pos[1] < self.y + self.h:
				return True
			else:
				return False
		else: return False

	@classmethod
	def clicked(cls, color):
		cls.brush_color = color


	@classmethod
	def handle_draw(cls, win):
		for i in cls.grid:
			for j in i:
				j.draw(win)

	@classmethod
	def handle_spots(cls, isPressed, pos):
		for i in cls.grid:
			for j in i:
				if j.isOver(pos) and isPressed:
					j.color = cls.brush_color

	@classmethod
	def spots_clicked(cls, spots):
		for spot in spots:
			spot.color = cls.brush_color

	def __repr__(self):
		return str("(") + str(self.x) + ", " + str(self.y) + str(")")


	@staticmethod
	def init_grid(x, y, w, h, cols, rows):
		
		sw, sh = w//cols, h//rows

		for i in range(rows):
			spot.grid.append([])
			for j in range(cols):
				spot.grid[i].append(spot(x + j*sw, y + i*sh, sw, sh))

	@staticmethod
	def print_grid(grid):
		for i in grid:
			for j in i:
				print(j, end=" ")
			print()



class cursor_brush:
	cursor = None
	x = 0 
	y = 0 
	size = 10
	color =  (255,0,0)
	rect = pygame.Rect(x, y, size, size)
	def __init__(self):
		cls.cursor = self

	@classmethod
	def draw(cls, win):
		pygame.draw.rect(win, cls.color, cls.rect)

	@classmethod
	def set_cursor(cls):
		x, y = pygame.mouse.get_pos()
		x, y = x-(cls.size//2), y-(cls.size//2)
		cls.rect.update((x, y), (cls.size, cls.size))

	@classmethod
	def check_collision(cls, in_object):
		return in_object.colliderect(cls.rect)

	@classmethod
	def check_collision_list(cls, in_list):
		out_list = []
		for i in in_list:
			if i.colliderect(cls.rect):
				out_list.append(i)
		return out_list

	@classmethod
	def check_collision_2D_array(cls, in_array):
		out_list = []
		for i in in_array:
			for j in i:
				if j.rect.colliderect(cls.rect):
					out_list.append(j)
		return out_list


