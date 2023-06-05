def sumaTotal (l:list) -> int:
    i: int = 0
    suma= 0
    while i < len(l):
        suma= suma + l[i]
        i=i+1
    return suma

def ordenados (l:list) -> bool:
    i: int = 0
    resultado: bool = False
    while i < len(l)-1 and l[i] < l[i+1]:
        i=i+1
        
    if i==len(l)-1:
        resultado= True
    return resultado

def contarPalabras (l: list) -> bool:
    i: int = 0
    res: bool = False
    while i< len(l):
        i=i+1
        
    if i >= len(l) and i>=7:
        res= True
        
    return res


    