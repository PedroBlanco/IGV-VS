from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from math import cos
from math import sin
from math import tan
from math import pi

import igv_utils    # Módulo con funciones definidas para la asignatura
import igv_3dobjects #Libreria de objetos recopilados y creados para la asignatura

axes_length = 100 # Máxima longitud de los ejes coordenados (se dibujarán desde -axes_length hasta +axes_length)
xMin = yMin = zMin = - axes_length
xMax = yMax = zMax = axes_length


# Definición de colores
grey = [128/255, 128/255, 128/255]
blue = [0, 204/255, 1]

yellow_1 = [254/255, 249/255, 231/255]
yellow_2 = [252/255, 243/255, 207/255]
yellow_3 = [247/255, 220/255, 111/255]
yellow_4 = [241/255, 196/255, 15/255]
yellow_5 = [183/255, 149/255, 11/255]

yellow_range = [yellow_1, yellow_2, yellow_3, yellow_4, yellow_5]
light_yellow_range = [yellow_1, yellow_2, yellow_3]
dark_yellow_range = [yellow_3, yellow_4, yellow_5]

brown_1 = [250/255, 229/255, 211/255]
brown_2 = [240/255, 178/255, 122/255]
brown_3 = [230/255, 126/255, 34/255]
brown_4 = [175/255, 96/255, 26/255]
brown_5 = [120/255, 66/255, 18/255]

brown_range = [brown_1, brown_2, brown_3, brown_4, brown_5]
light_brown_range = [brown_1, brown_2, brown_3]
dark_brown_range = [brown_3, brown_4, brown_5]

blue_1 = [214/255, 234/255, 248/255]
blue_2 = [133/255, 193/255, 233/255]
blue_3 = [52/255, 152/255, 219/255]
blue_4 = [40/255, 116/255, 166/255]
blue_5 = [27/255, 79/255, 114/255]

blue_range = [blue_1, blue_2, blue_3, blue_4, blue_5]
light_blue_range = [blue_1, blue_2, blue_3]
dark_blue_range = [blue_3, blue_4, blue_5]

green_1 = [213/255, 245/255, 227/255]
green_2 = [130/255, 224/255, 170/255]
green_3 = [46/255, 204/255, 113/255]
green_4 = [35/255, 155/255, 86/255]
green_5 = [24/255, 106/255, 59/255]

green_range  = [green_1, green_2, green_3, green_4, green_5]
light_green_range  = [green_1, green_2, green_3]
dark_green_range  = [green_3, green_4, green_5]

red_1 = [250/255, 219/255, 216/255]
red_2 = [241/255, 148/255, 138/255]
red_3 = [231/255, 76/255, 60/255]
red_4 = [176/255, 58/255, 46/255]
red_5 = [120/255, 40/255, 31/255]

red_range = [red_1, red_2, red_3, red_4, red_5]
light_red_range = [red_1, red_2, red_3]
dark_red_range = [red_3, red_4, red_5]


grey_1 = [242/255, 243/255, 244/255]
grey_2 = [215/255, 219/255, 221/255] 
grey_3 = [189/255, 195/255, 199/255] 
grey_4 = [144/255, 148/255, 151/255] 
grey_5 = [98/255, 101/255, 103/255] 

grey_range = [grey_1, grey_2, grey_3, grey_4, grey_5]
light_grey_range = [grey_1, grey_2, grey_3]
dark_grey_range = [grey_3, grey_4, grey_5]

black_5 = [27/255, 38/255, 49/255] 
grey_6 = [70/255, 70/255, 70/255] 
grey_7 = [50/255, 50/255, 50/255] 
grey_8 = [30/255, 30/255, 30/255]
 
grey_range = [grey_1, grey_2, grey_3, grey_4, grey_5]
light_grey_range = [grey_1, grey_2, grey_3]
dark_grey_range = [grey_4, grey_5, grey_6]
very_dark_grey = [grey_6, grey_7, grey_8]
                  
color_piel_claro = [220/255, 190/255, 170/255]
color_piel_oscuro = [215/255, 185/255, 165/255]
color_piel = [color_piel_claro, color_piel_claro, color_piel_claro, color_piel_claro, color_piel_oscuro]

