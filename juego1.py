import os
import readchar 
from mapa import cargar_mapa

def juego1():
    # Iniciar Juego
    tecla = readchar.readchar()

    if tecla == 'w':
        cargar_mapa(tecla)
    if tecla == 'a':
        cargar_mapa(tecla)
    elif tecla == 's':
        cargar_mapa(tecla)
    elif tecla == 'd':
        cargar_mapa(tecla)

while True:
    juego1()