from math import sqrt

#Ejercicio1
#raizDe2(): que devuelva la raız cuadrada de 2 con 4 decimales.
def raizDe2():
    print(round(sqrt (2),4))

raizDe2()


# problema imprimir_hola ()

def imprimir_hola():
    print("Hola")
    
imprimir_hola()

#imprimir_un_verso(): que imprima un verso de una cancion que vos elijas, respetando los saltos de lınea.

def imprimir_un_verso():
    print("No te quiero sino porque te quiero")
    print("y de quererte a no quererte llego")
    print("y de esperarte cuando no te espero")
    print("pasa mi corazón del frío al fuego.")

imprimir_un_verso()


def factorial_de_dos()->int:
    n:int = 2*1
    return n

print(factorial_de_dos())

def factorial_de_tres()->int:
    n:int = 3*2*1
    return n

print(factorial_de_tres())



def factorial_de_cuatro()->int:
    n:int = 4*3*2
    return n

print(factorial_de_cuatro())

def factorial_de_cinco()->int:
    n:int=5*4*3*2
    return n

print(factorial_de_cinco())

#Ejercicio2
#1
nombre:str= str(input("Ingrese su nombre "))
def imprimir_saludo(nombre:str):
    print("Hola",nombre)

imprimir_saludo(nombre)

#2
numero:int = int(input("Ingrese un numero positivo: "))
def raiz_cuadrada_de(numero):
    print(sqrt(numero))

raiz_cuadrada_de(numero)    


