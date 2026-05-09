#########################################################################################

#########################################################################################
# Importación de módulos

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import igv_utils

from random import randint
from random import choice

from math import sqrt
from math import cos
from math import sin
from math import tan
from math import pi


#########################################################################################
# Definición de colores
#########################################################################################

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

black_1 = [100/255, 100/255, 100/255]
black_2 = [75/255, 75/255, 75/255]
black_3 = [50/255, 50/255, 50/255]
black_4 = [25/255, 25/255, 25/255]
black_5 = [0, 0, 0]

black_range = [black_1, black_2, black_3, black_4, black_5]
light_black_range = [black_1, black_2, black_3]
dark_black_range = [black_3, black_4, black_5]

beige_1 = [218/255, 198/255, 181/255]
beige_2 = [212/255, 189/255, 168/255]
beige_3 = [206/255, 179/255, 156/255]
beige_4 = [200/255, 170/255, 143/255]
beige_5 = [196/255, 160/255, 131/255]

beige_range = [beige_1, beige_2, beige_3, beige_4, beige_5]
light_beige_range = [beige_1, beige_2, beige_3]
dark_beige_range = [beige_3, beige_4, beige_5]

#########################################################################################
# Definición de funciones
#########################################################################################

def solid_face_xz(x_size, z_size, colors):
    
    """
    Función que dibuja una cara sólida en el plano XZ, formada por cubos de lado uno y colores aleatorios.
    La esquina inferior posterior izquierda de la cara es un cubo centrado en el punto (0,0,0).
    El tamaño de la cara y la paleta de colores se definen a través de los parámetros de la función.
        
    Args:
        x_size: dimensión en el eje X. >= 2
        z_size: dimensión en el eje Z. >= 2
        colors: Array/lista de colores que se seleccionan aleatoriamente.
    """
    
    
    # Comprobar x_size, z_size
    if (x_size < 2) or (z_size < 2):
        print("Error en los parámetros de solid_face_xz")
        return
    
    # Preservar la matriz MODELVIEW
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
        
    for x in range(x_size):
        for z in range(z_size):
            color = choice(colors)  # Generar el color si es necesario (figura multicolor)
            igv_utils.color_cube(color)
            glTranslatef(0, 0, 1)      # Desplazamiento en Z
        glTranslatef(1, 0, -z_size)    # Retorno al eje X
        
    # Restaurar la matriz MODELVIEW
    glPopMatrix()




def solid_face_yz(y_size, z_size, colors):
    
    """
    Función que dibuja una cara sólida en el plano YZ, formada por cubos de lado uno y colores aleatorios.
    Se construye a partir de la función solid_face_xz(...) girando 90 grados sobre el eje Z.
    La esquina inferior posterior de la cara es un cubo centrado en el punto (0,0,0).
    El tamaño de la cara y la paleta de colores se definen a través de los parámetros de la función.
        
    Args:  
        y_size: dimensión en el eje Y. >= 2
        z_size: dimensión en el eje Z. >= 2
        colors: Array/lista de colores que se seleccionan aleatoriamente.
    """
    
    # Comprobar y_size, z_size
    if (y_size < 2) or (z_size < 2):
        print("Error en los parámetros de solid_face_yz")
        return
    
    # Preservar la matriz MODELVIEW
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    
    # Preparación de la rotación
    glRotatef(90, 0, 0, 1)

    solid_face_xz(y_size, z_size, colors)
        
    # Restaurar la matriz MODELVIEW 
    glPopMatrix()



def solid_face_xy(x_size, y_size, colors):
    
    """
    Función que dibuja una cara sólida en el plano XY, formada por cubos de lado uno y colores aleatorios.
    Se construye a partir de la función solid_face_xz(...) girando -90 grados sobre el eje X.
    La esquina inferior posterior izquierda de la cara es un cubo centrado en el punto (0,0,0).
    El tamaño de la cara y la paleta de colores se definen a través de los parámetros de la función.
        
    Args:
        x_size: dimensión en el eje X. >= 2
        y_size: dimensión en el eje Y. >= 2
        colors: Array/lista de colores que se seleccionan aleatoriamente.
    """
    
    # Comprobar x_size, y_size
    if (x_size < 2) or (y_size < 2):
        print("Error en los parámetros de solid_face_xy")
        return
    
    # Preservar la matriz MODELVIEW
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    
    # Preparación de la rotación
    glRotatef(-90, 1, 0, 0)

    solid_face_xz(x_size, y_size, colors)

    # Restaurar la matriz MODELVIEW    
    glPopMatrix()



