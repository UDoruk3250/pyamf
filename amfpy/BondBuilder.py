import math as m
from .Builder2D import *


class BondBuilder:
    def __init__(self):
        self.drawer = Drawer()

    def singleBond(self, atomList: list, bondList: list):
        self.drawer.plotBond(
           [float(atomList[int(bondList[-1][3]) - 1][3]), float(atomList[int(bondList[-1][4]) - 1][3])],
           [float(atomList[int(bondList[-1][3]) - 1][4]), float(atomList[int(bondList[-1][4]) - 1][4])])

    def doubleBond(self, atomList: list, bondList: list):
        result = m.atan(
            ((float(atomList[int(bondList[-1][4]) - 1][3])) - (float(atomList[int(bondList[-1][3]) - 1][3]))) / (
                    (float(atomList[int(bondList[-1][4]) - 1][4])) - (float(atomList[int(bondList[-1][3]) - 1][4]))))
        # print(result)
        distance = 0.1
        self.drawer.plotBond([float(atomList[int(bondList[-1][3]) - 1][3]) + (distance * m.cos(result)),
                              float(atomList[int(bondList[-1][4]) - 1][3]) + (distance * m.cos(result))],
                             [float(atomList[int(bondList[-1][3]) - 1][4]) + (distance * m.sin(result + (45 * m.pi))),
                              float(atomList[int(bondList[-1][4]) - 1][4]) + (distance * m.sin(result + (45 * m.pi)))])

        # plt.plot([float(atomList[int(bondList[-1][3]) - 1][3]) + (distance * m.cos(result)),
        #           float(atomList[int(bondList[-1][4]) - 1][3]) + (distance * m.cos(result))],
        #          [float(atomList[int(bondList[-1][3]) - 1][4]) + (distance * m.sin(result + (45 * m.pi))),
        #           float(atomList[int(bondList[-1][4]) - 1][4]) + (distance * m.sin(result + (45 * m.pi)))], zorder=1,
        #          color='dimgrey', linewidth=2)

        self.drawer.plotBond([float(atomList[int(bondList[-1][3]) - 1][3]) + (distance * m.cos(result + (45 * m.pi))),
                              float(atomList[int(bondList[-1][4]) - 1][3]) + (distance * m.cos(result + (45 * m.pi)))],
                             [float(atomList[int(bondList[-1][3]) - 1][4]) + (distance * m.sin(result)),
                              float(atomList[int(bondList[-1][4]) - 1][4]) + (distance * m.sin(result))])

    def tripleBond(self, atomList: list, bondList: list):
        pass
