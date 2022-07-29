# Ejercicio 3: obtener la fecha y la hora actual en el sistema
import datetime


HoraFecha = datetime.datetime.now()
print(HoraFecha)
print(type(HoraFecha))

print('\n', HoraFecha.strftime('%d/%m/%Y %H:%M:%S'))
