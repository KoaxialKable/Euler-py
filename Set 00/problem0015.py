#! /usr/bin/env python
############################################
#	Problem 15
#	Lattice Paths
#
#	Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
#	there are exactly 6 routes to the bottom right corner.
#
#	How many such routes are there through a 20×20 grid?
#
#	Answer: 137846528820
############################################
GRID_SIZE = 20

def count_paths(width, height):
	grid = [1] * (width * height)

	x,y = 1,1

	while (x < width):
		while (y < height):
			n = (y * width) + x
			grid[n] = grid[n-1] + grid[n-width]
			y += 1
		y = 1
		x += 1
	return grid[n]

print(count_paths(GRID_SIZE+1,GRID_SIZE+1))		# 137846528820