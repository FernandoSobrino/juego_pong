from random import randint
import pygame

COLOR_PANTALLA = (0,128,0)
COLOR_BLANCO = (255,255,255)
ALTO_PALETA = 80
ANCHO_PALETA = 5
ANCHO = 640
ALTO = 480
MARGEN_LATERAL = 30
TAMANIO_PELOTA = 6

class Paleta(pygame.Rect):
    ARRIBA = True
    ABAJO = False

    def __init__(self,x,y):
        super(Paleta,self).__init__(x,y, ANCHO_PALETA,ALTO_PALETA)
        self.velocidad = 5

    def mover_paleta(self,direccion):
        if direccion == self.ARRIBA:
            self.y = self.y - self.velocidad
            if self.y < 0:
                self.y = 0
        else:
            self.y = self.y + self.velocidad
            if self.y > ALTO - ALTO_PALETA:
                self.y = ALTO - ALTO_PALETA
        
class Pelota(pygame.Rect):

    def __init__(self):
        super(Pelota,self).__init__((ANCHO-TAMANIO_PELOTA)/2,
                                    (ALTO-TAMANIO_PELOTA)/2, 
                                    TAMANIO_PELOTA,TAMANIO_PELOTA)
    
        self.velocidad_x = randint(-5,5)
        self.velocidad_y = randint(-5,5)

    def mover_pelota(self):
        self.y = self.y + self.velocidad_y
        self.x = self.x + self.velocidad_x
        if self.y < 0:                              #PARA QUE LA BOLA NO SE SALGA DE ARRIBA
            self.y = 0
            self.velocidad_y = - self.velocidad_y
        if self.y > ALTO - TAMANIO_PELOTA:          #PARA QUE LA BOLA NO SE SALGA DE ABAJO
            self.y = ALTO - TAMANIO_PELOTA
            self.velocidad_y = - self.velocidad_y


#class Linea(pygame.Rect):
    #pass

class Pong:

    _ANCHO_RED = 5
    
    def __init__(self):
        print("Construyendo un objeto pong")
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO,ALTO))
        self.clock = pygame.time.Clock()
        self.pantalla.fill(COLOR_PANTALLA)

        self.jugador1 = Paleta(
            MARGEN_LATERAL,               #COORDENADA X (LEFT)
            (ALTO-ALTO_PALETA)/2)         #COORDENADA Y (TOP)
                                      
        
        self.jugador2 = Paleta(
            ANCHO - MARGEN_LATERAL - ANCHO_PALETA,
            (ALTO-ALTO_PALETA)/2)

        self.pelota = Pelota()
           

        #self.linea = Linea(ANCHO/2,0,self._ANCHO_RED,ALTO)

    

    def bucle_principal(self):
        print("Estoy en el bucle principal")
        salir_juego = False
        while not salir_juego:
            eventos = pygame.event.get()
            estado_teclas = pygame.key.get_pressed()
            for evento in eventos:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        salir_juego = True
                if evento.type == pygame.QUIT:
                    salir_juego = True
        
        #Aquí tenemos creados los eventos que tienen que ver con pulsaciones de teclado    
            if estado_teclas[pygame.K_a]:
                self.jugador1.mover_paleta(Paleta.ARRIBA)
            if estado_teclas[pygame.K_z]:
                self.jugador1.mover_paleta(Paleta.ABAJO)
            if estado_teclas[pygame.K_UP]:
                self.jugador2.mover_paleta(Paleta.ARRIBA)
            if estado_teclas[pygame.K_DOWN]:
                    self.jugador2.mover_paleta(Paleta.ABAJO)
            self.pelota.mover_pelota()

            self.colision_paletas()


            self.pantalla.fill(COLOR_PANTALLA)
                   
            #Dibujo de las dos palas y de la pelota
            pygame.draw.rect(self.pantalla,COLOR_BLANCO,self.jugador1)
            pygame.draw.rect(self.pantalla,COLOR_BLANCO,self.jugador2)
            pygame.draw.rect(self.pantalla,COLOR_BLANCO,self.pelota)
            
            #Dibujo del campo de tenis 
            self.pintar_campo()

            #Refresco de pantalla
            pygame.display.flip()
            self.clock.tick(60)
    
   
    """
    Este es el método que comprueba la colisión de la pelota con una de las paletas
    y si es así le cambia la dirección a la pelota
    """
    def colision_paletas(self):
        if self.jugador1.colliderect(self.pelota) or self.jugador2.colliderect(self.pelota):
            self.pelota.velocidad_x = -self.pelota.velocidad_x + randint(-1,1)
            self.pelota.velocidad_y = randint(-5,5)



    #Este es el método para el que luego llamamos para dibujar el campo
    def pintar_campo(self):
        for posicion in range(0, ALTO,50):
            pygame.draw.line(self.pantalla,COLOR_BLANCO,
                                (ANCHO/2, posicion),
                                (ANCHO/2,posicion + 29))
        pygame.draw.rect(self.pantalla,COLOR_BLANCO,(70,45,500,390),2)
        pygame.draw.line(self.pantalla,COLOR_BLANCO,(70,100),(567,100))
        pygame.draw.line(self.pantalla,COLOR_BLANCO,(70,380),(567,380))
        pygame.draw.line(self.pantalla,COLOR_BLANCO,(175,100),(175,380))
        pygame.draw.line(self.pantalla,COLOR_BLANCO,(470,100),(470,380))
        pygame.draw.line(self.pantalla,COLOR_BLANCO,(175,240),(470,240))
            
if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal()


