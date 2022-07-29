# Ejercicio 12: imprimir el calendario para un año y mes especificos.

import calendar

agnio = int(input('escribe el año: '))
mes = int(input('escribe el mes: '))

print(calendar.month(agnio, mes))
