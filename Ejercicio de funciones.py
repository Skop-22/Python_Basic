Suma = lambda a, b: print(f"La suma de: {a}+{b}={a + b}")

def HolaMundo():
    print("Hola Mundo")

def Sum(b, c):
    return b + c

def ParoImpar(NumS):  # Numero salida
    NumS = NumS % 2
    NumS = int(NumS)
    print("-------------------------------")
    if (NumS == 0):
        print(f"El Numero es -Par- por que da {NumS}")
    else:
        print(f"El Numero es -impar- por que da {NumS}")

Multiplicacion = lambda g, h: print(f"La multiplicacion de {g}*{h}={g * h}")
from random import *#para la funcion randint
def Generador_De_Numero_Aleatorio(Minimo,Maximo):
    if Minimo>Maximo:
        aux = Minimo
        Minimo = Maximo
        Maximo =aux
    return randint(Minimo,Maximo)#funciona con la libreria de random
def Factorial(Num):
    Resultado=Num
    for i in range(Num-1,1,-1):
        Resultado=Resultado*i
    return Resultado
def NumeroCentral(NumeroA,NumeroB):
    if NumeroA>NumeroB:
        aux = NumeroA
        NumeroA = NumeroB
        NumeroB =aux
    while NumeroA<NumeroB:
        NumeroA=NumeroA+1
        print(NumeroA,end=",")
def numeroentre(Num1,Num2):
    if Num1>Num2:
        aux=Num1
        Num1=Num2
        Num2=aux
    for i in range(Num1+1,Num2):
        print(i,end=",")
# ----------------------------------------------------------------------------
HolaMundo()
Suma(5, 4)
print("La suma de 4+6=", Sum(10, 20))
NumE = float(input("Introduce el numero: "))  # Numero entrada
ParoImpar(NumE)
print("-------------------------------------------")
NumeroA = int(input("Introduce El primer valor: "))
NumeroB = int(input("Introduce El segundo valor: "))
Multiplicacion(NumeroA, NumeroB)
i=0
while i<10:
    print(Generador_De_Numero_Aleatorio(NumeroA,NumeroB))
    i+=1
print()
print(f"El Factorial de {NumeroA} es de :{Factorial(NumeroA)}")
NumeroCentral(NumeroA,NumeroB)
print()
numeroentre(NumeroA,NumeroB)