from .constants import *
from .amfreader import Reader

bondLength = []

CorruptedFileError = Exception("The *.amf file has been corrupted or formatted wrong. Check the file again.")


def animate2D(f: int):
    # for i in range(f):
    atomlist, bondlist = Reader.getLists()
    if len(atomlist) != len(bondlist):
        raise CorruptedFileError
    print("a")

    # print("Step " + str(i))
