import sys

def fibonacciNoRecursivo(n: int) -> int:
  a: int =0
  b: int =1
  c: int 
  for i in range(n):
    c=a+b
    a=b
    b=c
  return a


if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))