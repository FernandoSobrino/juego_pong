import pygame

class Paleta(pygame.Rect):
    pass

class Pong:

    _ANCHO = 640
    _ALTO = 480
    _MARGEN_LATERAL = 40
    _ANCHO_PALETA = 5
    _ALTO_PALETA = _ALTO / 5
    _COLOR_PANTALLA = (0,210,0)






    def __init__(self):
        print("Construyendo un objeto pong")
        pygame.init()
        self.pantalla = pygame.display.set_mode((self._ANCHO,self._ALTO))
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

    def bucle_principal(self):
        print("Estoy en el bucle principal")
        salir_juego = False
        while not salir_juego:
            eventos = pygame.event.get()
            for evento in eventos:
                if evento.type == pygame.QUIT:
                    salir_juego = True
            self.pantalla.fill(self._COLOR_PANTALLA)
            pygame.draw.rect(self.pantalla,(255,255,255),self.jugador1)
            pygame.draw.rect(self.pantalla,(255,255,255),self.jugador2)
            pygame.draw.line(self.pantalla,(255,255,255),(self._ANCHO/2,self._ALTO),(self._ANCHO/2,0))
            pygame.display.flip()
            
            
if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal()


