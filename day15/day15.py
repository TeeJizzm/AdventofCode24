## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 15

############################
# Imports

import os

import tools.texttolists as tl
import tools.grids as gr

import re

############################
# Variables

dirs = {
    "^":(-1,0), 
    ">":(0,1), 
    "v":(1,0), 
    "<":(0,-1)
    }

W = 0
W2 = 0
H = 0

############################
# Functions

def getNext(r, c, dir, i=1):
    dr, dc = dirs[dir]
    return r+(dr*i), c+(dc*i)

def blocked(grid, loc, dir):

    nr, nc = getNext(loc[0], loc[1], dir)

    if grid[nr][nc] == "#":
        return True
    elif grid[nr][nc] == ".":
        return False

    if dir == "^" or dir == "v":
        if grid[nr][nc] == "[":
            a = blocked(grid, (nr, nc), dir) 
            b = blocked(grid, (nr, nc+1), dir)
            return a or b
        if grid[nr][nc] == "]":
            a = blocked(grid, (nr, nc), dir) 
            b = blocked(grid, (nr, nc-1), dir)
            return a or b
    else:
        return blocked(grid, (nr, nc), dir)
    

def moveRobot(grid, loc, dir):

    r1, c1 = loc

    for i in range(1, max(W, H)):
        r, c = getNext(loc[0], loc[1], dir, i)
        if 0 > r > H or 0 > c > W:
            break
        elif grid[r][c] == "#":
            break
        elif grid[r][c] == ".":
            if i > 1:
                grid[r][c] = "O"
            
            r1, c1 = getNext(loc[0], loc[1], dir)
            grid[r1][c1] = "@"
            grid[loc[0]][loc[1]] = "."
            break

    return r1, c1


def moveRobot2(grid, loc, dir):

    r1, c1 = loc

    if dir == "<" or dir == ">":
        for i in range(1, max(W, H)):
            r, c = getNext(loc[0], loc[1], dir, i)
            if 0 > r > H or 0 > c > W:
                break
            elif grid[r][c] == "#":
                break
            elif grid[r][c] == ".":
                if i > 1:
                    grid[r][c] = "["
                
                r1, c1 = getNext(loc[0], loc[1], dir)
                grid[r1][c1] = "@"
                grid[loc[0]][loc[1]] = "."
                break

    return r1, c1

def followInstructions(grid, instructions, start):

    location = start

    for instruction in instructions:
        location = moveRobot(grid, location, instruction)

def followWide(grid, instructions, start):

    location = start

    for instruction in instructions:
        continue


def wideGrid(grid):

    newgrid = []

    for row in grid:
        newrow = []
        for val in row:
            if val == "#":
                newrow.append("#")
                newrow.append("#")
            elif val == ".":
                newrow.append(".")
                newrow.append(".")
            elif val == "O":
                newrow.append("[")
                newrow.append("]")
            elif val == "@":
                newrow.append("@")
                newrow.append(".")
        newgrid.append(newrow)
    return newgrid


def calcGPS(grid, box="O"):
    boxes = gr.findLocs(grid, box)
    gps = 0

    for br, bc in boxes:
        gps += (100 * br) + bc

    return gps

def day15(text):
    print("Day 15 - Warehouse Woes")
    
    part1, part2 = 0, 0
    
    grid, instructions = tl.toLines(text, "\n\n")

    grid = tl.toGrid(grid)

    global W
    W = len(grid)
    global H
    H = len(grid[0])
    global W2
    W2 = W * 2

    grid2 = wideGrid(grid)
    
    for r in grid2:
        print(*r)

    robot = gr.findLocs(grid, "@")[0]
    r2 = gr.findLocs(grid, "@")[0]

    instructions = re.findall(f"\^|>|v|<", instructions)
    
    followInstructions(grid, instructions, robot)


    part1 = calcGPS(grid)
    part2 = calcGPS(grid2, "[")

    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day15/inc" 
    
    # Change file
    #######
    file = "ex.txt"
    file = "ex1.txt"
    file = "ex2.txt"
    #file = "in.txt"
    #######
    
    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)
    
    # Open file, clean up memory after
    with open(filepath, "r") as file:
        
        text = file.read() # Read data

    part1, part2 = day15(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############