from random import randint
import pygame

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
        self.velocidad = 4

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
        self.y = self.y + self.velocidad_x
        self.x = self.x + self.velocidad_y



#class Linea(pygame.Rect):
    #pass

class Pong:

    _ANCHO_RED = 5
    _COLOR_PANTALLA = (0,128,0)
    _COLOR_BLANCO = (255,255,255)

    def __init__(self):
        print("Construyendo un objeto pong")
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO,ALTO))
        self.clock = pygame.time.Clock()
        self.pantalla.fill(self._COLOR_PANTALLA)

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
            self.pantalla.fill(self._COLOR_PANTALLA)
                   
            
            pygame.draw.rect(self.pantalla,self._COLOR_BLANCO,self.jugador1)
            pygame.draw.rect(self.pantalla,self._COLOR_BLANCO,self.jugador2)
            pygame.draw.rect(self.pantalla,self._COLOR_BLANCO,self.pelota)
            
            #Dibujo del campo de tenis 
            self.pintar_campo()

            #Refresco de pantalla
            pygame.display.flip()
            self.clock.tick(120)

    #Este es el método para el que luego llamamos para dibujar el campo
    def pintar_campo(self):
        for posicion in range(0, ALTO,45):
                pygame.draw.line(self.pantalla,self._COLOR_BLANCO,
                                (ANCHO/2, posicion),
                                (ANCHO/2,posicion + 25))
        pygame.draw.rect(self.pantalla,self._COLOR_BLANCO,(70,45,500,390),2)
        pygame.draw.line(self.pantalla,self._COLOR_BLANCO,(70,100),(567,100))
        pygame.draw.line(self.pantalla,self._COLOR_BLANCO,(70,380),(567,380))
        pygame.draw.line(self.pantalla,self._COLOR_BLANCO,(175,100),(175,380))
        pygame.draw.line(self.pantalla,self._COLOR_BLANCO,(470,100),(470,380))
        pygame.draw.line(self.pantalla,self._COLOR_BLANCO,(175,240),(470,240))
            
if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal()


