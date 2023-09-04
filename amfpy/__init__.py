from .amfreader import *
from .Builder2D import *
from .Animator2D import *
from time import sleep
from multiprocessing import Process


def build(animate=False, frate=0):
    if not animate:
        Drawer.plotAll()
    else:
        animate2D(frate)


