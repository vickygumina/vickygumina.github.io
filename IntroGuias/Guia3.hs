--Ejercicio1
--a
f :: Integer ->Integer
f 1 = 8
f 4 = 131
f 16 = 16

--b
g :: Integer ->Integer
g 8 = 16
g 16 = 4
g 131 = 1

--c
h :: Integer -> Integer
h 131  = f (g 131) 
h 16  = f (g 16) 
h 8  = f (g 8) 

--Ejercicio2 especificar e implementar
--a
--absoluto: calcula el valor absoluto de un numero entero.
{-problema absoluto (a: Int): Int{
    requiere{ True}
    asegura{ res=if a>0 then a else -(a) fi}
}
-}
absoluto:: Integer ->Integer
absoluto a  | a>=0 = a
            | otherwise= -a

{-b 
maximoabsoluto: devuelve el maximo entre el valor absoluto de dos numeros enteros.

problema maximoAbsoluto (a,b: Int): Int{
    requiere{ True}
    asegura{ res= if absoluto (a)>= absoluto (b) then a else b fi}
}
-}
maximoAbsoluto:: Integer -> Integer -> Integer
maximoAbsoluto a b | absoluto a >= absoluto b = absoluto a
                   | otherwise = absoluto b

{-c
maximo3: devuelve el maximo entre tres numeros enteros.

problema maximo3 (a,b,c: Int): Int{
    requiere {True}
    asegura { (a>=b) && (a>=c) => res = a }
    asegura { (b>=a) && (b>=c) => res = b }
    asegura { (c>=a) && (c>=b) => res = c }
}
-}
maximo3:: Integer -> Integer -> Integer -> Integer
maximo3 a b c | (a==b) && (a==c) = a
              | (a>b) && (a>c) = a 
              | (b>a) && (b>c) = b
              | otherwise = c

{-d
algunoEs0: dados dos numeros racionales, decide si alguno de los dos es igual a 0 (hacerlo dos veces, una usando pattern
matching y otra no).
problema algunoEs0 (a,b:Float):Bool{
    requiere {True}
    asegura {res = True <=> a=0 || b=0}
}
-}

algunoEs0 :: Float -> Float -> Bool
algunoEs0 0 0 = True
algunoEs0 a b | a==0 || b==0 = True
              | otherwise = False

{-e
ambosSon0: dados dos numeros racionales, decide si ambos son iguales a 0 (hacerlo dos veces, 
una usando pattern matching y otra no).

problema ambosSon0 (a,b: Float):Bool{
    requiere {True}
    asegura{res = True <=> a=0 && b=0}
}
-}              

ambosSon0 :: Float -> Float -> Bool
ambosSon0 0 0 = True
ambosSon0 a b = False

{-f
mismoIntervalo: dados dos numeros reales, indica si estan relacionados considerando 
la relacion de equivalencia en R cuyas clases de equivalencia son: 
(−∞, 3],(3, 7] y (7, ∞), o dicho de otra forma, si pertenecen al mismo intervalo.

problema mismoIntervalo (a,b: Float): Bool{
    requiere{True}
    asegura {(a,b <= 3) => res= True}
    asegura {(a,b >3) && (a,b <= 7) => res= True}
    asegura {(a,b < 7) => res= True}
}
-}
mismoIntervalo :: Float -> Float -> Bool 
mismoIntervalo a b | a<=3 && b<=3 = True
                   | (a>3 && b>3) && (a<=7 && b <=7) = True
                   | a>7 && b>7 = True
                   | otherwise= False

{-g
sumaDistintos: que dados tres numeros enteros calcule la suma sin sumar repetidos (si los hubiera).
Aca lo pense como que si hay valores repetidos no se suman, y solo devuelve el valor que no se repite.

problema sumaDistintos (a,b,c: Int): Int{
    requiere {True}
    asegura { a!=b && a!=c && b!=c => res = a+b+c}
    asegura { a=b && a!=c && b!=c => res = c}
    asegura { a!=b && a=c && b!=c => res = b}
    asegura { a!=b && a!=c && b=c => res = a}
    asegura { a=b && a=c => res = 0}
}
-}
sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos a b c | a/=b && a/=c && b/=c = a+b+c
                    | a==b && a/=c && b/=c = c
                    | a/=b && a==c && b/=c = b
                    | a/=b && a/=c && b==c = a
                    | otherwise = 0

{-h
esMultiploDe: dados dos numeros naturales, decidir si el primero es multiplo del segundo.
problema sumaDistintos (a,b: Int): Bool {
    requiere{ a/=0 }
    asegura {res = True <=> b mod a = 0}
}
-}
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe a b | mod a b == 0 = True
                 | otherwise= False

{-i
digitoUnidades: dado un numero natural, extrae su dıgito de las unidades.
En este caso asumo que lo que debe devolver es el ultimo digito del numero a.
Tambien podria pensarlo como que devuelve el resto del numero a pero sin su unidad,
en ese caso usaria div a 10.

problema digitoUnidades (a: Int):Int{
    requiere {True}
    asegura {res = mod a 10 }
}
-}
digitoUnidades :: Integer -> Integer
digitoUnidades a | a >= 0 && a <=9 = a
                 | otherwise= mod a 10