def empty_ortho(x_size, y_size, z_size, colors):
    
    """
    Función que dibuja un ortoedro hueco, formado por cubos de lado uno y colores aleatorios.
    La esquina inferior posterior izquierda del ortoedro es un cubo centrado en el punto (0,0,0).
    El tamaño del ortoedro y la paleta de colores se definen a través de los parámetros de la función.
        
    Args:
        x_size: dimensión en el eje X. >= 4
        y_size: dimensión en el eje Y. >= 4
        z_size: dimensión en el eje Z. >= 4
        colors: Array/lista de colores que se seleccionan aleatoriamente.
    """
    
    # Comprobar x_size, y_size, z_size
    if (x_size < 4) or (y_size < 4) or (z_size < 4):
        print("Error en los parámetros de empty_ortho")
        return
    
    # Preservar la matriz MODELVIEW
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()  
    
    # cara inferior
    solid_face_xz(x_size, z_size, colors)
   
    # cara lateral izquierda
    glTranslate(0, 1, 0)
    solid_face_yz(y_size-2, z_size, colors)
    
    # cara lateral derecha
    glTranslate(x_size-1, 0, 0)
    solid_face_yz(y_size-2, z_size, colors)    
    
    # cara posterior
    glTranslate(-(x_size-2), 0, 0)
    solid_face_xy(x_size-2, y_size-2, colors)     
    
    # cara frontal
    glTranslate(0, 0, z_size-1)
    solid_face_xy(x_size-2, y_size-2, colors)
    
    # cara superior
    glTranslate(-1, y_size-2, -(z_size-1))
    solid_face_xz(x_size, z_size, colors) 
    
    # Restaurar la matriz MODELVIEW
    glPopMatrix() 
    

def solid_ortho(x_size, y_size, z_size, colors):
    
    """
    Función que dibuja un ortoedro sólido, formado por cubos de lado uno y colores aleatorios.
    La esquina inferior posterior izquierda del ortoedro es un cubo centrado en el punto (0,0,0).
    El tamaño del ortoedro y la paleta de colores se definen a través de los parámetros de la función.
        
    Args:
        x_size: dimensión en el eje X. >= 1
        y_size: dimensión en el eje Y. >= 1
        z_size: dimensión en el eje Z. >= 1
        colors: Array/lista de colores que se seleccionan aleatoriamente.
    """
    
    # Comprobar x_size, y_sixe, z_size
    if (x_size < 1) or (y_size < 1) or (z_size < 1):
        print("Error en los parámetros de solid_ortho")
        return
    
    # Preservar la matriz MODELVIEW
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()      
        
    for y in range(y_size):    
        for x in range(x_size):
            for z in range(z_size):
                color = choice(colors) # Generar el color si es necesario (figura multicolor)
                igv_utils.color_cube(color)
                glTranslatef(0, 0, 1)
            glTranslatef(1, 0, -z_size)
        glTranslate(-x_size, 1, 0)
        
    # Restaurar la matriz MODELVIEW
    glPopMatrix()
   


def empty_face_xz(x_size, z_size, colors):
    
    """
    Función que dibuja una cara hueca (sólo el contorno) en el plano XZ, formado por cubos de lado uno y colores aleatorios.
    La esquina inferior posterior izquierda de la cara es un cubo centrado en el punto (0,0,0).
    El tamaño de la cara y la paleta de colores se definen a través de los parámetros de la función.
        
    Args:
        x_size: dimensión en el eje X. >= 3
        z_size: dimensión en el eje Z. >= 3
        colors: Array/lista de colores que se seleccionan aleatoriamente.
    """
    
    # Comprobar x_size, z_size
    if (x_size < 3) or (z_size < 3):
        print("Error en los parámetros de empty_face_xz")
        return
    
    # Preservar la matriz MODELVIEW
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    
       
    for x in range(x_size-1):
        color = choice(colors)
        igv_utils.color_cube(color)
        glTranslatef(1, 0, 0)

            
    for z in range(z_size-1):
        color = choice(colors)
        igv_utils.color_cube(color)
        glTranslatef(0, 0, 1)            
            
    for x in range(x_size-1):
        color = choice(colors)
        igv_utils.color_cube(color)
        glTranslatef(-1, 0, 0)           
            

    for z in range(z_size):
        color = choice(colors)
        igv_utils.color_cube(color)
        glTranslatef(0, 0, -1)   
    
    # Restaurar la matriz MODELVIEW
    glPopMatrix()
