from .constants import *
from .amfreader import Reader
from .Builder2D import Drawer
from math import sqrt, atan2, cos, sin,pi

bondLength = []

CorruptedFileError = Exception("The *.amf file has been corrupted or formatted wrong. Check the file again.")


class Atom:
    def __init__(self, thelist):  # TODO: add atom number as well.
        self.id = float(thelist[1])
        self.atomnumber = float(thelist[2])
        self.x = float(thelist[3])
        self.y = float(thelist[4])


def animate2D(f: int):
    drawer = Drawer()
    atomlists, bondlists = Reader.getLists()
    if len(atomlists) != len(bondlists):
        raise CorruptedFileError
    for atomlist, bondlist in zip(atomlists, bondlists):
        for i in range(f // (60 * len(atomlists))):
            for bond in bondlist:
                atom1 = Atom(atomlist[int(bond[3]) - 1])
                atom2 = Atom(atomlist[int(bond[4]) - 1])
                distance = calculateDistance(atom1.x, atom2.x, atom1.y, atom2.y)
                extra = OPTIMUM_DISTANCE - distance
                change = extra/2
                # (extra / abs(extra)) * sqrt(abs(extra))
                angle = atan2(atom2.y - atom1.y, atom2.x - atom1.x) * 180/pi
                increment_x = change * cos(angle)
                increment_y = change * sin(angle)
                atomlist[int(bond[3]) - 1][3:] = [atom1.x + increment_x, atom1.y + increment_y]
                atomlist[int(bond[4]) - 1][3:] = [atom2.x - increment_x, atom2.y - increment_y]

                drawer.clear()
                drawer.buildFromLists(atomlist, bondlist)

