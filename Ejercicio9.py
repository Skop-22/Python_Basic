# Ejercicio 9: Mostrar la fecha de un evento almacenada en una tupla
fechaEvento = (2023, 9, 14)

print(type(fechaEvento))
# se ban a mapear a cada elemento que tiene la tupla
print('El evento programado sera para la fecha: %i/%i/%i' % fechaEvento)
Agio, mes, dia = fechaEvento
# Agio, mes = fechaEvento#error
print(f"El vento programado sera para la fecha: {Agio}/{mes}/{dia}")
