# Programa 13
# David emanueel FLores Beltran
# Turnos de una empresa
Nombre = input("Ingresa su nombre: ")
TTurno = input("Ingresa el turno si es (nocturno o diurno): ")
HTrabajadas = int(input("Horas Trabajadas: "))
DTrabajadas = int(input("Ingrese los dias que trabaja: "))
Domingo = input("Trabaja el domingo(si/no): ")
TotalD = 0

if DTrabajadas >= 1 and DTrabajadas <= 7:
    if DTrabajadas == 7:
        if HTrabajadas >= 5 and HTrabajadas <= 10:
            if TTurno == 'nocturno':
                TotalD = HTrabajadas*190
            elif TTurno == 'diurno':
                TotalD = HTrabajadas*130
            else:
                print("Error")
                exit(1)
        else:
            print("Error")
            exit(1)
    else:
        TotalD = 0
    if HTrabajadas >= 5 and HTrabajadas <= 10:
        if TTurno == 'nocturno':
            Totalse = HTrabajadas*130
        elif TTurno == 'diurno':
            Totalse = HTrabajadas*100
        else:
            print("Error")
            exit(1)
        pass
    else:
        print("Error")
        exit(1)
if Domingo == 'si':
    if HTrabajadas >= 5 and HTrabajadas <= 10:
        if TTurno == 'nocturno':
            TotalD = HTrabajadas*190
        elif TTurno == 'diurno':
            TotalD = HTrabajadas*130
        else:
            print("Error")
            exit(1)
    else:
        print("Error")
        exit(1)
elif Domingo == 'no':
    TotalD = 0
else:
    print("Error")
    exit(1)

print("-----------------------------------------")
print(f"Empleado: {Nombre}")
print(f"Tipo de turno: {TTurno}")
print(f"Dias de la semana que trabaja:{DTrabajadas}")
print(f"Salario de la semana es de: {Totalse}", end=" ")
if TotalD != 0:
    print(f"el salario del dia domingo es de: {TotalD}")
    pass
