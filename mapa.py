import os
#Variables para crear un juego
WITH_MAPA = 25
HEIHT_MAPA= 15
espacio_vacio = "   "
espacio_lleno= "[ ]"

coordenada_personaje = [8,10]
personaje = "🡹"

def cargar_mapa(movimiento_personaje):
    os.system('cls')
    if movimiento_personaje == 'w':
        personaje = " ▲ "
        coordenada_personaje[0] -= 1
    elif movimiento_personaje == 's':
        personaje = " ▼ "
        coordenada_personaje[0] += 1
    elif movimiento_personaje == 'a':
        personaje = " ◀ "
        coordenada_personaje[1] -= 1
    elif movimiento_personaje == 'd':
        personaje = " ▶ "
        coordenada_personaje[1] += 1


    print("+"  + "-"*75 + "+")
    for cada_fila in range(HEIHT_MAPA):
        print("|", end= "")
        for cada_bloque in range(WITH_MAPA):
            if(coordenada_personaje[0] == cada_fila and coordenada_personaje[1]== cada_bloque):
                print(f"{personaje}", end= "")
            else:
                print(espacio_vacio, end= "")

        print("|")
    print("+"  + "-"*75 + "+")
