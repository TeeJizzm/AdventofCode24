# Reads a text input and returns separated values
# Returns a list of lists

###########################

def padArray(grid, padding=2, pad="."):

    cols = padding + len(grid[0]) + padding

    for row in grid:
        for _ in range(padding):
            row.insert(0, pad)
            row.append(pad)

    for _ in range(padding):
        grid.insert(0, [pad]*cols)
        grid.append([pad]*cols)

    return grid

def findLocs(grid, target):

    locations = []

    for x, row in enumerate(grid):
        for y, v in enumerate(row):
            if v == target:
                locations.append((x,y))
                #print(target, end="")
            else:
                #print(v, end="")
                #print(".", end="")
                continue
        #print()

    return locations

def findWord(grid, word):

    locs = findLocs(grid, word[0])

    count = 0

    dirs = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)] # Clockwise directions

    for x, y in locs:
        for dx, dy in dirs:
            if "".join([grid[x+(dx*i)][y+(dy*i)] for i in range(len(word))]) == word:
                count += 1

    return count

########## EOF ############
