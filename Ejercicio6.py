# Ejercicio 6: obtener un conjunto de numeros por coma y crear una lista

entrada = input('escriba varios numeros separados por coma: ')

print(entrada)
print(type(entrada))
# split
numeros = entrada.split(',')
print(type(numeros))
print(numeros)
