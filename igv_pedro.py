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


# Necesario para controlar qué objetos mostramos
visibilidad = {
    "ejes": True,
    "coche": False,
    "carril_bici": False,
    "acerado": False,
    "carretera": False,
}

def cambiar_visibilidad(nombre_objeto):
    global visibilidad

    if nombre_objeto not in visibilidad:
        print(f"Objeto no reconocido: {nombre_objeto}")
        return

    visibilidad[nombre_objeto] = not visibilidad[nombre_objeto]

    estado = "visible" if visibilidad[nombre_objeto] else "oculto"
    print(f"{nombre_objeto}: {estado}")

    glutPostRedisplay()


def gestiona_tecla(key, x, y):
    match key:
        case b'\x1b':  # ESC
            print("ESC pulsado -> Salir")
            salir()

        case b'0':
            print("Tecla 0 pulsada -> Cambiar visibilidad de ejes")
            cambiar_visibilidad("ejes")

        case b'1':
            print("Tecla 1 pulsada -> Cambiar visibilidad de coche")
            cambiar_visibilidad("coche")

        case b'2':
            print("Tecla 2 pulsada -> Cambiar visibilidad de carril_bici")
            cambiar_visibilidad("carril_bici")

        case b'3':
            print("Tecla 3 pulsada -> Cambiar visibilidad de acerado")
            cambiar_visibilidad("acerado")

        case b'4':
            print("Tecla 4 pulsada -> Cambiar visibilidad de carretera")
            cambiar_visibilidad("carretera")

        case _:
            print(f"Tecla sin acción asignada: {key}")


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
