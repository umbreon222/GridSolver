import sys
import pygame
from grid_solver.grid_solver import GridSolver

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
	ANIMATION_INTERVAL = 7 # Interval in milliseconds
	POLL_INTERVAL = 250 # Interval in milliseconds
	# Variables
	running = False

	def __init__(self):
		# Calculate "constant"
		self.GRID_CELL_SIZE = (self.SCREEN_HEIGHT_WIDTH - self.CELL_SPACING) / self.GRID_ROW_SIZE
		self.grid_solver = GridSolver(self.GRID_ROW_SIZE, start_coord=(0, 0), destination_coord=(3, 3))
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
	
	def animate_move(self, cell_pos1, cell_pos2, skip_animation=False):
		self.draw_line_between(cell_pos1, cell_pos2)
		if not skip_animation:
			pygame.display.flip()
			pygame.time.wait(self.ANIMATION_INTERVAL)
		self.draw_point(cell_pos2)
		pygame.display.flip()
		if not skip_animation:
			pygame.time.wait(self.ANIMATION_INTERVAL)
		self.process_ui_events()

	def draw_reset(self, traveled_array):
		self.reset_grid()
		for i in range(0, len(traveled_array)):
			if i == 0:
				self.draw_point(traveled_array[i])
				continue
			self.animate_move(traveled_array[i - 1], traveled_array[i], skip_animation=True)
		self.process_ui_events()

	def run(self):
		self.running = True
		self.reset_grid()
		self.draw_point(self.grid_solver.start_coord)
		self.grid_solver.solve_path(animate_move_callback=self.animate_move, draw_reset_callback=self.draw_reset)
		while True:
			self.process_ui_events()
			pygame.time.wait(self.POLL_INTERVAL)
	
	# Threading/Async would have to be implemented to handle events properly but this is just a POC and it works so idgaf
	def process_ui_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					sys.exit()
