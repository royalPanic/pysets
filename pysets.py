# pysets v0.5

# this function takes an array or string and returns it as a human readable set
def makeset(arg):
    return(">>> Set X = {"+", ".join(str(list(dict.fromkeys(arg))).translate(str.maketrans(dict.fromkeys(",'[] "))))+"}")

# this function takes an array and returns an array that follows set rules
def makesetArray(arg):
    if type(arg) is list:
        return(list(dict.fromkeys(arg)))
    else:
        raise TypeError("This function can only take an array.")
