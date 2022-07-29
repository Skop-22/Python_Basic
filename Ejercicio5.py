# Ejercicio 5 : obtener la representación inversa ed una cadena de carcteres

cadena = 'Python'
for i in range(len(cadena)-1, -1, -1):
    print(cadena[i], end=' ')
    pass

print('\n', cadena[::-1])
