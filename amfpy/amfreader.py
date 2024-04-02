from .OriginBuilder import *
from .constants import *

condition = False

atomlist = []
bondlist = []
commandlist = []


class Reader:
    def __init__(self, molecule):
        global atomlist, bondlist, commandlist
        self.MOLECULE = molecule
        self.commandList = []
        self.atomList = []
        self.condition = False
        self.bondList = []

        with open(self.MOLECULE, "r") as f:
            for enum, line in enumerate(f):
                if len(line) > 1:
                    self.commandList.append(line.split())
                    if self.commandList[-1][0] == "END":
                        break
                    if self.commandList[-1][0] == "ORI":
                        builder = Origin("".join(self.commandList[-1][1:]))
                        file = open(molecule, "r").readlines()[enum:]
                        i = 0
                        while "STOP" not in file[i]:
                            i += 1

                        builder.add(
                            (lambda x: [a.replace("\n", "") for a in x])(file[:i]
                                                                         .copy()))

                    if self.commandList[-1][0] == "STT":
                        self.condition = True
                    if self.condition:
                        if self.commandList[-1][0] == "ATOM":
                            self.atomList.append(line.split())
                            atomlist.append(self.atomList[-1])
                            color = getAtomColor(int(self.commandList[-1][2]))
                            plt.plot(int(self.commandList[-1][3]), int(self.commandList[-1][4]),
                                     marker="o", color=color)
                        elif self.commandList[-1][0] == "INS":
                            self.atomList, self.bondList = builder.buildOriginPrefab("ORI " + self.commandList[-1][1],
                                                                                     self.commandList[-1][2:])
                            self.setLists()

                        elif self.commandList[-1][0] == "BND":
                            self.bondList.append(line.split())
                            bondlist.append(self.bondList[-1])
                            plt.plot(
                                [float(self.atomList[int(self.bondList[-1][2]) - 1][3]),
                                 float(self.atomList[int(self.bondList[-1][3]) - 1][3])],
                                [float(self.atomList[int(self.bondList[-1][2]) - 1][4]),
                                 float(self.atomList[int(self.bondList[-1][3]) - 1][4])],
                                color='g', linewidth=2)
                    commandlist.append(self.commandList[-1])

    def setLists(self):
        global atomlist, bondlist
        atomlist.append(self.atomList.copy())
        bondlist.append(self.bondList.copy())

    @staticmethod
    def getLists():
        global atomlist, bondlist
        return [atomlist, bondlist]

