from typing import List
from queue import LifoQueue

def calcular_expresion(expr: str, pila: LifoQueue):
    # Dividir la expresión en operandos y operadores separados por espacios
    elementos = expr.split()

    for elemento in elementos:
        if elemento.isdigit() or elemento.replace('.', '', 1).isdigit():
            # Si el elemento es un número, se agrega a la pila
            pila.put(float(elemento))
        else:
            # Si el elemento es un operador, se realiza la operación correspondiente
            num2 = pila.get()
            num1 = pila.get()

            if elemento == '+':
                resultado = num1 + num2
            elif elemento == '-':
                resultado = num1 - num2
            elif elemento == '*':
                resultado = num1 * num2
            elif elemento == '/':
                resultado = num1 / num2

            # Se agrega el resultado a la pila
            pila.put(resultado)

    # Al finalizar, la pila debe contener el resultado final
    return pila.get()

# Ejemplo de uso
expresion = "2 5 * 7 +"
pila = LifoQueue()
resultado = calcular_expresion(expresion, pila)
print(resultado)

from queue import LifoQueue

def calcular_expresion(expr: str, pila: LifoQueue):
    elementos = expr.split()

    for elemento in elementos:
        if elemento.isdigit() or (elemento[0] == '-' and elemento[1:].isdigit()):
            pila.put(float(elemento))
        else:
            num2 = pila.get()
            num1 = pila.get()

            if elemento == "+":
                res = num1 + num2
            elif elemento == "-":
                res = num1 - num2
            elif elemento == "*":
                res = num1 * num2
            elif elemento == "/":
                res = num1 / num2

            pila.put(res)

if __name__ == '__main__':
    expr = input("Ingrese la expresión en notación polaca inversa: ")
    expr = expr.strip()
    pila = LifoQueue()
    calcular_expresion(expr, pila)
    resultado = pila.get()
    print("El resultado de la expresión es:", resultado)
