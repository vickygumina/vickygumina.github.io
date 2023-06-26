from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def hayMesetaDeLong(l:List[int], n:int):
    for i in range(len(l) - n + 1):
        j = i + n - 1
        if todosIguales(l, i, j):
            return True
    return False

def todosIguales(l:List[int], i:int, j:int):
    for k in range(i+1, j+1):
        if l[k] != l[i]:
            return False
    return True

def mesetaMasLarga(l: List[int]) -> int :
  max_meseta = 0
  for n in range(1, len(l) + 1):
        if hayMesetaDeLong(l, n):
            max_meseta = n
  return max_meseta

if __name__ == '__main__':
  x = input()
  print(mesetaMasLarga([int(j) for j in x.split()]))