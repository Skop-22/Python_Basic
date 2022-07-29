# Programa 13
# David Emanuel Flores Beltran
# programa de empleados de una fabrica
nombre = input("Ingrese su nombre: ")
TTurno = input("Ingresa el tipo de turno (diurno/nocturno): ")
HTrabajadas= int (input("Ingresa la Horas trabajadas de (5/10): "))
DTrabajadas= int (input("Ingresa LOs dias trabajadas de(1/7): "))
if DTrabajadas >=1 and DTrabajadas <= 6:
    Domingo=input("Trabaja el domingo(si/no): ")
else:
    Domingo='si'

TotalD = 0
if DTrabajadas>=1 and DTrabajadas <=7:
    if DTrabajadas ==7:
        if HTrabajadas>=5 and HTrabajadas<=10:
            if TTurno=='nocturno':
                TotalD=HTrabajadas*190
            elif TTurno=='diurno':
                TotalD=HTrabajadas*130
            else:
                print("Error")
                exit(1)
        else:
            print("Error")
            exit(1)
    else:
        TotalD=0
    if HTrabajadas>=5 and HTrabajadas<=10:
        if TTurno=='nocturno':
            Totalsa=HTrabajadas*130
        elif TTurno=='diurno':
            Totalsa=HTrabajadas*100
        else:
            print("Error")
            exit(1)
    else:
        print("Error")
        exit(1)
else:
    print("Error")
    exit(1)
if Domingo=='si':
    if HTrabajadas>=5 and HTrabajadas<=10:
        if TTurno=='nocturno':
            TotalD=HTrabajadas*190
        elif TTurno=='diurno':
            TotalD=HTrabajadas*130
        else:
            print("Error")
            exit(1)
    else:
        print("Error")
        exit(1)
elif Domingo=='no':
    TotalD=0
else:
    print("Error")
    exit(1)
print("\n","-"*30)
print(f"Empleado: {nombre}")
print(f"Tipo De Turno: {TTurno}")
print(f"Salario de la semana es de:{Totalsa}",end=" ")
if TotalD!=0:
    print(f"El salario del dia domingo es de:{TotalD}")