def makeset(arg):
    return(">>> Set X = {"+", ".join(str(list(dict.fromkeys(arg))).translate(str.maketrans(dict.fromkeys(",'[] "))))+"}")
