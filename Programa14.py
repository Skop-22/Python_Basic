# Programa 14
# David Emanuel Flores Beltran
# promedio de edades
c=0
a=0
edad=int(input("Esctribe la edad o cero para termoinar"))
while edad !=0:
    c+=1
    a+=edad
    edad=int(input("Esctribe la edad o cero para termoinar"))

print(f"El promedio de edad es: {a/c}")