from .amfreader import *
from .Builder2D import *
from .Animator2D import *


def build(animate=False, frate=0):
    if not animate:
        Drawer.plotAll(True)
    else:
        Drawer.plotAll(False)
        animate2D(frate)
        Drawer.plotAll(True)
