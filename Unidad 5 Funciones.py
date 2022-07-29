#funciones y como funcionan
def Primerafuncion():#definir una funcion
    print("Hola Mundo \n")
def Segundafuncion(Variable,an,mas=12.4):#definir una funcion
    print(f"Hola Mundo -{Variable}- y tengo -{an}- años")
    print(f"Variable extra -{mas}-")
    print(f"Tipo de variable: {Variable}",type(Variable))
    print(f"Tipo de variable: {an}",type(an))
    print(f"Tipo de variable: {mas}",type(mas))
def suma(a,b):#variables con operacion y como imprimirla
    print(a+b)
def suma2(x,y):#variable con operacion
    return x+y
Primerafuncion()#declarar una funcion
Segundafuncion("soy David",21)#declarar una funcion con sus valores
suma(4,5)#declarar la funcion con opercion
sum=suma2(6,89)#declarar la funcion y como mandar la a imprimir
print(sum)
def recursion(k):
    if (k > 0):
        result = k + recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print("\n")
recursion(7)
print("\n")
print("----------------------------------")
#Landa funcion
print("Funciones Lamda")
#en funcion lamda se puede usar mas de una variable
x= lambda a : a+3#Con una variable
print(x(5))
segunda =lambda b,c: b*c#con dos variables
print(segunda(3,3))