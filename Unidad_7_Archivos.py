#ARCHIVOS (de texto)
# Abrir y cerrar archivos
#r =leerlo
#w =escrivir y cambiar su contenido
#a =añadir informacion
#r+ =leer y escrivir
c=0
Archivos_estudiantes = open("Estudiantes.txt","r")#abrir el archivo y lo que se hace con es archivo
print(Archivos_estudiantes.readline())#imprime por linea
for est in Archivos_estudiantes:
    c+=1
    print(c,est)
#lo buelbe a leer
Archivos_estudiantes = open("Estudiantes.txt","r")#abrir el archivo y lo que se hace con es archivo
print(Archivos_estudiantes.readable())#para saber si es legible o se puede leer
print(Archivos_estudiantes.read())#lee el archivo
#escribir
Archivos_estudiantes.close() #cerrar archivo
archivo_estu=open("Estu.txt","w")
print(archivo_estu.write("Este es un archivo de nuevo"))
archivo_estu.close()
print()
archivo=open("nuevo.txt","a")
print(archivo.write("Hola como estas si esta jalando\n"))
archivo.close()
#eliminar un archibo
import os
os.remove("Estu.txt")#elimiar el archivo
