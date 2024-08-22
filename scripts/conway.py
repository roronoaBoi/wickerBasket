"""
conway's game of life illustrated
"""
# pylint: disable=invalid-name

import time
import random
import copy #copy and deepcopy functions

width = 15
height = 5

next_cells = []

for hor in range(width):
    column = []
    for ver in range(height):
        if random.randint(0,1) == 0:
            column.append('#')
        else:
            column.append(' ')
    next_cells.append(column)

while True:
    print('\n\n')
    current_cells = copy.deepcopy(next_cells)
    for ver in range(height):
        for hor in range(width):
            print(current_cells[hor][ver], end = '')
        print()
    for hor in range(width):
        for ver in range(height):
            left_coord = (hor - 1) % width
            right_coord = (hor + 1) % width
            above_coord = (ver -1) % height
            below_coord = (ver + 1) % height

            num_neighbors = 0
            if current_cells[left_coord][above_coord] == '#':
                num_neighbors += 1
            if current_cells[hor][above_coord] == '#':
                num_neighbors += 1
            if current_cells[right_coord][above_coord] =='#':
                num_neighbors += 1
            if current_cells[left_coord][ver] == '#':
                num_neighbors += 1
            if current_cells[right_coord][ver] == '#':
                num_neighbors += 1
            if current_cells[left_coord][below_coord] == '#':
                num_neighbors += 1
            if current_cells[hor][below_coord] == '#':
                num_neighbors += 1
            if current_cells[right_coord][below_coord] == '#':
                num_neighbors += 1

            if current_cells[hor][ver] == '#' and (num_neighbors in (2,3)):
                next_cells[hor][ver] == '#' #pylint: disable=pointless-statement
            elif current_cells[hor][ver] == ' ' and num_neighbors == 3:
                next_cells[hor][ver] = '#'
            else:
                next_cells[hor][ver] = ' '
        time.sleep(0.1)
