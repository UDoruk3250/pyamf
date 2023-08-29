from .OriginBuilder import *
from .constants import *
commandlist = []
atomlist = []
condition = False
bondlist = []

class Reader:

    def __init__(self, molecule):
        self.MOLECULE = molecule
        self.commandlist = []
        self.atomlist = []
        self.condition = False
        self.bondlist = []

        plt.axes().set_facecolor("black")
        with open(self.MOLECULE, "r") as f:
            for enum, line in enumerate(f):
                if len(line) > 1:
                    self.commandlist.append(line.split())
                    if self.commandlist[-1][0] == "END":
                        break
                    if self.commandlist[-1][0] == "ORI":
                        builder = Origin("".join(self.commandlist[-1][1:]))
                        file = open(molecule, "r").readlines()[enum:]
                        i = 0
                        while "STOP" not in file[i]:
                            i += 1

                        builder.add(
                            (lambda x: [a.replace("\n", "") for a in x])(file[:i]
                                                                         .copy()))

                    if self.commandlist[-1][0] == "STT":
                        self.condition = True
                    if self.condition:
                        if self.commandlist[-1][0] == "ATOM":
                            self.atomlist.append(line.split())
                            if self.atomlist[-1][2] == '8':
                                color = 'red'
                            color = getAtomColor(self.commandlist[-1][2])
                            plt.plot(int(self.commandlist[-1][3]), int(self.commandlist[-1][4]),
                                     marker="o", color=color)
                        elif self.commandlist[-1][0] == "INS":
                            builder.buildOriginPrefab("ORI " + self.commandlist[-1][1], self.commandlist[-1][2:])
                        elif self.commandlist[-1][0] == "BND":
                            self.bondlist.append(line.split())
                            plt.plot(
                                [float(self.atomlist[int(self.bondlist[-1][2]) - 1][3]),
                                 float(self.atomlist[int(self.bondlist[-1][3]) - 1][3])],
                                [float(self.atomlist[int(self.bondlist[-1][2]) - 1][4]),
                                 float(self.atomlist[int(self.bondlist[-1][3]) - 1][4])],
                                color='g', linewidth=2)

        commandlist = self.commandlist
        bondlist = self.bondlist
        atomlist = self.atomlist
