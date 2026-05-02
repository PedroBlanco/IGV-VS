
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



def solid_face_xz(x_size, z_size, colors):
    
    # Comprobar x_size, z_size
    if (x_size < 2) or (z_size < 2):
        print("Error en los parámetros de solid_face_xz")
        return
    
    # Preservar la matriz MODELVIEW
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    
    for x in range(x_size):
        for z in range(z_size):
            color = choice(colors)       # Generar el color 
            igv_utils.color_cube(color)  # Dibujar el cubo
            glTranslatef(0, 0, 1)        # Desplazamiento en Z
        glTranslatef(1, 0, -z_size)      # Retorno al eje X
        
     
    # Restaurar la matriz MODELVIEW
    glPopMatrix()

def solid_face_yz(y_size, z_size, colors):
    
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
    
    # Comprobar x_size, y_sixe, z_size, density
    if (x_size < 1) or (y_size < 1) or (z_size < 1):
        print("Error en los parámetros de solid_ortho")
        return
    
    # Preservar la matriz MODELVIEW
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    
    for y in range(y_size):    
        for x in range(x_size):
            for z in range(z_size):
                color = choice(colors) # Generar el color 
                igv_utils.color_cube(color)
                glTranslatef(0, 0, 1)
            glTranslatef(1, 0, -z_size)
        glTranslate(-x_size, 1, 0)
        
    # Restaurar la matriz MODELVIEW
    glPopMatrix()


def density_face_xz(x_size, z_size, density, colors):
    
    # Comprobar x_size, z_size, density
    if (x_size < 2) or (z_size < 2) or (density < 0):
        print("Error en los parámetros de density_face_xz")
        return
    
    # Preservar la matriz MODELVIEW
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
        
        
    # Cálculo de los puntos necesarios según la densidad
    max_cubes = x_size * z_size
    #print(f"posibles cubos = {x_size} x {z_size} = {max_cubes}")
    
    num_cubes = int((max_cubes * density) / 100)
    #print(f"{density}% de {max_cubes} = {num_cubes}")
    
    n = 0   # Contador para sumar el número de cubos 
        
    for x in range(x_size):
        for z in range(z_size):
            if randint(0,100) < density:   # se pinta el cubo
                color = choice(colors) # Generar el color
                igv_utils.color_cube(color)
                n += 1
            glTranslatef(0, 0, 1)
        glTranslatef(1, 0, -z_size)
    
    #print(f"Se han pintado {n} cubos")
     
    # Restaurar la matriz MODELVIEW    
    glPopMatrix()


def density_ortho(x_size, y_size, z_size, density, colors):
    
    # Comprobar x_size, y_sixe, z_size, density
    if (x_size < 2) or (y_size < 2) or (z_size < 2) or (density < 0):
        print("Error en los parámetros de density_ortho")
        return
    
    # Preservar la matriz MODELVIEW
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
        
        
    # Cálculo de los puntos necesarios según la densidad
    max_cubes = x_size * y_size * z_size
    #print(f"posibles cubos = {x_size} x {y_size} x {z_size} = {max_cubes}")
    
    num_cubes = int((max_cubes * density) / 100)
    #print(f"{density}% de {max_cubes} = {num_cubes}")
    
    n = 0   # Contador para sumar el número de cubos
        
    for y in range(y_size):    
        for x in range(x_size):
            for z in range(z_size):
                if randint(0,100) < density:   # se pinta el cubo
                    color = choice(colors) # Generar el color
                    igv_utils.color_cube(color)
                    n += 1
                glTranslatef(0, 0, 1)
            glTranslatef(1, 0, -z_size)
        glTranslate(-x_size, 1, 0)
    
    #print(f"Se han pintado {n} cubos")
     
    # Restaurar la matriz MODELVIEW
    glPopMatrix()