camisa_azul_claro = [15/255, 100/255, 125/255]
camisa_azul_oscuro = [10/255, 95/255, 120/255]
color_camisa = [camisa_azul_claro, camisa_azul_claro, camisa_azul_oscuro]

color_pantalon_claro = [55/255, 40/255, 25/255]
color_pantalon_oscuro = [50/255, 35/255, 20/255]
color_pantalon = [color_pantalon_claro, color_pantalon_claro, color_pantalon_oscuro]

color_zapato_claro = [110/255, 80/255, 70/255]
color_zapato_oscuro = [105/255, 75/255, 65/255]
color_zapato = [color_zapato_claro, color_zapato_claro, color_zapato_oscuro]

color_sombrero_claro = [255/255, 205/255, 5/255]
color_sombrero_oscuro = [250/255, 200/255, 0/255]
color_sombrero = [color_sombrero_claro, color_sombrero_oscuro]
# Definir colores para el creeper
color_creeper_verde_claro = [102/255, 204/255, 102/255]  # Verde claro creeper
color_creeper_verde_oscuro = [76/255, 153/255, 76/255]   # Verde oscuro creeper
color_creeper_negro = [0, 0, 0]                          # Negro para ojos y boca
color_creeper = [color_creeper_verde_claro, color_creeper_verde_claro, color_creeper_verde_claro, 
                 color_creeper_verde_oscuro, color_creeper_verde_oscuro]

# Definición de colores para el Golem
color_golem_hierro_claro = [200/255, 200/255, 200/255]  # Hierro claro
color_golem_hierro_medio = [170/255, 170/255, 170/255]  # Hierro medio
color_golem_hierro_oscuro = [140/255, 140/255, 140/255]  # Hierro oscuro
color_golem_hierro = [color_golem_hierro_claro, color_golem_hierro_medio, color_golem_hierro_oscuro]

color_golem_ojos = [30/255, 30/255, 30/255]  # Negro para ojos

# Necesario para controlar qué objetos mostramos
visibilidad = {
    "ejes": True,
    "coche": False,
    "carril_bici": False,
    "acerado": False,
    "carretera": False,
    "pasodecebra": False,
    "semaforo": False,
    "farola": False
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
            print(f"Tecla {key} pulsada -> Salir")
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

        case b'5':
            print("Tecla 5 pulsada -> Cambiar visibilidad de pasodecebra")
            cambiar_visibilidad("pasodecebra")

        case b'6':
            print("Tecla 6 pulsada -> Cambiar visibilidad de semaforo")
            cambiar_visibilidad("semaforo")

        case b'7':
            print("Tecla 7 pulsada -> Cambiar visibilidad de farola")
            cambiar_visibilidad("farola")

        case _:
            print(f"Tecla sin acción asignada: {key}")


def salir():
    
    try:
        glutLeaveMainLoop()
    except Exception:
        import os
        os._exit(0)


def init_gl():
    glutInit()                                     # Inicializa la librerÃ­a GLUT
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)    # Ãšnico frame buffer y modo de color RGB y buffer de prof
    glutInitWindowSize(1000, 600)                   #(height, width)
    glutInitWindowPosition(100, 100)               #(x pos, y pos)
    glutCreateWindow(b'actividad grupal')          # CreaciÃ³n de la ventana (si no se pone b da error)
    glClearColor(1.0, 1.0, 1.0, 1.0);              # Color del buffer
    
    glutSetOption(GLUT_ACTION_ON_WINDOW_CLOSE, GLUT_ACTION_GLUTMAINLOOP_RETURNS)
    
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_DEPTH_TEST)                        # HABILITA COMPROBACIÓN DE PROFUNDIDAD EN EL DIBUJO 


