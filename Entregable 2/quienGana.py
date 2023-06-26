import sys


def juegaBien(j:str):
    return j == "Piedra" or j == "Papel" or j == "Tijera"

def gana(j1:str, j2:str):
    return piedraGanaAtijera(j1, j2) or tijeraGanaAPapel(j1, j2) or papelGanaAPiedra(j1, j2)

def piedraGanaAtijera(j1:str, j2:str):
    return j1 == "Piedra" and j2 == "Tijera"

def tijeraGanaAPapel(j1:str, j2:str):
    return j1 == "Tijera" and j2 == "Papel"

def papelGanaAPiedra(j1:str, j2:str):
    return j1 == "Papel" and j2 == "Piedra"

def quienGana(j1: str, j2: str) -> str : 
    if juegaBien(j1) and juegaBien(j2):
        if gana(j1, j2):
            return "Jugador1"
        elif gana(j2, j1):
            return "Jugador2"
        else:
            return "Empate"
    else:
        return "Error: Jugada inválida"


if __name__ == '__main__':
  x = input()
  jug = str.split(x)
  print(quienGana(jug[0], jug[1]))