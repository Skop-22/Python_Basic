# ejercicion 7: Obtener la extension de un archivo aspecificado por el ususario
nombreDelArchivo = input('Ingrese el nombre del archivo: ')

partesNombreArchivo = nombreDelArchivo.split('.')
print(type(partesNombreArchivo))
print(partesNombreArchivo)

# obtine el ultimo elemento de la lisita que regresa split
print(partesNombreArchivo[-1])
