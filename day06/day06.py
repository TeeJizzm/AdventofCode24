## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 06

############################
# Imports

import os

import tools.texttolists as tl
import tools.grids as grids

from itertools import cycle
from copy import deepcopy as dc

############################
# Variables

dirs = {
    "^":(-1,0), 
    ">":(0,1), 
    "v":(1,0), 
    "<":(0,-1)
    } # 90 degree right turns

dirCycle = cycle(dirs.keys())

############################
# Functions

def changeDir(current):

    for key in dirCycle:
        if key == current:
            break
    return next(dirCycle)

def getNext(x, y, dir):
    dx, dy = dirs[dir]
    return x+dx, y+dy

def createPath(grid, start, dir):
    visited = []

    inbounds = True

    x,y = start

    while inbounds == True:   

        x_n,y_n = getNext(x, y, dir)

        next_square = grid[x_n][y_n]

        #print((x,y), dir, next_square)

        if next_square == "~":
            visited.append((x,y))
            inbounds = False
        elif next_square == "#":
            dir = changeDir(dir)
        else: # next_square == "." or in dirs
            visited.append((x,y))
            x, y = x_n, y_n

    return visited

def findLoop(grid, start, dir):
    #visited = []
    #directions = []

    rcd = []

    inbounds = True

    x,y = start

    while inbounds == True:       

        x_n,y_n = getNext(x, y, dir)

        if len(rcd) > 20000:
            return True

        if (x_n,y_n, dir) in set(rcd):
            print("Visited before:",x,y,dir)
            return True

        #if (x_n,y_n) in set(visited):
            #for i in range(len([idx for idx, visit in enumerate(visited) if visit == (x,y) and directions[idx] == dir])):
                #print(set(visited))
                #if visited[i] == (x,y) and directions[i] == dir:
                
                    #print(f"Visited {x_n},{y_n} while facing {dir} before.")
                    #return True

        next_square = grid[x_n][y_n]

        #print((x,y), dir, next_square)

        if next_square == "~":
            #visited.append((x,y))
            #directions.append(dir)
            return False
        elif next_square == "#":
            dir = changeDir(dir)
            #visited.append((x,y))
            #directions.append(dir)
            rcd.append((x,y,dir))
        else: # next_square == "." or in dirs
            
            x, y = x_n, y_n
            
            #visited.append((x,y))
            #directions.append(dir)
            rcd.append((x,y,dir))

        #print(visited[-1], directions[-1])


    return False

def partTwo(grid, start, dir):

    loopCount = 0

    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            test_grid = dc(grid)
            
            if grid[x][y] == ".":
                
                test_grid[x][y] = "#"
                #print(f"Testing location: ({x},{y})")
                print("Testing location:",x,y)

                if findLoop(test_grid, start, dir):
                    loopCount += 1

    return loopCount

def day06(text):
    print("Day 06 - Guard Gallivant")
    
    part1, part2 = 0,0

    grid = grids.padArray(tl.toGrid(text), padding=1, pad="~")
    #print(grid)

    start = grids.findLocs(grid, "^")

    #print(start)

    orig_path = createPath(grid, start[0], "^")
    
    part1 = len(set(orig_path))
    print(part1)

    part2 = partTwo(grid,start[0], "^")

    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day06/inc" 
    
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

    part1, part2 = day06(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############