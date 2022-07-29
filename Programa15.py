# Programa 15
# David Emanuel Flores Beltran
# numeros negativos y positivo
cp=0
cn=0
while True:
    numero =int (input("Escribe un numero negativo o cero para terminar:"))
    if numero<0:
        cn+=1
    elif numero>0:
        cp+=1
    elif numero==0:
        break
    else:
        print("Error")
print(f"\nEl total de numeros positivos es: {cp}")
print(f"El total de numeros negativos es: {cn}")