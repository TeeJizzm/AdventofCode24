## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 05

############################
# Imports

import os

import tools.texttolists as tl

from functools import cmp_to_key as ck

############################
# Variables

RULES = []

############################
# Functions

def comp(first, second):
    for rule in RULES:
        #print(rule)
        if (rule[0], rule[1]) == (second, first):
            return 1
    return -1


def isUpdateCorrect(update):

    for idx, first in enumerate(update[:-1], start=1):

        #print(idx, first)
        for second in update[idx:]:
            if comp(first, second) > 0:
                return False
    return True


def checkUpdates(updates):
    goodList = []

    for idx, update in enumerate(updates):

        if isUpdateCorrect(update):
            goodList.append(idx)

    return goodList


def fixOrder(update):
    fixedUpdate = update[:]
    #print(update)
    fixedUpdate.sort(key=ck(comp))

    #print(fixedUpdate)
    return fixedUpdate


def correctUpdates(updates, goodList):
    correctedUpdates = []

    for idx, update in enumerate(updates):
        if idx not in goodList:
            #print(update)

            correctedUpdates.append(fixOrder(update))

    return correctedUpdates


def day05(text):
    print("Day 05 -  Print Queue")
    
    global RULES
    part1, part2 = 0,0
    
    rules, updates = tl.toLines(text, "\n\n")

    RULES = tl.to2dInts(rules, item="|")
    updates = tl.to2dInts(updates)


    goodList = checkUpdates(updates)

    part1 = sum(update[(len(update)//2)] for idx, update in enumerate(updates) if idx in goodList)

    updates2 = correctUpdates(updates, goodList)

    part2 = sum(update[(len(update))//2] for update in updates2)

    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day05/inc" 
    
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

    part1, part2 = day05(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############