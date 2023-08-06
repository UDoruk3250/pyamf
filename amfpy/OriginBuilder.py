import matplotlib.pyplot as plt
from .BondBuilder import *

bondbuilder = BondBuilder()


class Origin:
    def __init__(self, oriname):
        self.name = oriname
        self.cList = {}
        self.atomList = []
        self.bondList = []

    def add(self, args: list):
        # print("Key: " + args.copy()[0])
        self.cList[args.copy()[0]] = args.copy()

    def buildOriginPrefab(self, id, coords):
        x, y, z = coords
        for atom in self.cList[id][1:]:
            if len(atom) > 1:
                if atom.split()[0] == "ATOM":
                    if atom.split()[2] == '8':
                        oricolor = 'red'
                    elif atom.split()[2] == '1':
                        oricolor = 'whitesmoke'
                    elif atom.split()[2] == '7':
                        oricolor = "limegreen"
                    else:
                        oricolor = 'blue'
                    self.atomList.append(["ATOM", atom.split()[1], atom.split()[2], str(float(atom.split()[3]) + float(x)),
                                     str(float(atom.split()[4]) + float(y))])
                    plt.plot(float(atom.split()[3]) + float(x), float(atom.split()[4]) + float(y),
                             marker="o", color=oricolor)

                elif atom.split()[0] == "BND":
                    self.bondList.append(atom.split())

                    if self.bondList[-1][2] == "1":

                        # print("X1: ", x1, ", X2: ", x2, ", Y1: ", y1, ", Y2: ", y2)
                        # print(self.atomList[len(self.bondList) - 1])
                        bondbuilder.singleBond(self.atomList, self.bondList)
                    elif self.bondList[-1][2] == "2":
                        print("DOUBLE BOND")
                        bondbuilder.doubleBond(self.atomList, self.bondList)
                    elif self.bondList[-1][2] == "3":
                        bondbuilder.tripleBond(self.atomList, self.bondList)
                    else:
                        plt.plot(
                            [float(self.atomList[int(self.bondList[-1][3]) - 1][3]),
                             float(self.atomList[int(self.bondList[-1][4]) - 1][3])],
                            [float(self.atomList[int(self.bondList[-1][3]) - 1][4]),
                             float(self.atomList[int(self.bondList[-1][4]) - 1][4])],
                            color='g', zorder=2, linewidth=2)

                else:
                    break
