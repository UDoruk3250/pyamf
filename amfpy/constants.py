import math as m

atomnumbertocolor = {
    1: "whitesmoke",
    2: "",
    6: "blue",
    7: "limegreen",
    8: "red"
}

OPTIMUM_DISTANCE = 5


def getAtomColor(number: int):
    if atomnumbertocolor[int(number)]:
        return atomnumbertocolor[int(number)]
    else:
        return "firebrick"


def calculateDistance(x1: float, x2: float, y1: float, y2: float):
    return m.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
