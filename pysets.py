#this function takes a string and outputs a set in correct mathematical set notation, ex: Set A = {1, 2, 3}
def stringtoset(tac):
    firstlist = list(str(tac))
    finallist = list(dict.fromkeys(firstlist))
    standard = str.maketrans(dict.fromkeys("'[]"))
    bold = str(finallist).translate(standard)
    setNotation = ">>> Set X = {"+bold+"}"
    return(setNotation)

#this function returns only the part in brackets
def stringtobold(tac):
    firstlist = list(str(tac))
    finallist = list(dict.fromkeys(firstlist))
    standard = str.maketrans(dict.fromkeys("'[]"))
    bold = str(finallist).translate(standard)
    return(">>> {"+bold+"}")

#this function takes a python array and returns a set in complete set notation
def arraytoset(arr):
    finallist = list(dict.fromkeys(arr))
    standard = str.maketrans(dict.fromkeys(",'[] "))
    bold = str(finallist).translate(standard)
    arc = ", "
    primobold = arc.join(bold)
    setNotation = ">>> Set X = {"+primobold+"}"
    return(setNotation)