{-i
digitoDecenas: dado un numero natural, extrae su dıgito de las decenas.

problema digitoDecenas (a:Int):Int{
    requiere {True}
    asegura {res =  mod (div a 10) 10}
}
-}
digitoDecenas :: Integer -> Integer
digitoDecenas a | a >= 0 && a <=9 = 0
                | a>=10 && a <=99 = div a 10
                | otherwise= mod (div a 10) 10

--Ejercicio3

estanRelacionados :: Integer -> Integer -> Bool
estanRelacionados a b | mod a (-div a b * b ) == 0 = True
                      | otherwise= False

--Ejercicio4 
{-Especificar e implementar las siguientes funciones utilizando tuplas para representar pares,
ternas de numeros.
-}

{-a
prodInt: calcula el producto interno entre dos tuplas R × R

problema prodInt (t, s: Int x Int):Int{
    requiere {True}
    asegura{res= t_0 * s_0 + t_1 * s_0}
}
-}

prodInt :: (Integer, Integer) -> (Integer, Integer) -> Integer
prodInt (t0,t1) (s0,s1) = t0*s0 + t1*s1

{-b
todoMenor: dadas dos tuplas R×R, decide si es cierto que cada coordenada de la 
primera tupla es menor a la coordenada correspondiente de la segunda tupla.

problema todoMenor (t,s: Float x Float): Bool {
    requiere {True}
    asegura {res = if t0 < s0 && t1 <s1 then True else False if}
        Otra forma:
    asegura {res= True <=> (t0<s0) && (t1<s1)}
}
-}

todoMenor :: (Float,Float) -> (Float,Float) -> Bool
todoMenor (t0,t1) (s0,s1) | t0 < s0 && t1<s1 = True
                          | otherwise= False

{-c
distanciaPuntos: calcula la distancia entre dos puntos de R^2.

problema distanciaPuntos (t,s: Float x Float): Float{
    requiere {True}
    asegura {res = sqrt ((s0-t0)^2 + (s1-t1)^2)}
}
-}

distanciaPuntos :: (Float,Float) -> (Float,Float) -> Float
distanciaPuntos t s = sqrt ((fst s -fst t)^2 + (snd s - snd t)^2)

{-d
sumaTerna: dada una terna de enteros, calcula la suma de sus tres elementos.

problema sumaTerna (t: Int x Int x Int): Int{
    requiere {True}
    asegura {res = t0+t1+t2}
}
-}

sumaTerna :: (Integer, Integer,Integer) -> Integer
sumaTerna (t0,t1,t2) = t0+t1+t2

{-e
sumarSoloMultiplos: dada una terna de numeros enteros y un natural, 
calcula la suma de los elementos de la terna que son multiplos del numero natural.

Aca voy a asumir que si ninguno de los numeros de la terna es multiplo del natural
devuelva cero.

problema sumarSoloMultiplos (t:Int x Int x Int, a: Int): Int{
    requiere {a>0}
    asegura {(pt i:Int)(0<=i<3 -> res = sumatoria(dd 0 ht 3)(if t_i mod a =0 then t_i else 0 fi))}
}
-}

sumarSoloMultiplos :: (Integer,Integer,Integer) -> Integer -> Integer
sumarSoloMultiplos (t0,t1,t2) a | esMultiploDe t0 a && esMultiploDe t1 a && esMultiploDe t2 a = t0 + t1 + t2
                                | esMultiploDe t0 a && esMultiploDe t1 a && mod t2 a /= 0 = t0 + t1 
                                | mod t0 a /= 0 && esMultiploDe t1 a && esMultiploDe t2 a = t1 + t2 
                                | esMultiploDe t0 a && mod t1 a /= 0 && esMultiploDe t2 a = t0 + t2
                                | esMultiploDe t0 a && mod t1 a /= 0 && mod t2 a /= 0 = t0
                                | mod t0 a /= 0 && esMultiploDe t1 a && mod t2 a /= 0 = t1
                                | mod t0 a /= 0 && mod t1 a /= 0 && esMultiploDe t2 a = t2
                                | otherwise = 0

{-f
posPrimerPar: dada una terna de enteros, devuelve la posicion del primer numero par si es que hay alguno, 
y devuelve 4 si son todos impares.

problema posPrimerPar (t:Int x Int x Int): Int{
    requiere {True}
    asegura {hayPar(t)-> 0<= res<3 && (pt i: Int)(0<=i<3 && esPar(t_i) -> i>res) && esPar(t_res)}
    asegura {¬hayPar(t) -> res=4}
}
-}

posPrimerPar :: (Integer,Integer,Integer)->Integer
posPrimerPar (t0,t1,t2) | esMultiploDe t0 2 = 0
                        | mod t0 2 /= 0 && esMultiploDe t1 2 = 1
                        | mod t0 2 /= 0 && mod t1 2 /= 0 && esMultiploDe t2 2 = 2
                        | otherwise = 4 
