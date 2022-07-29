Diccionario_Tienda={}
desicion='si'
def Agregar(Agre_Clave ,Agre_Valor):
    Diccionario_Tienda[Agre_Clave]=Agre_Valor

def Mostrar(Most_Producto):
    if (Most_Producto in Diccionario_Tienda):
        print(f"El precio de: {Most_Producto} = ",Diccionario_Tienda[Most_Producto])
    else:
        print("Error no existe este producto puede agregarlo")

while desicion=='si':
    print("--------------------------")
    print("1.-Agregar")
    print("2.-Mostrar")
    agregar=int(input("Que desea hacer: "))
    print("--------------------------")
    if (agregar==1):
        Producto= input("Introduce el nombre del producto: ")
        Precio= int(input("Introduce el Precio del produco: "))
        Agregar(Producto,Precio)
    if (agregar==2):
        Most_Producto = input("Escriva el producto: ")
        Mostrar(Most_Producto)
    desicion=input("\nDeseas Agregar un nuevo producto (si/no): ")