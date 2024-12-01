## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 01

############################
# Imports

import os

import tools.texttolists as tl

############################
# Variables



############################
# Functions

def day01(text):
    print("Day 01 - Historian Hysteria")
    
    part1, part2 = 0, 0
    
    pairs = tl.toTupleList(text,"\n","   ")
    lists = tl.to2dArray(text,"\n","   ")

    list_l = sorted([i[0] for i in pairs])
    list_r = sorted([i[1] for i in pairs])

    for i in range(len(pairs)):
        diff = abs(int(list_l[i]) - int(list_r[i]))
        part1 += diff

    for num in set(list_l):
        cr = list_r.count(num)
        cl = list_l.count(num)

        part2 += cr * cl * int(num)

    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day01/inc" 
    
    # Change file
    #######
    #file = "ex.txt"
    file = "in.txt"
    #######
    
    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)
    
    # Open file, clean up memory after
    with open(filepath, "r") as file:
        
        text = file.read() # Read data

    part1, part2 = day01(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############