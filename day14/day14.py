## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 14

############################
# Imports

import os

import tools.texttolists as tl
import re

from math import prod

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

import time

############################
# Variables

W = 11
W = 101

H = 7
H = 103

############################
# Functions

def moveRobot(robot, secs):

    x_s, y_s, dx, dy = int(robot[0]), int(robot[1]), int(robot[2]), int(robot[3])

    x = (x_s + (dx * secs)) % W
    y = (y_s + (dy * secs)) % H

    if x < 0:
        x = W + x
    if y < 0:
        y = H + y

    return x, y

def quadrantScore(positions):

    midh = H // 2
    midw = W // 2

    quad = [0, 0, 0, 0]

    for row in positions[:midh]:
        for col in row[:midw]:
            #print(col, end="")
            quad[0] += col
        #print(" ", end="")
        for col in row[midw+1:]:
            #print(col, end="")
            quad[1] += col
        #print()
    #print()
    for row in positions[midh+1:]:
        for col in row[:midw]:
            #print(col, end="")
            quad[2] += col
        #print(" ", end="")
        for col in row[midw+1:]:
            #print(col, end="")
            quad[3] += col
        #print()

    return quad

def getQuadrantScore(robots):

    positions = [[0 for _ in range(W)] for _ in range(H)]

    for r in robots:
        x, y = moveRobot(r, 100)
        positions[y][x] += 1

    score = quadrantScore(positions)
    
    
    fig, ax = plt.subplots()


    i = 8168 #found the christmas tree

    positions = [[0 for _ in range(W)] for _ in range(H)]
    for r in robots:
        x, y = moveRobot(r, i)
        positions[y][x] += 1

    p2 = i

    ax.clear()
    
    ax.set_title(f"Iteration: {i}")

    im = ax.imshow(positions, cmap='viridis', interpolation='none')

    plt.pause(1)


    plt.show()
    return prod(score), i

def day14(text):
    print("Day 14 - Restroom Redoubt")
    
    part1, part2 = 0, 0
    
    robots = [re.findall(r'-?[0-9]+', robot) for robot in tl.toLines(text)]

    part1, part2 = getQuadrantScore(robots)

    
    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day14/inc" 
    
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

    part1, part2 = day14(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############