def density_ortho(x_size, y_size, z_size, density, colors):
    
    # Comprobar x_size, y_sixe, z_size, density
    if (x_size < 2) or (y_size < 2) or (z_size < 2) or (density < 0):
        print("Error en los parámetros de density_ortho")
        return
    
    # Preservar la matriz MODELVIEW
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
               
    for y in range(y_size):    
        for x in range(x_size):
            for z in range(z_size):
                if randint(0,100) < density:   # se pinta el cubo
                    color = choice(colors) # Generar el color
                    igv_utils.color_cube(color)
                glTranslatef(0, 0, 1)
            glTranslatef(1, 0, -z_size)
        glTranslate(-x_size, 1, 0)
    
    glPopMatrix()


def empty_face_xz(x_size, z_size, colors):
    
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



def empty_pipe_y(x_size, y_size, z_size, colors):
    
    # Comprobar x_size, y_size, z_size
    if (x_size < 3) or (y_size < 3) or (z_size < 3):
        print("Error en los parámetros de empty_pipe_y")
        return
    
    # Preservar la matriz MODELVIEW
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()

    for y in range(y_size):
        empty_face_xz(x_size, z_size, colors)
        glTranslatef(0,1,0)
        
    # Restaurar la matriz MODELVIEW
    glPopMatrix()


def tree(color_trunk, color_top):
    
    glMatrixMode(GL_MODELVIEW)
    
    glPushMatrix()
    empty_ortho(10, 50, 10, color_trunk)
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(-15,35,-15)
    density_ortho(40, 40, 40, 5, color_top)
    glPopMatrix()
    

def bench():

    # colores
    leg_colors = [black_5]
    bench_colors = dark_brown_range
    
    # medidas de las patas
    leg_width = 1      # ancho de la pata
    leg_height = 8     # alto de la pata
    
    # medidas del asiento
    seat_length = 40
    seat_width = 10
    seat_height = 2
    
    # medidas del respaldo
    back_width = 2
    back_height = 4
    back_gap = 2
    
    # medidas de las barras
    bar_length = 2
    bar_width = 1    
    
    
    def legs():
        
        glPushMatrix()
        
        solid_ortho(leg_width, leg_height, leg_width, leg_colors)    # pata trasera izquierda
        
        glTranslatef(0, 0, seat_width-leg_width)
        solid_ortho(leg_width, leg_height, leg_width, leg_colors)    # pata delantera izquierda
        
        glTranslatef(seat_length-leg_width, 0, 0)
        solid_ortho(leg_width, leg_height, leg_width, leg_colors)    # pata delantera derecha
        
        glTranslatef(0, 0, -(seat_width-leg_width))
        solid_ortho(leg_width, leg_height, leg_width, leg_colors)    # pata trasera derecha
        
        glPopMatrix()
        
    def seat():

        glPushMatrix()
        
        glTranslatef(0, leg_height, 0)
        solid_ortho(seat_length, seat_height, seat_width, bench_colors)
        
        glPopMatrix()
        
    def back():

        glPushMatrix()
        
        glTranslatef(0, leg_height+ seat_height+back_gap, 0) 
        solid_ortho(seat_length, back_height, back_width, bench_colors)
        
        glTranslatef(0, back_height+back_gap, 0)
        solid_ortho(seat_length, back_height, back_width, bench_colors)
        
        glTranslatef(int(seat_length*0.2), -(back_height+2*back_gap+seat_height), -1)
        solid_ortho(bar_length, 2*back_height+2*back_gap+seat_height +1, bar_width, leg_colors)
        
        glTranslatef(int(seat_length*0.6), 0, 0)
        solid_ortho(bar_length, 2*back_height+2*back_gap+seat_height +1, bar_width, leg_colors)  
        
        glPopMatrix()

    glMatrixMode(GL_MODELVIEW)
    legs()
    seat()
    back()


def pyramid(size, colors):
    
    # Comprobar size
    if (size < 3):
        print("Error en los parámetros de pyramid")
        return

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    
    # Si el lado es par se le suma 1 para hacerlo impar y hacer que la cúspide sea un cubo
    if (size % 2) == 0:
        actual_size = size + 1
    else:
        actual_size = size
        
    current_size = actual_size   # current_size es el lado del piso actual
 
    while (current_size >= 3):  
        empty_face_xz(current_size, current_size, colors)
        glTranslatef(1,1,1)
        current_size -= 2     

    # Cubo correspodiente a la cúspide de la pirámide
    color = colors[randint(0, len(colors)-1)]  # Generar el color
    igv_utils.color_cube(color)

    
    glPopMatrix()

