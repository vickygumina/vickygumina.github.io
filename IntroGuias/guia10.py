#guia 10
#ejercicio11

from queue import LifoQueue as Pila
import random

#pila=Pila() #pila vacia
#pila.put(1)

def pila_aleatoria(cantidad:int)->int:
    pila=Pila()
    for i in range(cantidad):
        numero= random.randint(1,100)
        pila.put(numero)
    return pila
    
def copiar_pila(una_pila)->Pila:
    lista_intermedia=[]
    nueva_pila= Pila()
    #construyo la lista intermedia
    while(una_pila.empty()==False):
        lista_intermedia.append(una_pila.get())
    #reconstruyo la pila original y la nueva_pila
    cantidad=len(lista_intermedia)
    for i in range (cantidad):
        elemento=lista_intermedia[cantidad-1-i]
        nueva_pila.put(elemento)
        una_pila.put(elemento)
        
    return nueva_pila    
    
    
def buscar_el_maximo(p:Pila)->int:
    nueva_pila=copiar_pila(p)
    
    maximo_actual=nueva_pila.get()
        
    while(nueva_pila.empty()==False):
        posible_maximo= nueva_pila.get()
        if (maximo_actual < posible_maximo):
            maximo_actual=posible_maximo
        
    
    return maximo_actual
    

def tope(pila:Pila([int]))->int:
    tope_de_pila = pila.get()
    pila.put(tope_de_pila)
    return tope_de_pila
    
#print(tope(pila))    

pila_Vic=pila_aleatoria(10)  
elemento_maximo=buscar_el_maximo(pila_Vic)
print(elemento_maximo)