## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 12

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
DIAG = [
    (1,1),   # SE
    (1,-1),  # NE
    (-1,1),  # SW
    (-1,-1)  # NW
]

############################
# Functions

def dfs(grid, label, row, col, group, visited):

    if visited[row][col] or grid[row][col] != label:
        return
    
    group.append((row, col))
    visited[row][col] = True

    for dr, dc in DIRS:

        if grid[row+dr][col+dc] == label:

            if (row+dr, col+dc) not in group:

                group = dfs(grid, label, row+dr, col+dc, group, visited)

    return group


def findGroups(grid, labels):

    groups = []
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    for label in labels:
        group = []

        label_locs = grids.findLocs(grid, label)

        for row, col in label_locs:
            
            if (row, col) not in visited:
                group = dfs(grid, label, row, col, [], visited)
            
            if group:
                groups.append(group)

    return groups

def calcPerim(group):
    
    perim = 0
    corners = 0

    for x, y in group:
        perim += 4
        for dy, dx in DIRS:
            if (x+dx, y+dy) in group:
                perim -= 1


    return perim, corners

def answers(groups):

    total1 = 0
    total2 = 0

    for group in groups:
        area = len(group)
        perimeter, corners = calcPerim(group)

        total1 += area * perimeter
        total2 += area * corners

    return total1, total2

def day12(text):
    print("Day 12 - Garden Groups")
    
    part1, part2 = 0, 0
    
    grid = grids.padArray(tl.toGrid(text),1)
    
    labels = set("".join(text.split()))

    groups = findGroups(grid, labels)

    part1, part2 = answers(groups)


    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day12/inc" 
    
    # Change file
    #######
    file = "ex.txt"
    #file = "in.txt"
    #######
    
    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)
    
    # Open file, clean up memory after
    with open(filepath, "r") as file:
        
        text = file.read() # Read data

    part1, part2 = day12(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############