# Programa 16
# David Emanuel Flores Beltran
# lista de numeros de 1 al 10 omitiendo el 5
contador=0
while contador <10:
    contador+=1
    if contador==5:
        continue
    print(f"Lista: {contador}")