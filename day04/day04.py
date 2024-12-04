## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 04

############################
# Imports

import os

import tools.texttolists as tl
import tools.grids as grids

############################
# Variables

WORD = "XMAS"

############################
# Functions

def findXMAS(grid):

    locs = grids.findLocs(grid, "A")

    count = 0

    dirs = [(1,1),(1,-1)] # Diagonals

    for x, y in locs:
        mas = 0
        for dx, dy in dirs:
            #print("".join([grid[x+(dx*i)][y+(dy*i)] for i in range(-1,2)]))
            if "".join([grid[x+(dx*i)][y+(dy*i)] for i in range(-1,2)]) in ("MAS", "SAM"):
                mas += 1

        if mas == 2:
            count += 1

    return count


def day04(text):
    print("Day 04 - Ceres Search")

    padding = len(WORD) -1

    part1, part2 = 0, 0
    grid = grids.padArray([list(line) for line in tl.toLines(text)], padding)

    part1 = grids.findWord(grid, WORD)
    part2 = findXMAS(grid)

    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day04/inc" 
    
    # Change file
    #######
    file = "a.txt"
    file = "ex.txt"
    file = "in.txt"
    #######
    
    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)
    
    # Open file, clean up memory after
    with open(filepath, "r") as file:
        
        text = file.read() # Read data

    part1, part2 = day04(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############