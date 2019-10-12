#0 y 1
import numpy as np

tablero=[[" "," "," "],[" "," "," "],[" "," "," "]]
tablero = np.array(tablero)
posicion1=0
posicion2=0
pos1=0
pos2=0
posicionesAnt=[]
turnoJ=True #Cambiar turno
juego=True #Controla el fin del juego
#------------- Metodos --------------------
def imprimirTablero():
        print(tablero)
        
def primeraRegla():
    tablero[0][0]="X"
    if(tablero[1][1] == " "):
        tablero[1][1]="X"
        colocar(1,1)
        return True
    else:
        tablero[0][0]="X"
        colocar(0,0)
        return True
    return False

def segundaRegla():
    return contrarGane("X")

def terceraRegla():
    return contrarGane("O")

def cuartaRegla():
    #[0][0] [0][2] [2][0] [2][2]
    print(posicionesAnt)
    posicionAntY=posicionesAnt[-1][0]
    posicionAntX=posicionesAnt[-1][1]

    if(posicionAntY!=0 and posicionAntX!=0):
        colocar(0,0)
        tablero[0][0]="X"
    if(posicionAntY!=0 and posicionAntX!=2):
        colocar(0,2)
        tablero[0][0]="X"
    if(posicionAntY!=2 and posicionAntX!=0):
        colocar(2,0)
        tablero[0][0]="X"
    if(posicionAntY!=2 and posicionAntX!=2):
        colocar(2,2)
        tablero[0][0]="X"

def quintaRegla():
    pass

def sextaRegla():
    for i in range(0,3):
        for j in range(0,3):
            if(tablero[i][j]==" "):
                tablero[i][j]="X"
                colocar(i,j)
    return True

def contrarGane(ficha): #Encontrar futuro gane
    for i in range(0,3):
        if(np.count_nonzero(tablero[:,i] == ficha)==2):#Buscar en columnas
            posicionAuxiliar=np.where(tablero[:,i]==" ")[0]
            colocar(posicionAuxiliar[0],i)
            tablero[:,i][np.where(tablero[:,i]==" ")] = "X"        
            return True
            
        if(np.count_nonzero(tablero[i,:] == ficha) == 2):#Buscar en filas
            tablero[i,:][np.where(tablero[i,:]==" ")]="X"
            posicionAuxiliar=np.where(tablero[i,:]==" ")[0]
            colocar(i,posicionAuxiliar[0])
            return True
   
    if(np.count_nonzero(tablero[np.diag_indices(3)] == ficha)==2):#Diagonal \
        print("D: ",tablero[np.diag_indices(3)])
        print("Diagonal ",np.where(tablero[np.diag_indices(3)])) 
        tablero[np.diag_indices(3)][np.where(tablero[np.diag_indices(3)]==" ")] = "R"
        print(tablero[np.diag_indices(3)][np.where(tablero[np.diag_indices(3)]==" ")])
    
    #Aun no
    if(np.count_nonzero(np.diag(np.fliplr(tablero)) == ficha)==2):#Diagonal /
        np.diag(np.fliplr(tablero))[np.where(tablero[:,i]==" ")] = "R"

    return False
    
def endGame():
    pass

def verTiro(tablero):
    for i in range(0,3):
        for j in range(0,3):
            if(tablero[i][j]=="O"):
                if(not tablero[i][j] in posicionesAnt):
                    posicionesAnt.append([i,j])
                    break

def colocar(posicion1,posicion2):
    print("Y: ",posicion1," X:",posicion2)

def startGame():
    global turnoJ
    global juego
    while(juego):
        if(turnoJ):
            print("Jugador (O)")
            pos1=int(input("Y: "))
            pos2=int(input("X: "))
            tablero[pos1][pos2]="O"
            imprimirTablero()
            turnoJ=False
        else:
            print("Maquina (X)")
            verTiro(tablero)
            turnoJ=primeraRegla()
            turnoJ=False
            if(not turnoJ):
                turnoJ=segundaRegla()
            turnoJ=False
            if(not turnoJ):
                terceraRegla()
            turnoJ=True
            if(not turnoJ):
                cuartaRegla()
            if(not turnoJ):
                quintaRegla()
            if(not turnoJ):
                sextaRegla()
            imprimirTablero()
            juego=False #Va hacer remplazado por la funcion endgame

#------------- Start Game --------------------
startGame()
