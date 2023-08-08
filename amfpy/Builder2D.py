import matplotlib.pyplot as plt
from constants import *


class Drawer:

    def plotAtom(self, x: float, y: float, atomnumber: int):
        plt.plot(x, y, marker="o", color=getAtomColor(atomnumber))
    def plotBond(self):
        pass

    @staticmethod
    def plotAll():
        plt.plot()