def draw_viewport(vp_x, vp_y, vp_w, vp_h, projection, lookAt, label):
    """
    Configura un viewport y dibuja el mundo.
 
    projection: "ortho"       → proyección paralela ortogonal
                "cabinet"     → proyección paralela oblicua gabinete
                "perspective" → proyección en perspectiva simetrica
 
    lookAt:     "d"  → default (z-)   "x+" → eje X+   "x-" → eje X-
                "z+" → eje Z+         "y+" → eje Y+    "perspectiva" (camara elevada)
    """
 
    glViewport(vp_x, vp_y, vp_w, vp_h)
 
    # Establecer dNear y dFar en función de los límites del eje Z
    dNear = -zMax;  dFar = -zMin    # El plano de proyeccion es z = -dNear
 
    ##############################
    # PREPARACIÓN DE LA PROYECCIÓN
    ##############################
 
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
 
    if projection == "cabinet":
        # PREPARACIÓN DE LA MATRIZ DE CONVERSIÓN GABINETE
        factor = pi/180                 # Factor de conversión de grados a radianes
        alpha = 63.4                    # Definicion del angulo alfa
        alpha = alpha * factor          # Conversión a radianes
        # phi = 45                      # Definicion del angulo phi
        phi = 30                        # Definicion del angulo phi
        phi = phi * factor              # Conversión a radianes
        cx = cos(phi)/tan(alpha)
        cy = sin(phi)/tan(alpha)
        cabinet_matrix = [1, 0, 0, 0, 0, 1, 0, 0, cx, cy, 1, 0, 0, 0, 0, 1]
        glMultMatrixf(cabinet_matrix)   # definición de la proyección (tipo gabinete)
        glOrtho(xMin, xMax, yMin, yMax, dNear, dFar)
 
    elif projection == "perspective":
        # PROYECCIÓN EN PERSPECTIVA SIMÉTRICA
        aspect = vp_w / vp_h
        # gluPerspective(50, aspect, 1, 60)
        gluPerspective(100, aspect, 1, 800)
 
    else:   # "ortho"
        glOrtho(xMin, xMax, yMin, yMax, dNear, dFar)
 
    ##############################
    # PREPARACIÓN DE LA CÁMARA
    ##############################
 
    if lookAt == "x+":
        x0=0.0; y0=0.0; z0=0.0;  xref=1.0;  yref=0.0; zref=0.0;  vx=0.0; vy=1.0; vz=0.0
    elif lookAt == "x-":
        x0=0.0; y0=0.0; z0=0.0;  xref=-1.0; yref=0.0; zref=0.0;  vx=0.0; vy=1.0; vz=0.0
    elif lookAt == "z+":
        x0=0.0; y0=0.0; z0=0.0;  xref=0.0;  yref=0.0; zref=1.0;  vx=0.0; vy=1.0; vz=0.0
    elif lookAt == "y+":
        x0=0.0; y0=0.0; z0=0.0;  xref=0.0;  yref=1.0; zref=0.0;  vx=0.0; vy=0.0; vz=1.0
    elif lookAt == "perspectiva":
        # x0=14.0; y0=12.0; z0=14.0;  xref=0.0; yref=3.0; zref=0.0;  vx=0.0; vy=1.0; vz=0.0
        x0=90.0; y0=100.0; z0=70.0;  xref=0.0; yref=3.0; zref=0.0;  vx=0.0; vy=1.0; vz=0.0
    else:   # default (z-)
        x0=0.0; y0=0.0; z0=0.0;  xref=0.0;  yref=0.0; zref=-1.0;  vx=0.0; vy=1.0; vz=0.0
 
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(x0, y0, z0, xref, yref, zref, vx, vy, vz)
 
    draw_mundo()
    igv_utils.draw_label_viewport(label, vp_w, vp_h)



