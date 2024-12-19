## ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## ##

## Day 17

############################
# Imports

import os

import tools.texttolists as tl
import re

############################
# Variables

global A
global B
global C

A = 0
B = 0
C = 0

global p2
p2 = []


combo_operands = {
    0 : lambda: 0,
    1 : lambda: 1,
    2 : lambda: 2,
    3 : lambda: 3,
    4 : lambda: A,
    5 : lambda: B,
    6 : lambda: C,
    7 : lambda: None
}

def get_combo(operand):
    return combo_operands.get(operand, lambda: "Invalid")()


############################
# Functions

def div(operand):
    
    return int(A) // pow(2, get_combo(operand))

def adv(operand): # Opcode 0, Combo Operand

    global A
    A = int(div(operand))
    return -1

def bxl(operand): # Opcode 1, Literal Operand

    global B
    res = int(int(B) ^ int(operand))
    B = res
    return -1

def bst(operand): # Opcode 2, Combo Operand

    global B
    B = int(get_combo(operand) % 8)

    return -1

def jnz(operand): # Opcode 3, Literal Operand
    
    if int(A) == 0:
        return -1
    else:
        return operand # Return literal value as new index

def bxc(operand): # Opcode 4, Literal Operand

    # Bitwise XOR of Register B and Register C
    # Operand is read but not used.
    global B
    res = int(B) ^ int(C)
    B = int(res)

    return -1

def out(operand): # Opcode 5, Combo Operand
    # Prints output of combo operand mod 8
    combo = get_combo(operand)
    #print(combo, combo % 8)
    #print(combo % 8, sep=",", end=",")

    global p2
    p2.append(combo % 8)

    return -1

def bdv(operand): # Opcode 6, Combo Operand

    global B
    B = int(div(operand))
    return -1

def cdv(operand): # Opcode 7, Combo Operand

    global C
    C = int(div(operand))
    return -1

opcodes = { # Translates opcode to instruction
        0 : adv,
        1 : bxl,
        2 : bst,
        3 : jnz,
        4 : bxc,
        5 : out,
        6 : bdv,
        7 : cdv
    }

def program(instructions):
    
    pointer = 0

    while pointer < len(instructions):

        func = opcodes[int(instructions[pointer])]

        #print(A, B, C)
        #print(pointer, func, instructions[pointer+1])

        res = func(int(instructions[pointer+1]))

        if res < 0:
            pointer += 2
        else:
            pointer = res


    return 0


def day17(text):
    print("Day 17 - Chronospatial Computer")

    part1, part2 = 0, 0
    
    global A, B, C
    global p2

    reg, ins = tl.toLines(text, "\n\n")

    # Initialize registers
    A, B, C = re.findall(r"[0-9]+", reg)
    A = int(A)
    B = int(B)
    C = int(C)

    # Get opcodes and operands
    instructions = re.findall(r"[0-9]+", ins)

    print(instructions)

    program(instructions)

    i = 370000000000000

    while i:

        p2 = []
        A = i
        program(instructions)

        print(i)
        print(p2)

        if instructions == p2:
            print("FOUND IT", A)
            break

        i += 10000


    #for i in range(8):
        #print(get_combo(i))

    return part1, part2

############################
# Run main

if __name__ == "__main__":
    day = "day17/inc" 
    
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

    part1, part2 = day17(text)

    print("Part 1: ", part1)
    print("Part 2: ", part2)
    
########### EOF ############