def regalo():
    # Cuerpo regalo
    
    glPushMatrix()
    #glTranslatef(0,10,-2)
    empty_ortho(15, 15, 15, light_grey_range) # Caja color gris 
    glPopMatrix()
    glPushMatrix()
    glTranslatef(6,0,15)
    solid_face_xy(3, 16, dark_red_range) #lazo rojo frente
    glPopMatrix()
    glPushMatrix()
    glTranslatef(6,15,0)
    solid_face_xz(3, 16, dark_red_range) #lazo rojo arriba atrás al frente
    glPopMatrix()
    glPushMatrix()
    glTranslatef(6,0,-1)
    solid_face_xy(3, 16, dark_red_range) #lazo rojo trasera
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0,15,6)
    solid_face_xz(16, 3, dark_red_range) #lazo rojo arriba izquierda a derecha
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(-1,0,6)
    solid_face_yz(16, 3, dark_red_range) #lazo rojo lado izquierdo
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(15,0,6)
    solid_face_yz(16, 3, dark_red_range) #lazo rojo lado
    glPopMatrix()

    def tnt():
        # Cuerpo TNT
        glPushMatrix()
        
        # Se crea la caja de dinamita con piezas de empthy_ortho()
        empty_ortho(16, 6, 16, dark_red_range) # TNT color rojo inferior
        glTranslatef(0,6,0)
        empty_ortho(16, 6, 16, light_grey_range) # TNT color gris 
        glTranslatef(0,6,0)
        empty_ortho(16, 6, 16, dark_red_range) # TNT color rojo inferior
          
        glPopMatrix()
        letras()
    
def letras():

    # Primera letra T frente
    
    glPushMatrix()
    glTranslatef(2,10,16)
    solid_ortho(3,1,1,[black_5,black_5,black_5,black_5,black_5])
    glPopMatrix()

    glPushMatrix()
    glTranslatef(3,7,16)
    solid_ortho(1,3,1,[black_5,black_5,black_5,black_5,black_5])
    glPopMatrix()

    # Letra N frente
    
    glPushMatrix()
    glTranslatef(6,7,16)
    solid_ortho(1,4,1,[black_5,black_5,black_5,black_5,black_5])
    glPopMatrix()

    glPushMatrix()
    glTranslatef(7,9,16)
    solid_ortho(1,1,1,[black_5,black_5,black_5,black_5,black_5])
    glPopMatrix()

    glPushMatrix()
    glTranslatef(8,8,16)
    solid_ortho(1,1,1,[black_5,black_5,black_5,black_5,black_5])
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(9,7,16)
    solid_ortho(1,4,1,[black_5,black_5,black_5,black_5,black_5])
    glPopMatrix()

    # Segunta letra T frente
    
    glPushMatrix()
    glTranslatef(11,10,16)
    solid_ortho(3,1,1,[black_5,black_5,black_5,black_5,black_5])
    glPopMatrix()

    glPushMatrix()
    glTranslatef(12,7,16)
    solid_ortho(1,3,1,[black_5,black_5,black_5,black_5,black_5])
    glPopMatrix()

    # Primera letra T trasera
    
    glPushMatrix()
    glTranslatef(2,10,-1)
    solid_ortho(3,1,1,[black_5,black_5,black_5,black_5,black_5])
    glPopMatrix()

    glPushMatrix()
    glTranslatef(3,7,-1)
    solid_ortho(1,3,1,[black_5,black_5,black_5,black_5,black_5])
    glPopMatrix()

    # Letra N trasera
    
    glPushMatrix()
    glTranslatef(6,7,-1)
    solid_ortho(1,4,1,[black_5,black_5,black_5,black_5,black_5])
    glPopMatrix()

    glPushMatrix()
    glTranslatef(7,8,-1)
    solid_ortho(1,1,1,[black_5,black_5,black_5,black_5,black_5])
    glPopMatrix()

    glPushMatrix()
    glTranslatef(8,9,-1)
    solid_ortho(1,1,1,[black_5,black_5,black_5,black_5,black_5])
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(9,7,-1)
    solid_ortho(1,4,1,[black_5,black_5,black_5,black_5,black_5])
    glPopMatrix()

    # Segunta letra T trasera
    
    glPushMatrix()
    glTranslatef(11,10,-1)
    solid_ortho(3,1,1,[black_5,black_5,black_5,black_5,black_5])
    glPopMatrix()

    glPushMatrix()
    glTranslatef(12,7,-1)
    solid_ortho(1,3,1,[black_5,black_5,black_5,black_5,black_5])
    glPopMatrix()

    def ventana():
        # Ventana
        glPushMatrix()
        solid_ortho(3, 3, 1, [blue_2, blue_2, blue_2, blue_2, blue_2])
        glPopMatrix()

