## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 03

############################
# Imports

import os

import tools.texttolists as tl

import re

############################
# Variables



############################
# Functions

def day03(text):

    print("Day 03 - Mull it Over")
    
    part1, part2 = 0,0
    
    muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", text)

    instructions = re.findall(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", text)

    print(instructions)


    do = True
    for inst in instructions:
        if re.search(r"mul", inst) and do: 
            x, y = re.findall(r"\d{1,3}",inst)

            part2 += int(x) * int(y)
        elif re.search(r"don't", inst):
            do = False
        elif re.search(r"do\(\)", inst):
            do = True

    for mul in muls:
        x, y = re.findall(r"\d{1,3}",mul)

        part1 += int(x) * int(y)
    
    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day03/inc" 
    
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

    part1, part2 = day03(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############