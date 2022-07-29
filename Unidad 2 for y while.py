#condicionales
#los if funcionan con identacion o lo que lo separa del comienzo
a=int(input("Introdusca un numero: "))
if a>0:
    print("El numero es entero o igual")#pertenece al if
    print("se cumple")#pertenece al if
elif a==0: #else if conocido
    print("El numero es zero: ")
else:
    print("El numero es negativo")
    print("no se cumple")
print("Fin del if ")#lla no pertenece al if
#<-----------------------------------------------------------------------------------------
#bucles o siclos
#bucle while
#Ejemplo 1  <------------------------------------------------------------------------------
import math
num = int(input("Digita un numero: "))
while num<0:
    print("Error digita un numero entero positivo")
    num = int(input("Digita un numero: "))
raiz=math.sqrt(num)#Raizcuadrada
print(f"La Raizcuadrada es: {raiz:.3f}")
print("-------------------------------")
#Ejemplo2<---------------------------------------------------------------------------------
c=1
while c<=10:
    print(f"{c}.-Hola Mundo")
    c +=1
print()
#bucle for
'''
    en el bucle for se utiliza colecciones esto en python
    lista, tupla, conjunto, diccionario o cadena
    recorriendo elemento por elemento
    [],{conjuntos},(listas)
'''
cole =[1,10,12,5,'hola']#la coleccion
for i in cole:
    #print('Hola Mundo')
    print(f"El Elemento de la variable es: {i}")#toma el valor de la coleccion
print()
Diccionario = {'juan':22,'David':21,'Martin':34,'Mario':45}#Esto es un diccionario
#Muestra las clabes
for i in Diccionario:
    print(f"La clabe es: {i}")#La clabe del diccionario o la coleccion que trabaja for
print()
#Muestra el valor de las clables
for i in Diccionario:
    print(f"El valor es: {Diccionario[i]}")#muestra el valor de las clabes o los valores
print()
#Muestra ambas clabe y valor
for i in Diccionario:
    print(f"La clable es: {i} y el valor es: {Diccionario[i]}")
#forma tecnica de diccionarios
for clave,valor in Diccionario.items():
    print(f"{clave} -> {valor}")
print()
#cadenas con for
cadena = "David Emanuel"
a=0
for i in cadena:
    a +=1
    print(f"{a}.-Hola")
print()
for i in cadena:
    print(f"{i}",end=" ")#para evitar los altos de linea de los print