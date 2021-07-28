class GridSolver():
	def __init__(self, grid_row_size, start_coord, destination_coord):
		self.x_max = grid_row_size
		self.y_max = grid_row_size
		self.start_coord = start_coord
		self.destination_coord = destination_coord

	def is_coord_in_bounds(self, coord):
		x, y = coord
		return x >= 0 and x < self.x_max and y >= 0 and y < self.y_max

	def solve_path(self, current_path=[], animate_move_callback=None, draw_reset_callback=None):
		# Define our movement directions (up, down, right, left)
		directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
		# If our current path is empty then it's probably the first run so give it our start point
		if len(current_path) == 0:
			current_path.append(self.start_coord)
		# Lets get the coordinate we left off at (end of the current path)
		current_coord = current_path[-1]
		# We want to do depth first because it will make more sense visually
		# Start by getting our nearby coordinates
		for direction in directions:
			nearby_coord = (current_coord[0] + direction[0], current_coord[1] + direction[1])
			# Skip this coordinate if it's not valid or we've been to it already
			if not self.is_coord_in_bounds(nearby_coord) or nearby_coord in current_path:
				continue
			# Add this nearby coordinate to a cloned version of our path since it's valid to pursue
			current_path_copy = current_path.copy()
			current_path_copy.append(nearby_coord)
			# Show that we are pursuing it visually
			if animate_move_callback != None:
				animate_move_callback(current_coord, nearby_coord)
			# Check if we've been to every possible coordinate and this coordinate would get us to our destination
			if nearby_coord == self.destination_coord and len(current_path_copy) == (self.x_max * self.y_max):
				# Return this path since it's the solution
				return current_path_copy
			# Run recursively on this path for depth first search
			solution = self.solve_path(current_path_copy, animate_move_callback, draw_reset_callback)
			# Check if it found a solution and forward it up the call stack
			if solution != None:
				return solution
			# Reset since this was a bust
			if draw_reset_callback != None:
				draw_reset_callback(current_path)
		# We explored all of our options and found no solution
		return None

def clone_path(path):
	new_path = []
	for coord in path:
		new_path.append((coord[0], coord[1]))
	return new_path

def print_coord_array(coord_array):
	output_string = ""
	for i in range(0, len(coord_array)):
		output_string += str(coord_array[i])
		if i < len(coord_array) - 1:
			output_string += " -> "
	print(output_string)

def draw_point(p):
	print(str(p))


def draw_move(p1, p2, animation_delay=0.05):
	# time.sleep(animation_delay)
	if (p1[0] != p2[0] and p1[1] != p2[1]):
		print("WHAT THE FUCK")
	print("{} -> {}".format(str(p1), str(p2)))

def reset_board():
	print('\n' * 10)

def draw_reset(traveled_array):
	reset_board()
	for i in range(0, len(traveled_array)):
		if i == 0:
			draw_point(traveled_array[i])
			continue
		draw_move(traveled_array[i - 1], traveled_array[i], 0)

def main():
	grid_solver = GridSolver(grid_row_size=4, start_coord=(0, 0), destination_coord=(3, 3))
	path = grid_solver.solve_path(animate_move_callback=draw_move, draw_reset_callback=draw_reset)
	if path == None:
		print("no path found")
		return
	print_coord_array(path)

if __name__ == '__main__':
	main()