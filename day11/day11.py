## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 11

############################
# Imports

import os

import tools.texttolists as tl

from collections import defaultdict as ddict

############################
# Variables



############################
# Functions

def processStone(stones):
    
    output = ddict(int)

    for stone, quantity in stones.items():

        if stone == 0:
            output[1] += quantity
        elif len(str(stone)) % 2 == 0:
            output[int(str(stone)[:len(str(stone))//2])] += quantity
            output[int(str(stone)[len(str(stone))//2:])] += quantity
        else:
            output[stone * 2024] += quantity


    return output


def calcBlinks(stones, n):

    for i in range(n):
        stones = processStone(stones)
        print(i, stones)

    return sum(stones.values())


def day11(text):
    print("Day 11 - Plutonian Pebbles")
    
    part1, part2 = 0, 0
    
    initial = [int(x) for x in text.split(" ")]

    print(initial)

    dictionary = ddict(int)

    for i in range(len(initial)):
        dictionary[initial[i]] = 1

    part1 = calcBlinks(dictionary, 25)
    #part2 = calcBlinks(dictionary, 75)

    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day11/inc" 
    
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

    part1, part2 = day11(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############