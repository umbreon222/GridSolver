class GridSolver():
	grid = None

	def __init__(grid_row_size, start_cell, end_cell):
		self.grid_row_size = grid_row_size
		self.start_cell = start_cell
		self.end_cell = end_cell

	def reset_grid():
		# Build grid
		self.grid = [[0 for x in range(0, self.grid_row_size)] for x in range(0, self.grid_row_size)]
