## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 13

############################
# Imports

import os

import tools.texttolists as tl

import numpy as np
import re

############################
# Variables



############################
# Functions

def cramer(machine, offset = 0):

    A, B = 0, 0

    ax, ay, bx, by, px, py = re.findall(r"\d+", machine)

    px = int(px) + offset
    py = int(py) + offset

    print(f"Testing: {ax}x + {ay}y = {px}; {bx}x + {by}y = {py}")

    d = (int(ax)*int(by))-(int(ay)*int(bx))
    d_a = (px*int(by))-(py*int(bx))
    d_b = (int(ax)*py)-(int(ay)*px)

    if d_a % d == 0 and d_b % d == 0:
        A = int(d_a / d)
        B = int(d_b / d)
    
    return A, B

def findEq(machine):

    ax, ay, bx, by, px, py = re.findall(r"\d+", machine)

    #print(f"Testing: {ax}x + {ay}y = {px}; {bx}x + {by}y = {py}")

    ab = np.array([[int(ax), int(bx)], [int(ay), int(by)]])
    xy = np.array([int(px), int(py)])

    a, b = np.linalg.solve(ab, xy)

    #print("a:", a, "b:", b)

    if 0 < a > 100 or 0 < b > 100:
        a = 0
        b = 0

    elif abs(a - np.round(a) > 1e-3) or abs(b - np.round(b) > 1e-3):
        a = 0
        b = 0

    #print("a-", np.round(a), "b-", np.round(b))

    return int(np.round(a)), int(np.round((b)))


def day13(text):
    print("Day 13 - Claw Contraption")
    
    part1, part2 = 0, 0
    
    machines = tl.toLines(text, "\n\n")


    for machine in machines:
        #a, b = findEq(machine)
        a, b = cramer(machine)
        part1 += ((3*a) + b)
        a, b = cramer(machine, offset=10000000000000)
        part2 += ((3*a) + b)

    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day13/inc" 
    
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

    part1, part2 = day13(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############