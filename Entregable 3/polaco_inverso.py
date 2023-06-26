from queue import LifoQueue


# para el tipo pila de floats, usar: "pila: LifoQueue". La notación "pila: LifoQueue[float]" no funciona.
# Es decir, debería decir "pilaOperandos: LifoQueue[float] en lugar de "pilaOperandos: LifoQueue"
def calcular_expresion(expr: str, pila: LifoQueue):
  elementos: str = expr.split()

  for elemento in elementos:
    if elemento.isdigit() :
      pila.put(float(elemento))

    else:
      num2 = pila.get()
      num1 = pila.get()

      if elemento == "+":
        res = num1+num2

      elif elemento == "-":
        res = num1-num2
      elif elemento == "*":
        res = num1 * num2
      elif elemento == "/":
        res = num1 /num2

      pila.put(res)
   



if __name__ == '__main__':
  x = input()  # Por ejemplo: 2 5 * 7 +
  x = x.strip()
  pila = LifoQueue()
  calcular_expresion(x, pila)
  resultado = pila.get()
  print(round(resultado, 5))