def tejado(x_size, z_size, colores):

    #glMatrixMode(GL_MODELVIEW)
    glPushMatrix()

    # pintamos una piramide con la funcion solid_face_xz()
    x_size += 1
    z_size += 1
    for z in range(z_size, 1, -2):
        solid_face_xz(x_size, z_size, colores)
        x_size = x_size - 4
        z_size = z_size - 4
        glTranslatef(2, 1, 2)
    
    glPopMatrix()

def casa():
    # cuerpo del golem 
    glPushMatrix()
    empty_ortho(11, 11, 11, light_grey_range)
    glPopMatrix()

def suelo():
    # Base inferior, suelo verde (cesped) 
    glPushMatrix()
    # con color_creeper para ver su ubicación diferenciada
    solid_ortho(100, 1, 25, light_grey_range)
    glPopMatrix()

def bateria():
    # Dibujamos la batería
    
    #Bloque inferior
    
    glPushMatrix()
    empty_ortho(20, 12, 12, dark_brown_range)  # Cuerpo alto y delgado
    #glPopMatrix()
    glTranslatef(0, 12, 0)
    #Bloque superior
    
    #glPushMatrix()
    empty_ortho(20, 5, 12, light_grey_range)  # Cuerpo alto y delgado
    glPopMatrix()

    # Pintamos los bornes y sígnos
    #glTranslatef(4, 14, 12)
    
    #Signo +
    glPushMatrix()
    glTranslatef(4, 14, 12)
    solid_ortho(3,1,1,light_grey_range)
    glTranslatef(1, -1, 0)
    solid_ortho(1,3,1,light_grey_range)
    glPopMatrix()

    #Signo -
    glPushMatrix()
    glTranslatef(13, 14, 12)
    solid_ortho(3,1,1,light_grey_range)
    glPopMatrix()

    #Bornes superiores
    # Borne izquierdo
    glPushMatrix()
    glTranslatef(6, 17, 6)
    solid_ortho(2,1,1,light_grey_range)
    glTranslatef(0, 0, 1)
    solid_ortho(2,1,1,light_grey_range)
    glPopMatrix()

    # Borne izquierdo
    glPushMatrix()
    glTranslatef(12, 17, 6)
    solid_ortho(2,1,1,light_grey_range)
    glTranslatef(0, 0, 1)
    solid_ortho(2,1,1,light_grey_range)
    glPopMatrix()

def punto():
    glPushMatrix()
    #glTranslatef(6,4,6)
    solid_ortho(2, 1, 2, color_zapato)
    glTranslatef(0,0,1)
    solid_ortho(2, 1, 2, color_zapato)
    glPopMatrix()

def barra():
    glPushMatrix()
    #glTranslatef(6,4,6)
    solid_ortho(2, 1, 12, color_zapato)
    #glTranslatef(0,0,1)
    #solid_ortho(2, 1, 2, color_zapato)
    glPopMatrix()

