import matplotlib.pyplot as plt
from .constants import *


class Drawer:

    def plotAtom(self, x: float, y: float, atomnumber: int):
        plt.plot(x, y, marker="o", color=getAtomColor(atomnumber))

    def plotBond(self, xlist: list, ylist: list, atomnumber: int):
        plt.plot(xlist, ylist, color="g", linewidth=2)

    @staticmethod
    def plotAll():
        plt.plot()
