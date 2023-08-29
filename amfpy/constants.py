import math as m
atomnumbertocolor = {
    1: "whitesmoke",
    2: "",
    6: "blue",
    7: "limegreen",
    8: "red"
}


def getAtomColor(number: int):
    if atomnumbertocolor[int(number)]: return atomnumbertocolor[int(number)]
    else: return "firebrick"


def calculateDistance(x1: int,x2: int,y1: int,y2: int):
    return m.sqrt((x2 - x1)**2 + (y2 - y1)**2)
