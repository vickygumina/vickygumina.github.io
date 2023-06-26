from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int :
  if origen == destino:
    return -1
  
  ciudades_visitadas:List[str] = []
  ruta:List[Tuple[str, str]] =[(origen,"")]

  while ruta:
    (ciudad_actual, vuelo_anterior) = ruta.pop()
    ciudades_visitadas.append(ciudad_actual)

    for vuelo in vuelos:
      (ciudad_partida, ciudad_llegada) = vuelo

      if ciudad_partida == ciudad_actual and vuelo != vuelo_anterior:
                if ciudad_llegada == destino:
                    return len(ciudades_visitadas)
                
                ruta.append((ciudad_llegada, vuelo_anterior ))

  return -1

if __name__ == '__main__':
  origen = input()
  origen = origen.strip()
  destino = input()
  destino = destino.strip()
  vuelos = input()
  vuelos = vuelos.strip()
  
  print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))