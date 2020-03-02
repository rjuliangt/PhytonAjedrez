from Classnodo import Node
import os
import time

# FUNCION PARA CREAR Y ENLAZAR LOS NODOS 
def loadRow(numBox):
    tablero = []
    for i in range(0,numBox):
        tablero.append([Node(i)]*numBox)
    for valx in range(0,4):
        for valy in range(0,4):
            print("indice {}.{} valor: {}".format(valx,valy,tablero[valx][valy].status))
            if bool(tablero[valx][valy].get_node_top()):
                print("Top: {}".format(tablero[valx][valy].get_node_top().status))
            if bool(tablero[valx][valy].get_node_rigth()):
                print("Deracha: {}".format(tablero[valx][valy].get_node_rigth()))
            if bool(tablero[valx][valy].get_node_down()):
                print("Abajo: {}".format(tablero[valx][valy].get_node_down()))
            if bool(tablero[valx][valy].get_node_left()):
                print("izquierda: {}".format(tablero[valx][valy].get_node_left()))    

    #Asignacion nodos horizontales
    for i in range(0,numBox): 
        for j in range(0,numBox):
            if(i == 0 and j == 0):
                AuxTablero = Node(0)
                tablero[i][j].insert_right(AuxTablero)
                print("\n left: {}".format(tablero[i][j].status))
            if(j > 1 and j < (numBox-1)): #para los siguientes cuadro del ajadez 
                AuxTablero = Node(0)
                AuxTablero2 = Node(0)
                tablero[i][j].insert_right(AuxTablero)
                # tablero[i][j].insert_left(tablero[i][j-1])
                # tablero[i][j].insert_left(AuxTablero2)
            if(j == (numBox - 1)):
                AuxTablero2 = tablero[i][j-1]
                tablero[i][j].insert_left(AuxTablero2)
            # print("i= {} --- j= {}".format(i,j))

    #Asignacion nodos verticales
    for i in range(0,numBox): 
        for j in range(0,numBox):
            # Para el primer cuadro del ajedrez
            if(i == 0 and j == 0):
                AuxTablero = Node(0)
                tablero[i][j].insert_down(AuxTablero)
            #para los siguientes cuadro del ajadez    
            if(i > 0 and i < (numBox - 1)):
                AuxTablero = tablero[i+1][j]
                tablero[i][j].insert_top(AuxTablero)
                tablero[i][j].insert_down(AuxTablero)
            if(i == (numBox - 1)):
                AuxTablero = Node(0)#tablero[i-1][j]
                tablero[i][j].insert_top(AuxTablero)
            # tablero[i][j] = j
    # print("Finalizo enlace vertical")   
    return tablero 



def playAjedrez(tabler = []):
    tablers = tabler
    len_tab= len(tablers) 
    # for valx in range(0,4):
    #     for valy in range(0,4):
    #         print("indice {}.{} valor: {}".format(valx,valy,tablers[valx][valy].status))
    #         if bool(tablers[valx][valy].get_node_top()):
    #             print("Top: {}".format(tablers[valx][valy].get_node_top().status))
    #         if bool(tablers[valx][valy].get_node_rigth()):
    #             print("Deracha: {}".format(tablers[valx][valy].get_node_rigth()))
    #         if bool(tablers[valx][valy].get_node_down()):
    #             print("Abajo: {}".format(tablers[valx][valy].get_node_down()))
    #         if bool(tablers[valx][valy].get_node_left()):
    #             print("izquierda: {}".format(tablers[valx][valy].get_node_left()))
    nextMove(tablers,len_tab)
       

def nextMove(table,len_tabs):
    pos_table = verificationMovida(len_tabs) 
    row = pos_table[0]
    column = pos_table[1]

    if table[row][column].status != "re":
        validateMove(table,row,column)
        table[row][column].status = "re"
        print("Valor nodo {}.{} es: {}".format(row,column,table[row][column].status))
        for valx in range(0,4):
            for valy in range (4):
                print(table[valx][valy].status)
    else:
        print("Posicion Ocupad: {}.{}".format(row,column))
        print("row {} column {} data: {}".format(row,column,table[row][column].status))
        for valx in range(0,4):
            for valy in range(0,4):
                print(table[valx][valy].status)
              
    nextMove(table,len_tabs)

def validateMove(tabler,row,colum):
    len_tab = len(tabler)
    for m in range(colum,len_tab):
        if tabler[row][m].get_node_rigth() != None:
            print("Derecho esta vacio {}.{}".format(row,colum+m))
        else:
            return print("Perdio")
    pos_column = int(len_tab-colum)
    for n in range(0,pos_column):
        if tabler[row][colum-n].get_node_left() != None:
            print("Izquierda esta vacio {}.{}".format(row,colum))
        else:
            return print("Perdio")

def verificationMovida(len_tab):
    movida = str(input("Ingresa numero de casilla: "))
    mov_data = movida.partition(".") 
    rowAux =  int(mov_data[0])
    columnAux = int(mov_data[2])
    if rowAux < len_tab and columnAux < len_tab:
        return rowAux,columnAux
    else:
       print("Valores fuera de rango {}.{}".format(rowAux,columnAux))
       time.sleep(3)
       os.system("cls")
       del(movida)
       verificationMovida(len_tab)
      
    

    # clearTablero(tabler)

    # tabler[n[1]][n[2]]
#     insertMovida(tabler)

# def insertMovida(tabl = [],):
#     tabl
    

# def clearTablero(tab = []):
#     clear = int(input("Limpiar tablero"))
#     if clear == 1:
#         print("{}".format(tab))
#         tab.clear
#         print("{}".format(tab))
#     else:
#         print("No se limpiara el tablero")       


def __main__():
    option = int(input("Ingrese Opcion: \n 4)Tablero de 4x4 8)Tablero de 8x8 : "))
    if(option == 4 or option == 8):
        print("Eligio tablero de: {}".format(option))
        tabl = loadRow(option)
        playAjedrez(tabl) 

    else:
        os.system ("cls") 
        print("Elige entre 1 o 2")
        __main__()

if __name__ == "__main__":
    __main__()