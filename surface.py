import sys
import pygame

pygame.init()

width = 400
height = 500
surface = pygame.display.set_mode((width, height)) # superficies esto define la ventana 

# almacenamos la superfici en una variable 'surface'

pygame.display.set_caption("Hola mundo!!") # este es el titulo de la ventana 

#----------------------------------------------------------------
# colores
# el resive argumentos en RGB 
red = pygame.Color(255,0,0)  # nota .Color la c es en mayuscula


while True:       # este while estara a la escucha de todo los eventos 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # el evento QUIT la ventana cerrara
            pygame.quit()
            sys.exit()
#-------------------------------
# dentro del bucle se coloca el color 
    surface.fill(red)
    pygame.display.update()

