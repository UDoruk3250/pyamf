from .constants import *
from .amfreader import Reader
from .Builder2D import Drawer
from math import sqrt, atan2, cos, sin

bondLength = []

CorruptedFileError = Exception("The *.amf file has been corrupted or formatted wrong. Check the file again.")



class Atom:
    def __init__(self, thelist):  # TODO: add atom number as well.
        self.id = thelist[1]
        self.atomnumber = thelist[2]
        self.x = thelist[3]
        self.y = thelist[4]


def animate2D(f: int):
    drawer = Drawer()
    atomlists, bondlists = Reader.getLists()
    if len(atomlists) != len(bondlists):
        raise CorruptedFileError
    for atomlist, bondlist in zip(atomlists, bondlists):
        for i in range(f // (60 * len(atomlist))):
            for bond in bondlist:
                atom1 = Atom(atomlist[int(bond[3]) - 1])
                atom2 = Atom(atomlist[int(bond[4]) - 1])
                distance = calculateDistance(atom1.x, atom2.x, atom1.y, atom2.y)
                extra = OPTIMUM_DISTANCE - distance
                change = (extra / abs(extra)) * sqrt(abs(extra))
                angle = atan2(atom2.y - atom1.y, atom2.x - atom1.x)
                incrementX = change * cos(angle)
                incrementY = change * sin(angle)
                self.drawer.clear()
                Drawer.buildFromLists()
    # print("Step " + str(i))
