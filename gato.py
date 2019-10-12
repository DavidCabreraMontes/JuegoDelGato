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
pieza="X" #Pieza de la maquina
#------------- Metodos --------------------
def imprimirTablero():
        print(tablero)
        
def primeraRegla():
    print("R1")
    if(np.count_nonzero(tablero == pieza)<1):
        if(tablero[1][1] == " "):
            tablero[1][1]="X"
            colocar(1,1)
            return True
        if(tablero[0][0] == " "):
            tablero[0][0]="X"
            colocar(0,0)
            return True
    return False

def segundaRegla():
    print("R2")
    return contrarGane("X")

def terceraRegla():
    print("R3")
    return contrarGane("O")

def cuartaRegla():
    print("R4")
    posicionAntY=posicionesAnt[-1][0]
    posicionAntX=posicionesAnt[-1][1]
    if(posicionAntY!=0 and posicionAntX!=0 and tablero[0][0]==" "):
        colocar(0,0)
        tablero[0][0]="X"
        return True
    if(posicionAntY!=0 and posicionAntX!=2 and tablero[0][2]==" "):
        colocar(0,2)
        tablero[0][2]="X"
        return True
    if(posicionAntY!=2 and posicionAntX!=0 and tablero[2][0]==" "):
        colocar(2,0)
        tablero[2][0]="X"
        return True
    if(posicionAntY!=2 and posicionAntX!=2 and tablero[2][2]==" "):
        colocar(2,2)
        tablero[2][2]="X"
        return True
    return False

def quintaRegla():
    print("R5")
    posicionAntY=posicionesAnt[-1][0]
    posicionAntX=posicionesAnt[-1][1]
    #tablero[:,i]
    if(posicionAntY!=0 and posicionAntX!=0 and tablero[0][0]==" "):
        colocar(0,0)
        tablero[0][0]="X"
        return True
    if(posicionAntY!=0 and posicionAntX!=2 and tablero[0][2]==" "):
        colocar(0,2)
        tablero[0][2]="X"
        return True
    if(posicionAntY!=2 and posicionAntX!=0 and tablero[2][0]==" "):
        colocar(2,0)
        tablero[2][0]="X"
        return True
    if(posicionAntY!=2 and posicionAntX!=2 and tablero[2][2]==" "):
        colocar(2,2)
        tablero[2][2]="X"
        return True
    return False

def sextaRegla():
    print("R6")
    for i in range(0,3):
        for j in range(0,3):
            if(tablero[i][j]==" "):
                tablero[i][j]="X"
                colocar(i,j)
                return True
    return False

def contrarGane(ficha): #Encontrar futuro gane
    for i in range(0,3):
        if(np.count_nonzero(tablero[:,i] == ficha)==2 and np.count_nonzero(tablero[:,i] == " ")==1):#Buscar en columnas
            posicionAuxiliar=np.where(tablero[:,i]==" ")[0]
            colocar(posicionAuxiliar[0],i)
            tablero[:,i][np.where(tablero[:,i]==" ")] = "X"        
            return True
            
        if(np.count_nonzero(tablero[i,:] == ficha) == 2 and np.count_nonzero(tablero[i,:] == " ")==1):#Buscar en filas
            posicionAuxiliar=np.where(tablero[i,:]==" ")[0]
            tablero[i,:][np.where(tablero[i,:]==" ")]="X"
            colocar(i,posicionAuxiliar[0])
            return True
   
    if(np.count_nonzero(tablero[np.diag_indices(3)] == ficha)==2 and np.count_nonzero(tablero[np.diag_indices(3)] == " ")==1):#Diagonal \
        posicionAuxiliar=[np.where(tablero[np.diag_indices(3)]==" ")][0] #Como es diagonal siempre sera la misma posicion en X e Y
        #print(posicionAuxiliar)
        posicionAuxiliar=posicionAuxiliar[0][0]#El valor aun esta en una tupla para eso el [0]
        tablero[posicionAuxiliar,posicionAuxiliar] = "X"
        colocar(posicionAuxiliar,posicionAuxiliar)

    if(np.count_nonzero(np.diag(np.fliplr(tablero)) == ficha)==2 and np.count_nonzero(np.diag(np.fliplr(tablero)) == " ")==1):#Diagonal /
        posicionAuxiliar=[np.where(np.diag(np.fliplr(tablero))==" ")][0]
        #print(posicionAuxiliar)
        posicionAuxiliar=posicionAuxiliar[0][0]#El valor aun esta en una tupla para eso el [0]
        tablero[posicionAuxiliar,(2-posicionAuxiliar)] = "X"
        colocar(posicionAuxiliar,(2-posicionAuxiliar))

    return False
    
def endGame(ficha):
    for i in range(0,3):
        if(np.count_nonzero(tablero[:,i] == ficha)==3):#Buscar en columnas       
            return False
        if(np.count_nonzero(tablero[i,:] == ficha) == 3):#Buscar en filas
            return False

    if(np.count_nonzero(tablero[np.diag_indices(3)] == ficha)==3):#Diagonal \      
        return False
    if(np.count_nonzero(np.diag(np.fliplr(tablero)) == ficha)==3):#Diagonal /
        return False
    if(np.count_nonzero(tablero[i,:] == " ") == 0):
        return False
    return True

def verTiro(tablero):
    for i in range(0,3):
        for j in range(0,3):
            if(tablero[i][j]=="O"):
                if(not [i,j] in posicionesAnt):
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
            if(not turnoJ):
                turnoJ=segundaRegla()
            if(not turnoJ):
                turnoJ=terceraRegla()
            if(not turnoJ):
                turnoJ=cuartaRegla()
            #if(not turnoJ):
            #    turnoJ=quintaRegla()
            if(not turnoJ):
                turnoJ=sextaRegla()

            imprimirTablero()
            juego=endGame("X")

#------------- Start Game --------------------
startGame()
