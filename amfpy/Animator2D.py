from .constants import *
from .amfreader import *

bondLength = []


def animate2D(f: int):
    # for i in range(f):
    atomlist, bondlist = Reader.getLists()
    if len(atomlist) != len(bondlist):
        yield
        # print("Step " + str(i))
