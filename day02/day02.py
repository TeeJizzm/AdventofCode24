## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 02

############################
# Imports

import os

import tools.texttolists as tl

import numpy as np

from itertools import pairwise as pw

############################
# Variables



############################
# Functions

def isSafe(x, y) -> bool:

    #print("Current:", curr, "Testing:", test)
    if x == 0:
        return False
    elif x < -3 or x > 3:
        return False
    elif x * y < 0:
        return False
    
    return True
        
def checkReport(report) -> bool:

    diffs = np.diff(report[:])

    if not isSafe(diffs[0], diffs[0]):
        return False
    
    for idx, curr in enumerate(diffs[:-1], start=1):
        next = diffs[idx]
        if not isSafe(next, curr):
            return False
            
    return True

def checkReportBadLevel(report) -> bool:

    if checkReport(report):
        return True
    else:
        for i in range(len(report)):
            rep = report[:]
            del rep[i]
            if checkReport(rep):
                return True

    return False


def day02(text):
    print("Day 02 - Red-Nosed Reports")
    
    part1, part2 = 0, 0
    
    # Parsing

    reports = tl.to2dInts(text,"\n"," ")
    #print(reports)

    part1 = sum([int(checkReport(report)) for report in reports])
    part2 = sum([int(checkReportBadLevel(report)) for report in reports])

    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day02/inc" 
    
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

    part1, part2 = day02(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############