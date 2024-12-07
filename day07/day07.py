## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 07

############################
# Imports

import os

import tools.texttolists as tl

from itertools import product

############################
# Variables

signsTwo = [
    "p", # plus
    "t", # times
    "c"  # concatenation
]

signsOne = [
    "p", # plus
    "t"  # times
]

############################
# Functions

def calc(a, b, s):

    if s == "p":
        return int(a) + int(b)
    elif s == "m":
        return int(a) - int(b)
    elif s == "t":
        return int(a) * int(b)
    elif s == "d":
        return int(a) / int(b)
    elif s == "c":
        return (str(a) + str(b))
    else:
        return 0

def reduceEq(nums, ops):

    for i in range(len(ops)):
        #print(nums[0], ops[i], nums[1])
        a = nums.pop(0)
        nums[0] = calc(a, nums[0], ops[i])

    #print("end:", nums, ops)
    return int(nums[0])


def findAnswer(nums, total, signs=signsOne):

    #print(total, nums)
    for ops in product(signs, repeat=len(nums)-1):    
        if reduceEq(nums[:], ops[:]) == int(total):
            #print("correct:", nums, ops)
            return int(total)
        
    return 0

def answers(equations):
    ansOne, ansTwo = 0, 0

    for equation in equations:

        total, nums = tl.toLines(equation, ": ")
        nums = tl.toLines(nums, " ")

        ansOne += findAnswer(nums,total)
        ansTwo += findAnswer(nums, total, signsTwo)
        

    return ansOne, ansTwo


def day07(text):
    print("Day 07 - Bridge Repair")
    
    part1, part2 = 0,0
    
    equations = tl.toLines(text)

    part1, part2 = answers(equations)
    
    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day07/inc" 
    
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

    part1, part2 = day07(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############