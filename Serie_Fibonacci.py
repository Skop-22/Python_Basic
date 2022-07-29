print("Serie Fibonacci")
i = 1
contador = 1
numero = 1
print(f" {numero}", end=" ")
while(i < 20):
    print(f" {contador}", end=" ")
    contador = numero+contador
    numero = contador-numero
    i += 1
