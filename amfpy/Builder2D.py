import matplotlib.pyplot as plt


class Drawer:
    def plotAtom(self, x: float, y: float, atomnumber: int):
        plt.plot(x,y)

    def plotBond(self):
        pass

    @staticmethod
    def plotAll():
        plt.plot()
