#listas
lista = ['hola','mundo','soy','david','jejeje','22']
del(lista[0])#elimina elementos
print(lista[0])#imprime la posicion
print(lista[-1])#imprime la ultima posicion
print(lista)
lista.remove("mundo")#elimina los elementos por nombre
print(lista)
lista.append("añadido")#añadir un elemento a la lista siempre se añade al final
print(lista)
lista.insert(0,'nuevo')#inserta el valor en la posicion que deseamos
#Diccionarios
# variable_del_diccionario = { "Clave":"Valor"}
print("------------------------------------------------")
print("                       DICCIONARIOS ")
print("------------------------------------------------")
diccionario={"rojo":"red","azul":"blue","verde":"grend"}
diccionario["amarillo"]="yellow" #agraga claves y valor al diccionario, tambien se puede modificar
diccionario["azul"]="BLUE"#modifica
del(diccionario["verde"])#elimina lo que hay en el diccionario por medio de su clave
print(diccionario)#imprime lo que hay en el diccionario
print(diccionario["rojo"])#Imprime el valor de la clave del diccionario
print(diccionario.get("hola","Error no existe este valor"))#para mandar error en diccionario no funciona con otra cosa
print("rojo" in diccionario)#evalua lo que hay en la clave del diccionario
print(diccionario.keys())#muestra solamente las claves del diccionario
print(diccionario.values())#muestra solamente los valores del diccionario
print(diccionario.items())#Recorre todo el diccionaio al macenandolos en tuplas
print(len(diccionario))#muestra cuantas claves hay en el diccionario
diccionario.clear()#para eliminar lo que hay en el diccionario
print(diccionario)
