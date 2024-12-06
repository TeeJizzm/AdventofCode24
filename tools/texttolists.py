# Reads a text input and returns separated values
# Returns a list of lists

###########################

def toGrid(text):

    return [list(line) for line in toLines(text, "\n")]


def to2dArray(text, group="\n", sep=","):

    # Split text into groups, split groups into items
    lists = [line.split(str(sep)) for line in toLines(text, group)]
        
    # return list of lists
    return lists

def to2dInts(text, group="\n", item=","):

    ints = [[int(x) for x in line.split(item)] for line in toLines(text, group)]

    # Return 2d list of ints
    return ints

def toLines(text, group="\n"):
    
    return text.split(str(group))
        
def toTupleList(text, group="\n", item=","):

    tups = [tuple(group.split(str(item))) for group in text.split(str(group))]

    # return list of tuples
    return tups

########### EOF ############