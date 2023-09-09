import matplotlib.pyplot as plt
from .constants import *


class Drawer:
    def __init__(self):
        plt.ion()

    def clear(self):
        plt.clf()
        plt.axes().set_facecolor("black")

    def plotAtom(self, x: float, y: float, atomnumber: int):
        plt.plot(x, y, marker="o", color=getAtomColor(atomnumber), zorder=2)

    def plotBond(self, xlist: list, ylist: list):
        plt.plot(xlist, ylist, color="dimgrey", linewidth=2, zorder=1)

    @staticmethod
    def buildFromLists(atomlist, bondlist):
        for atom in atomlist:
            Drawer.plotAtom(Drawer(), float(atom[3]), float(atom[4]), int(atom[2]))
        for bond in bondlist:
            Drawer.plotBond(Drawer(),
                            [float(atomlist[int(bond[3]) - 1][3]), float(atomlist[int(bond[4]) - 1][3])],
                            [float(atomlist[int(bond[3]) - 1][4]), float(atomlist[int(bond[4]) - 1][4])])
        Drawer.plotAll(block=False)

    @staticmethod
    def plotAll(block: bool):
        plt.show(block=block)
