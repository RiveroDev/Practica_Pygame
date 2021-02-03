import sys
import pygame

pygame.init()

width = 400
height = 500
surface = pygame.display.set_mode((width, height)) # superficies esto define la ventana 
# almacenamos la superfici en una variable 'surface'

pygame.display.set_caption("Hola mundo!!") # este es el titulo de la ventana 

#----------------------------------------------------------------
# se genra por medio de 2 formas 
# colores usando la clase Color
# el resive argumentos en RGB 
red = pygame.Color(255,0,0)  # nota .Color la c es en mayuscula

# o por medio de tuplas
my_color = (253,58,94)   # esta tupla genera un rgb tambien 
color2 = (154,174,95)
color3 = (0 , 143, 57)
#---------------------------------------------------------------

#--------------------------------------------------------------
# Uso de los rectangulos para manejo de iamgenes y coliciones
rect = pygame.Rect(100, 150, 120,60)  # posicion en x , posicion en y,  ancho , alto
rect.center = (width // 2 , height // 2)  # x , y .... son las coredenadas del centro del rectangulo de valores enteros 
 # esta propiedad recalcula en centro de la posicion del rectangulo 

# generamos otro rectangulo por medio de tuplas
rect2 = (100,100,80,40) # x ,y , ancho, alto

#Notas implortantes :
# si se crean rectangulos con tuplas no se pueden usar las propiedades de Rect()\
# es por esto que si se necesita usar un rectangulo con movimiento se crean con Rect()
# si los rectangulos vas a ses fijos sin movimiento se crean por medio de tuplas
#--------------------------------------------------------------------------

surface2 = pygame.Surface((200,200))   # esta es una nueva superficie
surface2.fill(color3)  # le agregamos un color 


# -------------------------------------------..

## esto sirve para cargar un archivo de musica 

pygame.mixer.music.load('<direccion del archivo mp3>')
pygame.mixer.music.play(2,0.0) ##  numero de vecer y el minuto donde queremos que empiese
# en este caso la cancion inicia desde el principio y se repetira 2veces
# si queremso que la cancion nunca temine colocamos como valo -1
#  
pygame.mixer.music.set_volume(1.0)#  Float   esto es volumen que comprender desde 0.0  a  1.0 
#otros metodos para la manipulacion de la musica 


#-----------------------------------
# para agregar una imagen .. tiene que ser png
imagen = pygame.image.load('imagenes/chibipikachu.png') #--> con este comando podemos cargar una imagen y al asigamos a una variable 
rect3 = imagen.get_rect()
rect3.center = (width // 2, height // 2)

#-----------------------------------------------------------------------
# colocar TEXTO 

font = pygame.font.Font('freesansbold.ttf',36) # la fuente , el tamaño
texto = font.render('Hola mundo', True, my_color) # el texto a escribir, true ,color 

# podemos us una fuente gurdada solo calocando su direccion ejemplo
#font = pygame.font.Font('<carpeta o ruta>/<nombre de la fuente>.ttf',<tamaño>)
#-----------------------
font3 = pygame.font.Font('freesansbold.ttf',46)
#-----------------------------------------------------------------------
# este ciclo white es el bucle que esta a la escucha de todos los eventos en pantalla
while True:       # este while estara a la escucha de todo los eventos 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # el evento QUIT la ventana cerrara
            pygame.quit()
            sys.exit()
#-------------------------------

    tiempo =  pygame.time.get_ticks()  # esta funcion noss retornara en mili segundos una variable de el tiempo trascurrido
    print(tiempo) # imprime en terminal para ver el tiempo
    # nota si dividimos en tiempo entre mil obtendremos los segundos ejemplo
    # tiempo =  pygame.time.get_ticks() // 1000 
#-----------------------------------------
# dentro del bucle se coloca el color 
# tanto una tupla como la libreria color van dentro de fill()
    surface.fill(my_color)           #  .fill() resive un parameto y es el que pinta la pantalla

#-----------------------------------------
# cargaamos la imagen
    surface.blit(imagen , rect3)  # cusamos el metodo , identificando la superficie y el .blit
    # luego cargamos los parametos de blit con imagen y cordenada donde se va a colocar

#--------------------------------------    
    rect = surface2.get_rect()  # optenemos las dimenciones de la superficie 2 
    rect.center = (width // 2 , height // 2)  # luego redimencionamos la pocisicion

# usar el modulo draw()
# se usa para dibujar en la superfici de la ventana 

    pygame.draw.rect(surface, red, rect)    # ventana a ejecuta, color , dimenciones del rectangulo
    pygame.draw.rect(surface, color2, rect2) # otro rectangulo 

    pygame.draw.circle(surface, color2,(45,45),51) # a parte de cual ventana dibuja y el color la primera tupla indica la 
    #posicion del centro del circulo y la otra indica el radio 
    pygame.draw.line(surface, color2, (63,63),(200,200), 20)      # son 2 tuplas una indica el inicio y al otra el fin de la line con 
    # cordenadas x1,y1 y x2,y2 , el ultimo valor indica el grosor de la lineas en pixels
    ##-----------
    # figura mas complejas usando el modulo poligon()
    pygame.draw.polygon(surface,color2,((0,400),(100,300),(200,400)))  # en la tupla se coloca las cordenadas de los puntos y cadal poligono que queremos crear

    pygame.draw.polygon(surface,color2,(
        (146,0),
        (291,106),
        (236,277),
        (56,277),
        (0,106)))    # esto es un poligono de 5 puntas



    surface.blit(surface2, (100,100))  # con esta comando creamo la superficie nuemro 2
    # usando el blit() donde decimos que es la superfies 2 y agregamos una tupla que es la posicion donde se dibujara

    pygame.draw.rect(surface2, color2, (100,50,80,40))

#------------------------------------------------------------------------   
    surface.blit(texto,(100,100))  #colocamos el texto  , el texto , cordenadas



    #---------------------------------------------------------
    seconds = pygame.time.get_ticks() // 1000
    text3 = font3.render(str(seconds), True, my_color)  # elsta funcion recive un str 
    rect = text3.get_rect()
    rect.center = (width // 2, height // 2)

    surface.blit(text3, rect)
    #---------------------------------------------------------------------------
    #----------------------------------------------------
    pygame.display.update()     # el .updata() es para que la pantalla se actualice y se ve el cambio 
    # este es la parte mas importante de la funcion



    