def ficha():

    # Se usa solid_ortho porque no hay manera de construirlo de forma hueca
    # Cuerpo de la ficha

    # Base de la ficha
    glPushMatrix()
    solid_ortho(30, 2, 14, color_zapato)
    glTranslatef(0,2,0)
    solid_ortho(30, 2, 14, light_grey_range)
    glPopMatrix()

    # Elementos de la ficha
    # Barra central en posición x=14 con z=2 e y=1
    # Punto simple izquierda en x=6 con z=2 e y=1
    # Punto simple izquierda en x=7 con z=2 e y=1
    #glPushMatrix()
    glTranslatef(6,4,6)
    punto()

    glTranslatef(8,0,-5)
    barra()

    glTranslatef(4,0, 1)
    punto()
    glTranslatef(7,0, 8)
    punto()
    '''
    solid_ortho(2, 1, 2, color_zapato)
    glTranslatef(0,0,1)
    solid_ortho(2, 1, 2, color_zapato)
    glPopMatrix()
    '''

def carril_bici():
    glPushMatrix()
    solid_ortho(200, 1, 15, light_green_range)
    glPopMatrix()

def carretera():
    glPushMatrix()
    solid_ortho(200, 1, 40, dark_grey_range)
        # Línea discontinua central (en z ~ mitad de 40)
    dash_len = 6
    gap = 6
    z_line = 19   # centro aprox (0..39)
    x = 0
    while x < 200:
        glPushMatrix()
        glTranslatef(x, 1, z_line)             # y=1 para quedar encima del asfalto
        solid_ortho(dash_len, 1, 2, [grey_1])  # bloque blanco
        glPopMatrix()
        x += dash_len + gap
    glPopMatrix()



def farola():
    """
    Farola construida con solid_ortho, empty_ortho y solid_face_xz,
 
      Parte      Funcion         Medidas (x, y, z)
      Pedestal   empty_ortho     6 x 4 x 6
      Reductor   solid_ortho     4 x 2 x 4   (escalon intermedio hacia el fuste)
      Fuste      solid_ortho     2 x 20 x 2
      Brazo      solid_face_xz   10 x 2      (horizontal en +X sobre la cima del fuste)
      Cuello     solid_ortho     2 x 4 x 2   (baja del extremo del brazo)
      Linterna   empty_ortho     6 x 6 x 4   (cuerpo luminoso)
    """
 
    # Medidas de cada parte
    ped_w = 6;  ped_h = 4;  ped_d = 6     # pedestal
    red_w = 4;  red_h = 2;  red_d = 4     # reductor
    fus_w = 2;  fus_h = 20; fus_d = 2     # fuste
    bra_l = 10; bra_d = 2                 # brazo (longitud en X, profundidad en Z)
    cue_w = 2;  cue_h = 4;  cue_d = 2     # cuello
    lin_w = 6;  lin_h = 6;  lin_d = 4     # linterna
 
    def pedestal():
        glPushMatrix()
        empty_ortho(ped_w, ped_h, ped_d, light_grey_range)
        glPopMatrix()
 
    def reductor():
        # Sube al techo del pedestal y centra en XZ el escalon
        glPushMatrix()
        glTranslatef(1, ped_h, 1)
        solid_ortho(red_w, red_h, red_d, light_grey_range)
        glPopMatrix()
 
    def fuste():
        # Sube al techo del reductor y centra en XZ la columna
        glPushMatrix()
        glTranslatef(2, ped_h + red_h, 2)
        solid_ortho(fus_w, fus_h, fus_d, light_grey_range)
        glPopMatrix()
 
    def brazo():
        # Barra horizontal que sale en +X desde la cima del fuste
        glPushMatrix()
        glTranslatef(2, ped_h + red_h + fus_h, 2)
        solid_face_xz(bra_l, bra_d, light_grey_range)
        glPopMatrix()
 
    def cuello():
        # Baja verticalmente desde el extremo del brazo
        glPushMatrix()
        glTranslatef(2 + bra_l - cue_w,
                     ped_h + red_h + fus_h - cue_h,
                     2)
        solid_ortho(cue_w, cue_h, cue_d, light_grey_range)
        glPopMatrix()
 
    def linterna():
        # Caja luminosa colgada del cuello
        glPushMatrix()
        glTranslatef(2 + bra_l - cue_w - 1,
                     ped_h + red_h + fus_h - cue_h - lin_h,
                     2 - 1)
        empty_ortho(lin_w, lin_h, lin_d, light_yellow_range)
        glPopMatrix()
 
    pedestal()
    reductor()
    fuste()
    brazo()
    cuello()
    linterna()
