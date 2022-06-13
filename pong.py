import pygame

ALTO_PALETA = 80
ANCHO_PALETA = 5


class Paleta(pygame.Rect):
    ARRIBA = True
    ABAJO = False

    def __init__(self,x,y):
        super(Paleta,self).__init__(x,y, ANCHO_PALETA,ALTO_PALETA)
        self.velocidad = 3

    def mover_paleta(self,direccion):
        if direccion == self.ARRIBA:
            self.y = self.y - self.velocidad
        else:
            self.y = self.y + self.velocidad
        pass



class Linea(pygame.Rect):
    pass

class Pong:

    _ANCHO = 640
    _ALTO = 480
    _MARGEN_LATERAL = 30
    _ANCHO_RED = 5
    _COLOR_PANTALLA = (0,128,0)
    _COLOR_BLANCO = (255,255,255)

    def __init__(self):
        print("Construyendo un objeto pong")
        pygame.init()
        self.pantalla = pygame.display.set_mode((self._ANCHO,self._ALTO))
        self.pantalla.fill(self._COLOR_PANTALLA)
        self.jugador1 = Paleta(
            self._MARGEN_LATERAL,               #COORDENADA X (LEFT)
            (self._ALTO-ALTO_PALETA)/2)         #COORDENADA Y (TOP)
                                      
        
        self.jugador2 = Paleta(
            self._ANCHO - self._MARGEN_LATERAL - ANCHO_PALETA,
            (self._ALTO-ALTO_PALETA)/2)
           

        self.linea = Linea(self._ANCHO/2,0,self._ANCHO_RED,self._ALTO)

    

    def bucle_principal(self):
        print("Estoy en el bucle principal")
        salir_juego = False
        while not salir_juego:
            eventos = pygame.event.get()
            for evento in eventos:
                estado_teclas = pygame.key.get_pressed()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        salir_juego = True
                if evento.type == pygame.QUIT:
                    salir_juego = True
                
            if estado_teclas[pygame.K_a]:
                self.jugador1.mover_paleta(Paleta.ARRIBA)
            if estado_teclas[pygame.K_z]:
                self.jugador1.mover_paleta(Paleta.ABAJO)
            if estado_teclas[pygame.K_UP]:
                self.jugador2.mover_paleta(Paleta.ARRIBA)
            if estado_teclas[pygame.K_DOWN]:
                    self.jugador2.mover_paleta(Paleta.ABAJO)
                
            self.pantalla.fill(self._COLOR_PANTALLA)
                   
            
            pygame.draw.rect(self.pantalla,self._COLOR_BLANCO,self.jugador1)
            pygame.draw.rect(self.pantalla,self._COLOR_BLANCO,self.jugador2)
            #pygame.draw.rect(self.pantalla,self._BLANCO,self.linea)

            for posicion in range(0, self._ALTO,45):
                pygame.draw.line(self.pantalla,self._COLOR_BLANCO,
                                (self._ANCHO/2, posicion),
                                (self._ANCHO/2,posicion + 25))
                

            #Dibujo del campo de tenis (molaría llevarlo a una función)
            
            pygame.draw.rect(self.pantalla,self._COLOR_BLANCO,(70,45,500,390),2)
            pygame.draw.line(self.pantalla,self._COLOR_BLANCO,(70,100),(567,100))
            pygame.draw.line(self.pantalla,self._COLOR_BLANCO,(70,380),(567,380))
            pygame.draw.line(self.pantalla,self._COLOR_BLANCO,(175,100),(175,380))
            pygame.draw.line(self.pantalla,self._COLOR_BLANCO,(470,100),(470,380))
            pygame.draw.line(self.pantalla,self._COLOR_BLANCO,(175,240),(470,240))
            

            pygame.display.flip()
            
            
if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal()


