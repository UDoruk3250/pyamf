atomnumbertocolor = {
    1: "whitesmoke",
    2: "",
    6: "blue",
    7: "limegreen",
    8: "red"
}


def getAtomColor(number: int):
    if atomnumbertocolor[int(number)]: return atomnumbertocolor[int(number)]
    else: return ""
