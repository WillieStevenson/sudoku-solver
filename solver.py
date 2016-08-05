###
## Author: Willie Stevenson
## Sudoku Solver
## An under 100 line sudoku solver in Python that utilizes the recursive backtracking algorithm to solve sudoku puzzles.
###

from collections import Counter

def read_puzzle(filename):
	# read in puzzle
	tempBase = []
	tempRow = []

	with open(filename) as f:
		while True:
			c = f.read(1)

			if not c:
				break
			if c == '\n':
				tempBase.append(tempRow)
				tempRow = []
			else:
				tempRow.append(c)
				
	return tempBase

def print_puzzle(filename, array):
	print "\n--", filename, "--\n"

	for i in range(9):
		if i%3 == 0:
			print "+-------+-------+-------+"
		print "|",
		for j in range(9):
			if j%3 == 0 and j > 0:
				print "|",
			print array[i][j],
		print "|"
	print "+-------+-------+-------+"	

def verify(grid, index_i, index_j, val):
	# verify row and column by building the row and column list based 
	# on the passed indicie if the count of value at indicie is more
	# or than 0, return false sum should always 0 or higher
	rc = ([grid[i][index_j] for i in range(9)].count(val) + [grid[index_i][i] for i in range(9)].count(val) == 0)
	
	# verify quadrant
	# gets sudoku grid quadrant as list and count the occurences of all items as a list
	item_count = Counter(get_quadrant(grid, index_i, index_j, val))
	
	q = True

	for i in item_count:
		if i != ' ':
			if item_count[i] > 1:
				q = False

	return rc and q

def get_quadrant(array, index_i, index_j, val):
	for i in range(0,7,3):
		if i%3 == 0:
			for j in range(0,7,3):
				if j%3 == 0:
					for a in range(i,i+3):
						for b in range(j,j+3):
							if index_i == a and index_j == b:
								array[index_i][index_j] = val
								quad = [array[z][j:j+3] for z in range(i,i+3)]
								return [q for u in quad for q in u] 

def solve(index_i, index_j, grid):
	if index_i == 9:
		index_i = 0
		index_j = index_j + 1
		if index_j == 9:
			return True
	if grid[index_i][index_j] != ' ':
		return solve(index_i+1, index_j, grid)
	for val in range(1, 10):
		if verify(grid, index_i, index_j, str(val)):
			grid[index_i][index_j] = str(val)
			# print_puzzle('the puzzle - solving', grid)
			if solve(index_i+1, index_j, grid):
				return True
	# do some bactracking
	grid[index_i][index_j] = ' '
	return False
	
def do_puzzle_main(filename):
	grid = read_puzzle(filename)
	print_puzzle(filename + ' - start', grid)
	solve(0, 0, grid)
	print_puzzle(filename + ' - finish', grid)

##############################################
do_puzzle_main('puzzle-example1.txt')