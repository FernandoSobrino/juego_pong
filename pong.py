from random import randint
import pygame

ALTO = 480
ALTO_PALETA = 80
ANCHO = 640
ANCHO_PALETA = 5
COLOR_BLANCO = (255,255,255)
COLOR_PANTALLA = (0,128,0)
FPS = 60
MARGEN_LATERAL = 30
PUNTOS_PARTIDA = 3
TAMANIO_PELOTA = 6
VEL_MAX_PELOTA = 5
VELOCIDAD_PALETA = 5

class Paleta(pygame.Rect):
    ARRIBA = True
    ABAJO = False

    def __init__(self,x,y):
        super(Paleta,self).__init__(x,y, ANCHO_PALETA,ALTO_PALETA)
        self.velocidad = VELOCIDAD_PALETA

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
    
        valido_posicion_x = False
        while not valido_posicion_x:
            self.velocidad_x = randint(-VEL_MAX_PELOTA,VEL_MAX_PELOTA)
            valido_posicion_x = self.velocidad_x != 0
        self.velocidad_y = randint(-VEL_MAX_PELOTA,VEL_MAX_PELOTA)

    def mover_pelota(self):
        self.y = self.y + self.velocidad_y
        self.x = self.x + self.velocidad_x
        if self.y < 0:                              #PARA QUE LA BOLA NO SE SALGA DE ARRIBA
            self.y = 0
            self.velocidad_y = - self.velocidad_y
        if self.y > ALTO - TAMANIO_PELOTA:          #PARA QUE LA BOLA NO SE SALGA DE ABAJO
            self.y = ALTO - TAMANIO_PELOTA
            self.velocidad_y = - self.velocidad_y

class Marcador:
    def __init__(self):
        self.inicializar()

    def comprobar_ganador(self):
        if self.partida_finalizada:
            return True
        if self.valor[0] == PUNTOS_PARTIDA:
            print("Ha ganado el jugador 1")
            self.partida_finalizada = True
        elif self.valor[1] == PUNTOS_PARTIDA:
            print("Ha ganado el jugador 2")
            self.partida_finalizada = True
        return self.partida_finalizada

    def inicializar(self):
        self.valor = [0,0]
        self.partida_finalizada = False

class Pong:

    
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

        self.marcador = Marcador()
           

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
                    if evento.key == pygame.K_r:
                        print("Nueva partida")
                        self.marcador.inicializar()
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
            
            if not self.marcador.comprobar_ganador():
                self.pelota.mover_pelota()
                self.colision_paletas()
                self.comprobar_punto()

            self.pantalla.fill(COLOR_PANTALLA)
                   
            #Dibujo de las dos palas y de la pelota
            pygame.draw.rect(self.pantalla,COLOR_BLANCO,self.jugador1)
            pygame.draw.rect(self.pantalla,COLOR_BLANCO,self.jugador2)
            pygame.draw.rect(self.pantalla,COLOR_BLANCO,self.pelota)
            
            #Dibujo del campo de tenis 
            self.pintar_campo()

            #Refresco de pantalla
            pygame.display.flip()
            self.clock.tick(FPS)
    
    def colision_paletas(self):
        if self.jugador1.colliderect(self.pelota) or self.jugador2.colliderect(self.pelota):
            self.pelota.velocidad_x = -self.pelota.velocidad_x 
            self.pelota.velocidad_y = randint(-VEL_MAX_PELOTA,VEL_MAX_PELOTA)

    def comprobar_punto(self):
            if self.pelota.x < 0:
                self.marcador.valor[1] = self.marcador.valor[1] + 1
                print(f"El nuevo marcador es {self.marcador.valor}")
                self.pelota.velocidad_x = randint(-VEL_MAX_PELOTA,-1)
                self.iniciar_punto()
                
            elif self.pelota.x > ANCHO:
                self.marcador.valor[0] = self.marcador.valor[0] + 1
                print(f"El nuevo marcador es {self.marcador.valor}")
                self.pelota.velocidad_x = randint(-VEL_MAX_PELOTA,-1)
                self.iniciar_punto()
                
            self.marcador.comprobar_ganador()

    def iniciar_punto(self):
        self.pelota.x = (ANCHO - TAMANIO_PELOTA)/2
        self.pelota.y = (ALTO - TAMANIO_PELOTA)/2
        self.pelota.velocidad_y = randint(-VEL_MAX_PELOTA,VEL_MAX_PELOTA)


    def pintar_campo(self):
        #Este es el método para el que luego llamamos para dibujar el campo
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


