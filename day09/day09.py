## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 09

############################
# Imports

import os

import tools.texttolists as tl

############################
# Variables



############################
# Functions

def constructData(entries):
    data = []
    
    x = 0

    for idx, num in enumerate(entries):

        if idx % 2 == 0:
            data += [x]* int(num)
            x += 1
            #print(data)
        else:
            data += ["."]* int(num)
            #print(data)

    return data

def reorgData(data):

    for idx in range(len(data) - 1, -1, -1):
        if data[idx] != ".":
            jdx = data.index(".")
            if jdx > idx:
                break
            data[jdx] = data[idx]
            data[idx] = "."

        #print(data)

    return data

def reorgFiles(data, entries):

    lengths = [num for idx, num in enumerate(entries) if idx % 2 == 0]

    v = len(lengths)-1
    width = int(lengths[v])

    for idx in range(len(data) - 1, -1, -1):
        #print(val)   
        if data[idx] not in [".", "*"]:
            if int(data[idx]) == v:
                
                #print(idx, v)
                for jdx in range(len(data)-1):
                    if jdx > idx: break
                    if data[jdx:jdx+width] == ["."] * width:
                        data[jdx:jdx+width] = [v]*width
                        data[idx-width+1:idx+1] = ["."] * width
                        #print(jdx, ["."]*int(lengths[v]))
                        break

                #print(data[idx], lengths[v])
                v -= 1 
                width = int(lengths[v])   
        #print(data)

    return data


def getCheckSum(data):

    return sum([idx * int(val) for idx, val in enumerate(data) if val != "."])

def day09(text):
    print("Day 09 - Disk Fragmenter")
    
    part1, part2 = 0, 0
    
    entries = list(text)
    #print(entries)
    dataLine = constructData(entries)

    #print(dataLine)

    defragmented = reorgData(dataLine[:])
    sortedFiles = reorgFiles(dataLine[:], entries)

    part1 = getCheckSum(defragmented)
    part2 = getCheckSum(sortedFiles)

    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day09/inc" 
    
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

    part1, part2 = day09(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############