import sys
import pygame

pygame.init()

width = 400
height = 500
surface = pygame.display.set_mode((width, height)) # superficies esto define la ventana 

# almacenamos la superfici en una variable 'surface'

pygame.display.set_caption("Hola mundo!!") # este es el titulo de la ventana 

#----------------------------------------------------------------
# colores usando la clase Color
# el resive argumentos en RGB 
red = pygame.Color(255,0,0)  # nota .Color la c es en mayuscula

# o por medio de tuplas
my_color = (253,58,94)   # esta tupla genera un rgb tambien 
#---------------------------------------------------------------

while True:       # este while estara a la escucha de todo los eventos 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # el evento QUIT la ventana cerrara
            pygame.quit()
            sys.exit()
#-------------------------------
# dentro del bucle se coloca el color 
# tanto una tupla como la libreria color van dentro de fill()
    surface.fill(my_color)           #  .fill() resive un parameto y es el que pinta la pantalla
    pygame.display.update()     # el .updata() es para que la pantalla se actualice y se ve el cambio 

