#11: Largest product in a grid

#!/bin/python3

import sys


grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)

len_g = len(grid)
numbers = []
    
for i in range(len_g):
    for j in range(len_g):
        # UP
        if (i-3 >= 0):
            number = grid[i][j] * grid[i-1][j] * grid[i-2][j] * grid[i-3][j]
            numbers.append(number)
        # DOWN
        if (i+3 < len_g):
            number = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
            numbers.append(number)
        # LEFT
        if (j-3 >= 0):
            number = grid[i][j] * grid[i][j-1] * grid[i][j-2] * grid[i][j-3]
            numbers.append(number)
        # RIGHT
        if (j+3 < len_g):
            number = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
            numbers.append(number)
        # DIAGONAL
        # DOWN RIGHT
        if (j+3 < len_g and i+3 < len_g):
            number = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
            numbers.append(number)
        # DOWN LEFT
        if (j-3 >= 0 and i+3 < len_g):
            number = grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3]
            numbers.append(number)
        # UP LEFT
        if (j-3 >= 0 and i-3 >= 0):
            number = grid[i][j] * grid[i-1][j-1] * grid[i-2][j-2] * grid[i-3][j-3]
            numbers.append(number)
        # UP RIGHT
        if (j+3 < len_g and i-3 >= 0):
            number = grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2] * grid[i-3][j+3]
            numbers.append(number)
        
print(max(numbers))