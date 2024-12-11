## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 10

############################
# Imports

import os

import tools.texttolists as tl
import tools.grids as grids

############################
# Variables

DIRS = [
    (0, 1),  # E
    (1, 0),  # S
    (0, -1), # W
    (-1, 0)  # N
]

############################
# Functions

def navigate(grid, loc, val):

    nines = []

    row, col = loc

    for dr, dc in DIRS:
        l = grid[row+dr][col+dc]

        if l.isdigit() == True:
            if int(l) == val+1 != 9:
                nines += navigate(grid, (row+dr, col+dc), val+1)
            elif int(l) == val+1 == 9:
                nines += [(row+dr, col+dc)]
                #print(nines)

    return nines

def findTrails(grid):

    count, count2 = 0, 0
    zeroes = grids.findLocs(grid[:], "0")

    #print(zeroes)

    for zero in zeroes:

        nines = navigate(grid, zero, 0)
        count += len(set(nines))
        count2 += len(nines)
        #print(nines)

    return count, count2

def day10(text):
    print("Day 10 - Hoof It")
    
    part1, part2 = 0, 0
    
    grid = grids.padArray(tl.toGrid(text), 1)

    part1, part2 = findTrails(grid)


    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day10/inc" 
    
    # Change file
    #######
    file = "ex.txt"
    file = "in.txt"
    #######
    
    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)
    
    # Open file, clean up memory after
    with open(filepath, "r") as file:
        
        text = file.read() # Read data

    part1, part2 = day10(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############