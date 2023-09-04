from .amfreader import *
from .Builder2D import *
from .Animator2D import *
from time import sleep
from multiprocessing import Process


def build():
    Drawer.plotAll()


def animate(f: int):
    animate2D(f)
