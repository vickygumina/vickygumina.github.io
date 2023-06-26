from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.

# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def esMatriz(matriz:List[List[int]]):
    if len(matriz) == 0 or len(matriz[0]) == 0:
        return False
    first_row_length = len(matriz[0])
    for i in range(len(matriz)):
        if len(matriz[i]) != first_row_length:
            return False
    return True

def filaAnteriorMasN(matriz:List[List[int]], i:int, n:int):
    for j in range(len(matriz[0])):
        if matriz[i][j] != matriz[i-1][j] + n:
            return False
    return True

def filasParecidasAanterior(matriz:List[List[int]], n:int):
    for i in range(1, len(matriz)):
        if not filaAnteriorMasN(matriz, i, n):
            return False
    return True


def filasParecidas(matriz: List[List[int]]) -> bool :
  if not esMatriz(matriz):
    return False
  for n in range(-100, 101):
      if filasParecidasAanterior(matriz, n):
          return True
  return False


if __name__ == '__main__':
  filas = int(input())
  columnas = int(input())
 
  matriz = []
 
  for i in range(filas):         
    fila = input()
    if len(fila.split()) != columnas:
      print("Fila " + str(i) + " no contiene la cantidad adecuada de columnas")
    matriz.append([int(j) for j in fila.split()])
  
  print(filasParecidas(matriz))