## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 08

############################
# Imports

import os

import tools.texttolists as tl
import tools.grids as grids

from itertools import combinations

############################
# Variables



############################
# Functions

def iterations(n):
    if n == 1:
        yield 1
    else:
        for i in range(n):
            yield i

def getAntinodes(a, b, grid, n):
    antinodes = []

    a_row, a_col = a
    b_row, b_col = b

    d_col = a_col - b_col
    d_row = a_row - b_row

    for i in iterations(n):
        if 0 <= (a_col + (i*d_col)) < len(grid) and 0 <= (a_row + (i*d_row)) < len(grid):
            antinodes.append((a_col+(i*d_col), a_row+(i*d_row)))
        if 0 <= (b_col - (i*d_col)) < len(grid) and 0 <= (b_row - (i*d_row)) < len(grid):
            antinodes.append((b_col-(i*d_col), b_row-(i*d_row)))

    #print("Found nodes: ", antinodes)
    return antinodes

def getUniqueAntinodes(grid, freqs, n=1):
    nodes = []

    for freq in freqs:
        #print(freq)
        signals = grids.findLocs(grid, str(freq))

        for pair in combinations(signals, 2):
            #print(freq, pair)
            nodes += getAntinodes(pair[0], pair[1], grid, n)

        #print(signals)

    return len(set(nodes))

def day08(text):
    print("Day 08 - Resonant Collinearity")
    
    part1, part2 = 0, 0
    
    grid = tl.toGrid(text)

    #print(grid)

    freqs = list(set([a for row in grid for a in row]))
    freqs.remove(".")

    #print(grid)

    part1 += getUniqueAntinodes(grid, freqs)
    part2 += getUniqueAntinodes(grid, freqs, n=50)

    #print(freqs)

    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day08/inc" 
    
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

    part1, part2 = day08(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############