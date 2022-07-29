print("    CLAVE    ")
Clave = input("Escriva la clave: ")
Contraseña = "holamundo.12"
Clave =Clave.lower()#Convertir en minusculas la contraseña
c=1
while Clave!=Contraseña and c<=3:
    Clave = input(f"Error Escriva de nuevo la contraseña ({c}): ")
    Clave = Clave.lower()  # Convertir en minusculas la contraseña
    c +=1
if Clave==Contraseña:
    print("----------------------------")
    print("     Contraseña correcta")
    print("----------------------------")
if Clave != Contraseña:
    print("----------------------------")
    print("  error en la contraseña")
    print("     Fin de intentos")
    print("---------------------------")