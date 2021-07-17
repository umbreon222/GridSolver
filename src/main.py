from grid_solver.grid_solver import GridSolver
from grid_solver.grid_solver_ui import GridSolverUI

def main():
	grid_solver = GridSolver(4, (0, 0), (3, 3)) 
	grid_solver_ui = GridSolverUI(grid_solver)
	grid_solver_ui.run()

if __name__ == '__main__':
	main()
