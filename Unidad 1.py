#Para comentarios de una sola linea
'''
    comentario multilinea
'''
#print("Hola Mundo \nhola muchacho") <- para imprimir en pantalla
#print("hola si jala") <- para imprimir en pantalla
NumBar=10
NumBar2=10.23
Cadena='hola "muchacho"'
Booleano=False
#De La variable NumBar
print(NumBar)
print(type(NumBar))
#De La Variable NumBar2
print(NumBar2)
print(type(NumBar2))
#De La Variable Cadena
print(Cadena)
print(type(Cadena))
#De la Variable Booeano
print(Booleano)
print(type(Booleano))
#para la operacion de variables
uno=34
dos=23
resultado=(uno+dos)-23
#exposiacion
resul= 2 ** 3 #exponente
print("El exponente es: ",resul)
print("El resultado es: ",resultado)
#tipado dinamico
#El tipado dinamico permite utilizar la misma bariable Canbiando lo que hay en ella
Control=23
print("El control es igual a: ",Control)
Control='si jala'
print("El Control es igual a: ",Control)
#operadores logicos
a=12
b=3
c=23
resulT=(a>b)or(b>c)
resultado2=not resulT
print(resulT)
print(resultado2)
#operadores en asignacion
a2 =0 #se tiene que declarar primero
a2 +=5 #suma en asignacion
a2 -=4 #resta en asignacion
a2 *=3 #multiplicacion en asignacion
a2 **=2 #potenciacion en asignacion
print(a2)
#salidas
cadena ='David'
edad=22
print("Hola {} tienes {} años".format(cadena,edad))
print(f"Hola {cadena} tieneas {edad} años")
curso ='python'
nombre = "David"
edad = 21
print("tutoriales de % s"%curso)
print("hola soy, %s y tengo %s años"%(nombre,edad))
print(f"hola soy {nombre} y mi edad es {edad} años.")
#entrada de datos
Nombre = input("Digita tu nombre ")
edad =int(input("tu edad es: "))
flot =float(input("Introduce un numero flotante: "))
print(f"Tu nombre es {Nombre} y tienes {edad} años")
print(f"Tu numero Flotante es: {flot}")
print("--------------------------------------")
print("Variable Nombre ",type(Nombre))
print("Variable edad   ",type(edad))
print("Variable flot   ",type(flot))