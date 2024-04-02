from .constants import *
from .amfreader import Reader
from .Builder2D import Drawer
from sympy import sin, cos, pi, atan

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
                if atom2.x - atom1.x != 0:
                    slope = (atom2.y - atom1.y)/(atom2.x - atom1.x)
                    degree = atan(slope) * 180 / pi
                else:
                    degree = pi/2
                distance = calculateDistance(atom1.x, atom2.x, atom1.y, atom2.y)
                extra = distance - OPTIMUM_DISTANCE

                print("Atom " + str(int(atom1.id)) + " X:", atom1.x, ", Y:", atom1.y)
                print("Atom " + str(int(atom2.id)) + " X:", atom2.x, ", Y:", atom2.y)
                print("Distance: " + str(distance))
                print("Degree: " + str(degree))
                print("Extra: " + str(extra))

                x_inc = extra * cos(degree)
                y_inc = extra * sin(degree)

                # (extra / abs(extra)) * sqrt(abs(extra))

                # angle = atan2(atom2.y - atom1.y, atom2.x - atom1.x) * 180/pi
                # increment_x = change * cos(angle)
                # increment_y = change * sin(angle)
                atomlist[int(bond[4]) - 1][3:] = [atom2.x + x_inc, atom2.y + y_inc]

                drawer.clear()
                drawer.buildFromLists(atomlist, bondlist)

