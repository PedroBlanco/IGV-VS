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
        case b'\x1b'| b'q' | b'Q':  # ESC, q ó Q
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

def draw_label_viewport(label, vp_w, vp_h):
    """
    Dibuja una etiqueta 2D en la esquina superior izquierda
    del viewport activo.
    """

    margen_x = 10
    margen_y = 20

    # Desactivar profundidad para que el texto no quede oculto
    glDisable(GL_DEPTH_TEST)

    # Guardar matriz de proyección actual
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()

    # Sistema de coordenadas 2D del viewport:
    # x: 0 -> vp_w
    # y: 0 -> vp_h
    gluOrtho2D(0, vp_w, 0, vp_h)

    # Guardar matriz de modelo/vista actual
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    # Color del texto
    glColor3f(0.0, 0.0, 0.0)

    # Esquina superior izquierda
    igv_utils.draw_text_3d(
        label,
        margen_x,
        vp_h - margen_y,
        0
    )

    # Restaurar matriz de modelo/vista
    glPopMatrix()

    # Restaurar matriz de proyección
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()

    # Volver a modelo/vista
    glMatrixMode(GL_MODELVIEW)

    # Reactivar profundidad para el resto del dibujo
    glEnable(GL_DEPTH_TEST)
