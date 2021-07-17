import sys
import pygame

class GridSolverUI():
	# Constants
	SCREEN_HEIGHT_WIDTH = 800
	GRID_ROW_SIZE = 4 # Needs to be a perfect square
	COLOR_BLACK = (0, 0, 0)
	COLOR_WHITE = (255, 255, 255)
	COLOR_RED = (255, 0, 0)
	CELL_SPACING = 10 # Needs to be even
	CELL_BORDER_SIZE = 2
	POINT_RADIUS = 20
	LINE_WIDTH = 9 # Needs to be odd for line to be centered
	ANIMATION_INTERVAL = 100 # Interval in milliseconds
	# Variables
	running = False

	def __init__(self, grid_solver):
		# Calculate "constant"
		self.GRID_CELL_SIZE = (self.SCREEN_HEIGHT_WIDTH - self.CELL_SPACING) / self.GRID_ROW_SIZE
		self.grid_solver = grid_solver
		# Initialize Pygame
		pygame.init()
		self.surface = pygame.display.set_mode((self.SCREEN_HEIGHT_WIDTH, self.SCREEN_HEIGHT_WIDTH))

	def draw_grid(self):
		# Create grid squares
		for x in range(0, self.GRID_ROW_SIZE):
			for y in range(0, self.GRID_ROW_SIZE):
				pos_1 = (self.GRID_CELL_SIZE * (x % self.GRID_ROW_SIZE) + self.CELL_SPACING, self.GRID_CELL_SIZE * (y % self.GRID_ROW_SIZE) + self.CELL_SPACING)
				pos_2 = (self.GRID_CELL_SIZE - self.CELL_SPACING, self.GRID_CELL_SIZE - self.CELL_SPACING)
				rect = pygame.Rect(pos_1, pos_2)
				pygame.draw.rect(self.surface, self.COLOR_WHITE, rect, self.CELL_BORDER_SIZE)

	def reset_grid(self):
		# Reset screen
		self.surface.fill(self.COLOR_BLACK)
		# Draw initial grid
		self.draw_grid()
		pygame.display.flip()

	def find_center(self, cell_pos):
		(x, y) = cell_pos
		return (self.GRID_CELL_SIZE * (x % self.GRID_ROW_SIZE) + (self.CELL_SPACING / 2) + (self.GRID_CELL_SIZE / 2), self.GRID_CELL_SIZE * (y % self.GRID_ROW_SIZE) + (self.CELL_SPACING / 2) + (self.GRID_CELL_SIZE / 2))

	def draw_point(self, cell_pos):
		pygame.draw.circle(self.surface, self.COLOR_RED, self.find_center(cell_pos), self.POINT_RADIUS)

	def draw_line_between(self, cell_pos1, cell_pos2):
		pygame.draw.line(self.surface, self.COLOR_RED, self.find_center(cell_pos1), self.find_center(cell_pos2), self.LINE_WIDTH)

	def run(self):
		self.running = True
		self.reset_grid()
		# Debug (animating travel)
		points = []
		for x in range(0, self.GRID_ROW_SIZE):
			for y in range(0, self.GRID_ROW_SIZE):
				points.append((x, y))
		self.draw_point(points[0])
		pygame.display.flip()
		pygame.time.wait(self.ANIMATION_INTERVAL)
		i = 0
		while i < len(points) - 1:
			self.draw_line_between(points[i], points[i + 1])
			pygame.display.flip()
			pygame.time.wait(self.ANIMATION_INTERVAL)
			self.draw_point(points[i + 1])
			pygame.display.flip()
			pygame.time.wait(self.ANIMATION_INTERVAL)
			i += 1
		# End debug
		# Game loop
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					break
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.running = False
						break
		# Game loop broke, bye bye
		pygame.quit()
		sys.exit()
