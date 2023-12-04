# Logaritmo del juego piedra papel o tijeras de dos jugadores en python

# import random es  un módulo incorporado que proporciona funciones para trabajar con números aleatorios, lo utilizare para realizar las actividades de la pc
import random

# funcion del juego
def jugar():
    
    # Creo la variable usuario y le pido q ingrese su eleccion por un input
    usuario = input("Elige una opción según el número: 1-Piedra, 2-Papel, 3-Tijeras")
    usuario = usuario.lower()
    
    #Creo los elementos para que la computadora eliga al azar
    elementos = ['1','2','3']
    
    # Creo la variable pc
    pc = random.choice(elementos)
    
    # Condicion que si eligen lo mismo es un empate
    if usuario == pc:
        return "Los dos eligieron {}".format(pc)
    
    # Condicion de ganador, si la computadora o el usuario es ganador retorna un true
    if is_ganador(usuario,pc):
        return "Haz elegido {} y el oponente eligio {}. Haz ganado".format(usuario,pc)
    
    # En caso de perder
    return "Haz elegido {} y el oponente eligio {}. Haz perdido".format(usuario,pc)
    
# Funcion del juego para el ganador    
def is_ganador(jugador, oponente):
    # Devuelve True si el jugador es el ganador
    # Condiciones para ganar: 1-Piedra > 3-Tijera, 3-Tijera > 2-Papel, 2-Papel > 1-Piedra
    if(jugador == '1' and oponente == '3') or (jugador == '3' and oponente == '2') or (jugador == '2' and oponente == '1'):
        return True
    #Si no ganamos retorna false
    return False

if __name__ == "__name__" :
    print(jugar())