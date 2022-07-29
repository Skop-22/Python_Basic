'''
    David
    CALCULADORA BASICA
    Escriba un programa que permita realizar las operaciones matemáticas básicas: suma, resta, multiplicación, división.
'''
print("            OPERACIONES           ")
print("Suma Resta Multiplicacion Divicion")
print("----------------------------------")
Operacion = input("Escriba La operacion a realizar: ")
if Operacion=='Suma':
    num1 = float(input("Digita tu primer numero: "))
    num2 = float(input("Digita tu segundo numero: "))
    num11=int (num1)
    num22=int (num2)
    if num11<num1:
        resultado=num1+num22
        print(f"{num1} + {num22}")
        print(f"Resultado: {resultado}")
    if num22<num2:
        resultado=num11+num2
        print(f"{num11} + {num2}")
        print(f"Resultado: {resultado}")
    if num11==num1 and num22==num2:
        resultado=num11+num22
        print(f"{num11} + {num22}")
        print(f"Resultado: {resultado}")
if Operacion=='Resta':
    num1 = float(input("Digita tu primer numero: "))
    num2 = float(input("Digita tu segundo numero: "))
    num11 = int(num1)
    num22 = int(num2)
    if num11<num1:
        resultado=num1-num22
        print(f"{num1} - {num22}")
        print(f"Resultado: {resultado}")
    if num22<num2:
        resultado=num11-num2
        print(f"{num11} - {num2}")
        print(f"Resultado: {resultado}")
    if num11==num1 and num22==num2:
        resultado=num11-num22
        print(f"{num11} - {num22}")
        print(f"Resultado: {resultado}")
if Operacion=='Multiplicacion':
    num1 = float(input("Digita tu primer numero: "))
    num2 = float(input("Digita tu segundo numero: "))
    num11 = int(num1)
    num22 = int(num2)
    if num11<num1:
        resultado=num1*num22
        print(f"{num1} * {num22}")
        print(f"Resultado: {resultado}")
    if num22<num2:
        resultado=num11*num2
        print(f"{num11} * {num2}")
        print(f"Resultado: {resultado}")
    if num11==num1 and num22==num2:
        resultado=num11*num22
        print(f"{num11} * {num22}")
        print(f"Resultado: {resultado}")
if Operacion=='Divicion':
    num1 = float(input("Digita tu primer numero: "))
    num2 = float(input("Digita tu segundo numero: "))
    num11 = int(num1)
    num22 = int(num2)
    if num11<num1:
        resultado=num1/num22
        print(f"{num1} / {num22}")
        print(f"Resultado: {resultado}")
    if num22<num2:
        resultado=num11/num2
        print(f"{num11} / {num2}")
        print(f"Resultado: {resultado}")
    if num11==num1 and num22==num2:
        resultado=num11/num22
        print(f"{num11} / {num22}")
        print(f"Resultado: {resultado}")