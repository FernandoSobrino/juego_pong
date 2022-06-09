import pygame

class Pong:

    _ALTO = 200
    _ANCHO = 320

    def __init__(self):
        print("Construyendo un objeto pong")
        pygame.init()
        self.pantalla = pygame.display.set_mode((self._ANCHO,self._ALTO))

    def bucle_principal(self):
        print("Estoy en el bucle principal")
        while True:
            pygame.display.flip()

if __name__ == "__main__":
    juego = Pong()
    juego.bucle_principal()
