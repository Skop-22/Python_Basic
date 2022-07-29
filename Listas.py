c=1#           para añadir las 5 palabras
c2=1#          para la desicion 2 contador
Palabaras=[]#  Variable lista
proceso="si"
print("           AÑADE 5 PALABRAS A LA LISTA ")
while c<=5:
    añadir=input(f"Introduce la plabra a añadir({c}): ")
    Palabaras.append(añadir)
    c +=1
while proceso=='si':
    print()
    print("\n-------------------------")
    print("1.-Insertar")
    print("2.-Eliminar")
    print("-------------------------")
    desicion=int(input("\nQue desea hacer: "))
    if desicion==1:
        añadir=input("Introduce la palabra: ")
        Palabaras.append(añadir)
        print("-------------------------")
        print(f"       Se añadio : {añadir}")
        print("-------------------------")
        print("   LA LISTA ES: ")
        print("-------------------------")
        for i in Palabaras:
            print(i,end=" ")
        print("\n-------------------------")
    if  desicion==2:
        print("-------------------------")
        print("La Lista es: ")
        for i in Palabaras:
            print(f"Palabra({c2})= {i}")
            c2 +=1
        print("-------------------------")
        eliminar=input("Escriva la 'palabra' que desea eliminar: ")
        Palabaras.remove(eliminar)
        print("-------------------------")
        print("La Lista es: ")
        c2=0
        for i in Palabaras:
            print(f"Palabra({c2})= {i}")
            c2 += 1
    proceso=input("\n\nDesea continuar: ")
print()
print("Gracias por usar el programa Adios :)")
