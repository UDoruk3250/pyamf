from .amfreader import *
from .Builder2D import *
from .Animator2D import *
from multiprocessing import Process


def build():
    Drawer.plotAll()
    while True:
        pass

def animate(f: int):
    print("HEY!!")
    animate2D(f)