def display():
 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Borrar buffers
 
    win_w = glutGet(GLUT_WINDOW_WIDTH)
    win_h = glutGet(GLUT_WINDOW_HEIGHT)
    vp_w  = win_w // 2
    vp_h  = win_h // 2
 
    # Viewport 1 (arriba-izquierda): proyección gabinete, vista por defecto (z-)
    draw_viewport(0, vp_h, vp_w, vp_h,
                  projection="cabinet", lookAt="d",
                  label="Gabinete")
 
    # Viewport 2 (arriba-derecha): proyección ortogonal, vista posterior (z+)
    draw_viewport(vp_w, vp_h, vp_w, vp_h,
                  projection="ortho", lookAt="z+",
                  label="Ortogonal posterior")
 
    # Viewport 3 (abajo-izquierda): proyección ortogonal, vista lateral derecha (x-)
    draw_viewport(0, 0, vp_w, vp_h,
                  projection="ortho", lookAt="x-",
                  label="Ortogonal lateral der.")
 
    # Viewport 4 (abajo-derecha): proyección en perspectiva, cámara elevada
    draw_viewport(vp_w, 0, vp_w, vp_h,
                  projection="perspective", lookAt="perspectiva",
                  label="Perspectiva simétrica")
 
    glFlush()


def draw_mundo():
    igv_utils.axes(xMin, xMax, yMin, yMax, zMin, zMax, True)  # Dibujo de los ejes de coordenadas
    # glPushMatrix()
    # glTranslatef(-100, 0, 70)
    # igv_3dobjects.carril_bici()
    # glPopMatrix()

    # glPushMatrix()
    # glTranslatef(-100, 0, 30)
    # igv_3dobjects.acerado()
    # glPopMatrix()

    # glPushMatrix()
    # glTranslatef(-100, 0, -10)
    # igv_3dobjects.carretera()
    # glPopMatrix()

    # glPushMatrix()
    # glTranslatef(20, 0, -8)
    # igv_3dobjects.pasodecebra()
    # glPopMatrix()

    # glPushMatrix()
    # glTranslatef(20, 0, -8)
    # igv_3dobjects.semaforo() #Semaforo junto al paso de cebra
    # glPopMatrix()

    glPushMatrix()
    glTranslatef(20, 0, -8)
    glScalef(4.0, 4.0, 4.0) 
    glRotatef(90.0, 0.0, 1.0, 0.0)
    igv_3dobjects.bicicleta()
    glPopMatrix()


# def draw_mundo():
#     if visibilidad["ejes"]:
#         igv_utils.axes(xMin, xMax, yMin, yMax, zMin, zMax, True)

#     if visibilidad["carril_bici"]:
#         glPushMatrix()
#         glTranslatef(-100, 0, 70)
#         igv_3dobjects.carril_bici()
#         glPopMatrix()

#     if visibilidad["acerado"]:
#         glPushMatrix()
#         glTranslatef(-100, 0, 30)
#         igv_3dobjects.acerado()
#         glPopMatrix()

#     if visibilidad["carretera"]:
#         glPushMatrix()
#         glTranslatef(-100, 0, -10)
#         igv_3dobjects.carretera()
#         glPopMatrix()

#     if visibilidad["coche"]:
#         glPushMatrix()
#         glTranslatef(60, 0, 65)
#         igv_3dobjects.coche()
#         glPopMatrix()
    
#     if visibilidad["pasodecebra"]:
#         glPushMatrix()
#         glTranslatef(20, 0, -8)
#         igv_3dobjects.pasodecebra()
#         glPopMatrix()

#     if visibilidad["semaforo"]:
#         glPushMatrix()
#         # glTranslatef(15, 0, -5)
#         #glTranslatef(18, 4, 42)
#         # Cambio rápido
#         glTranslatef(20, 0, -8) #Al lado del paso de cebra
#         # rotar en el eje y 90 grados 
#         glRotatef(90, 0, 1, 0)
#         igv_3dobjects.semaforo()
#         glPopMatrix()

#     if visibilidad["farola"]:
#         glPushMatrix()
#         glTranslatef(60, 0, 65)
#         glRotatef(90, 0, 1, 0)
#         igv_3dobjects.farolav4()
#         glPopMatrix()
#         glPushMatrix()
#         glTranslatef(-60, 0, 59)
#         glRotatef(270, 0, 1, 0)
#         igv_3dobjects.farolav4()
#         glPopMatrix()



def main():
    init_gl()
    glutDisplayFunc(display)
    glutKeyboardFunc(gestiona_tecla)
    glutMainLoop()   

main()

