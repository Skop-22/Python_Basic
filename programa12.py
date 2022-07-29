# Programa 12 en python
# David Emanuel Flores Beltran
# programa que leea el numero de grados de un angulo y escriba que tipo de angulo es

grados =float(input("Escribe el numero de grados: "))

if grados >=0 and grados <90:
    print("El angulo es agudo")
elif grados == 90:
    print("El angulo es agudo")
elif grados >90 and grados <180:
    print("El angulo es obtuso")
elif grados ==180:
    print("El angulo es llano")
elif grados >180 and grados <360:
    print("El grado es concavo")
elif grados ==360:
    print("El angulo es completo")
else :
    print("Error")