# Vamos a importar todas las librería pertinentes, ya habrá tiempo para quitar las que no se usan
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from random import choice
import igv_utils 
from math import sqrt
from math import cos
from math import sin
from math import tan
from math import pi
import random
from random import randint
from random import choice


def gestiona_tecla(key, x, y):
    global window_id

    if key == b'\x1b':  # ESC
        print("ESC pulsado -> Salir")
        salir()

def salir():
    try:
        glutLeaveMainLoop()
    except Exception:
        # Plan B si no estás usando freeglut real
        try:
            if window_id is not None:
                glutDestroyWindow(window_id)
        finally:
            import os
            os._exit(0)
