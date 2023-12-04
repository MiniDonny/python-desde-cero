# Logaritmo del juego tateti

# ----------------------------------------------------------------------------------------------

# Primero se crea el "tablero", donde iran las "X" y las "O"
tablero = [ "-","-","-",
            "-","-","-",
            "-","-","-",
]
# ----------------------------------------------------------------------------------------------

# Variable global para el ganador del juego
ganador = None

# -----------------------------------------------------------------------------------------------

# Funcion del juego
def jugar():
    
    # llamo la variable global del ganador
    global ganador

    print("Empieza el juego")
    
    # llamo la funcion ver tablero
    ver_tablero()
    
    # Bucles para las jugadas
    # Primero bucle para el primer jugador
    # Maximo de jugadas que se pueden hacer es el 4 para el jugador 1
    for i in range(4):
        print("Turno del jugador 1 - X")
        valor="X"
        
        # Funcion jugada
        jugada(valor)
        
        #Esta funcion es para si ya alguien gano
        ganador()
        
        # Si no hubo ganador entonces le deja la jugada al segundo jugador. Tambien revisa la ultima jugada del jugador 1
        if ganador != "X" and i < 4 :
            
            # Bucle anidado para el segundo jugador
            # Las jugadas nesesarias para ganar es 3
            for j in range(3):
                print("Turno del jugador 2 - O")
                valor="O"
                
                #Funcion jugada
                jugada(valor)
                
                # Funcion para ver si gano
                ganador()
                
                # Si gano entonces que imprima un print
                if ganador == "O":
                    print("Felicidades 'jugador 2' Ganaste")
                # Rompe el siclo por que ya hubo un jugador
                break
            
        # En caso de que el primer jugador gane en la ultima jugada
        elif ganador == "X":
            print("Felicidades 'jugador 1' Ganaste")
            # Rompe el siclo por que ya hubo un jugador
            break
        
        # Else para el empate
        else:
            print("Empate")
            
# -----------------------------------------------------------------------------------------------

#Funcion para determinar el ganador
def ganador():
    # llamo a la variable global para que la reconozca
    global ganador 
    controlHorizontal() #Controla si esta lo mismo en horizontal
    controlVertical() #Controla si esta lo mismo en vertical
    controlDiagonal() #Controla si esta lo mismo en diagonal


# Funcion para controlar en forma Horizontal
def controlHorizontal():
    global ganador
    # Condicion en que el indice del tablero 0 1 y 2 sean iguales, es decir si son X o O
    if tablero[0] == tablero[1] == tablero[2] != "-":
        ganador == tablero[0]
    # Condicio en que el indice del tablero 3 4 y 5 sean iguales, es decir si son X o O
    elif tablero[3] == tablero[4] == tablero[5] != "-":
        ganador == tablero[3]
    # Condicio en que el indice del tablero 6 7 y 8 sean iguales, es decir si son X o O
    elif tablero[6] == tablero[7] == tablero[8] != "-":
        ganador == tablero[6]

# Funcion para controlar en forma Vertical
def controlVertical():
    global ganador
    # Condicion en que el indice del tablero 0 3 y 6 sean iguales, es decir si son X o O
    if tablero[0] == tablero[3] == tablero[6] != "-":
        ganador == tablero[0]
    # Condicio en que el indice del tablero 1 4 y 7 sean iguales, es decir si son X o O
    elif tablero[1] == tablero[4] == tablero[7] != "-":
        ganador == tablero[1]
    # Condicio en que el indice del tablero 2 5 y 8 sean iguales, es decir si son X o O
    elif tablero[2] == tablero[5] == tablero[8] != "-":
        ganador == tablero[2]

# Funcion para controlar en forma Diagonal
def controlDiagonal():
    global ganador
    # Condicion en que el indice del tablero 0 4 y 8 sean iguales, es decir si son X o O
    if tablero[0] == tablero[4] == tablero[8] != "-":
        ganador == tablero[0]
    # Condicio en que el indice del tablero 2 4 y 6 sean iguales, es decir si son X o O
    elif tablero[2] == tablero[4] == tablero[6] != "-":
        ganador == tablero[2]

# -----------------------------------------------------------------------------------------------

# Funcion de jugada que recibe un valor
def jugada(valor):
    
    #variable anoto para las anotaciones en el tablero 
    anoto = False
    
    # Un bucle While que sigue entrando mientras anoto es falso, para asi anotar en una casilla que este desocupada, si anono es true, sale del bucle y cambia el valor en la posicion
    while anoto == False:
        
        #Elige la posicion en el tablero
        posicion = int(input("Elegi una posicion del 1 al 9"))
        # Le restamos uno por que en la lista empieza en el cero y las elecciones que le damos empieza en 1
        posicion -= 1
        
        # Condicion si una posicion ya esta ocupada
        if tablero[posicion] == "-": # si la posicion es un "-" entonces esta libre
            anoto = True
        else:
            print("Esa posicion ya esta ocupada")
        
    # A esa posicion del tablero le pone el valor recibido por parametos
    tablero[posicion] = valor
    # Le mostramos el tablero para que vea como va
    ver_tablero()
    
# -----------------------------------------------------------------------------------------------

# Le damos un formato al tablero para poder verlo
def ver_tablero():
    print("\n") # "\n" es un salto de linea
    print(tablero[0] + " | " + tablero[1] + " | " + tablero[2] +"           1 | 2 | 3 ")
    print(tablero[3] + " | " + tablero[4] + " | " + tablero[5] +"           4 | 5 | 6 ")
    print(tablero[6] + " | " + tablero[7] + " | " + tablero[8] +"           7 | 8 | 9 ")
    print("\n")
    
    #  Esto es una referencia al jugador para saber que tiene que tocar para colocar su jugada en determinado lugar del tablero
    #  1 | 2 | 3
    #  4 | 5 | 6
    #  7 | 8 | 9

# -------------------------------------------------------------------------------------------------

# Ahora llamamos al tablero para verlo
print(ver_tablero())