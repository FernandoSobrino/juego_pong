import pygame


class Paleta(pygame.Rect):
    pass

class Linea(pygame.Rect):
    pass

class Pong:

    _ANCHO = 640
    _ALTO = 480
    _MARGEN_LATERAL = 30
    _ANCHO_PALETA = 5
    _ANCHO_RED = 5
    _ALTO_PALETA = _ALTO / 5
    _COLOR_PANTALLA = (0,128,0)
    _BLANCO = (255,255,255)

    def __init__(self):
        print("Construyendo un objeto pong")
        pygame.init()
        self.pantalla = pygame.display.set_mode((self._ANCHO,self._ALTO))
        self.pantalla.fill(self._COLOR_PANTALLA)
        self.jugador1 = Paleta(
            self._MARGEN_LATERAL,               #COORDENADA X (LEFT)
            (self._ALTO-self._ALTO_PALETA)/2,   #COORDENADA Y (TOP)
            self._ANCHO_PALETA,                 #ANCHO (WIDTH)
            self._ALTO_PALETA)                  #ALTO (HEIGHT)              
        
        self.jugador2 = Paleta(
            self._ANCHO - self._MARGEN_LATERAL - self._ANCHO_PALETA,
            (self._ALTO-self._ALTO_PALETA)/2,
            self._ANCHO_PALETA, 
            self._ALTO_PALETA)

        self.linea = Linea(self._ANCHO/2,0,self._ANCHO_RED,self._ALTO)

    

    def bucle_principal(self):
        print("Estoy en el bucle principal")
        salir_juego = False
        while not salir_juego:
            eventos = pygame.event.get()
            for evento in eventos:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        salir_juego = True
                if evento.type == pygame.QUIT:
                    salir_juego = True
            
            pygame.draw.rect(self.pantalla,self._BLANCO,self.jugador1)
            pygame.draw.rect(self.pantalla,self._BLANCO,self.jugador2)
            pygame.draw.rect(self.pantalla,self._BLANCO,self.linea)

            #Dibujo del campo de tenis (molaría llevarlo a una función)
            pygame.draw.rect(self.pantalla,self._BLANCO,(70,45,500,390),2)
            pygame.draw.line(self.pantalla,self._BLANCO,(70,100),(567,100))
            pygame.draw.line(self.pantalla,self._BLANCO,(70,380),(567,380))
            pygame.draw.line(self.pantalla,self._BLANCO,(175,100),(175,380))
            pygame.draw.line(self.pantalla,self._BLANCO,(470,100),(470,380))
            pygame.draw.line(self.pantalla,self._BLANCO,(175,240),(470,240))
        

            pygame.display.flip()
            
            
if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal()


