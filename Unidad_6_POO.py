#clase ---------------------------------------------------------------------
#Ejemplo uno del curso
print("clase ---------------------------------------------------------------------")
class Auto:#primera clase
    marca = ""     #Atributo
    modelo = 2004  #Atributo
    placa = ""     #Atributo

taxi = Auto()#obgeto
print(taxi.modelo)
'''
    Ejemplo 2
    CLASS nombre de la clase:
    DEF nombre el metodo (SELF):
    SELF.nombre de la variable = ALGORITMO
    _init_(SEFT) iniciar
'''
print("Metodos ----------------------------------------------------------------")
#Metodos ----------------------------------------------------------------
#metodo uno
class Matematica:#clase
    def Suma(self):
        self.n1 =5 #nospermite ejecutar
        self.n2 =3
s = Matematica()
s.Suma()
print(s.n1 + s.n2)
#metodo dos
print()
#Ejemplo 1
class Ropa:
    def __init__(self):
        self.marca = 'willow'
        self.talla = 'M'
        self.color = 'rojo'
camisa = Ropa()
print(camisa.talla,end=",")
print(camisa.marca,end=",")
print(camisa.color)
#ejemplo 2
class Calculdora:
    def __init__(self,n1,n2):
        self.suma = n1+n2
        self.resta =n1-n2
        self.producto =n1*n2
        self.deivion =n1/n2
operacion = Calculdora(2,4)
print("La Multiplicacion es de: ",operacion.producto)
print()
print("Crear funciones con atribitos--------------------------------------")
#Crear funciones con atribitos--------------------------------------

class Persona:
    edad = 27
    nombre ='victor'
    pais = 'brazil'

doctor = Persona()
print("La edad es: ",doctor.edad)
print("La edad es: ",getattr(doctor,'edad'))
print('el doctor tine una edad?',hasattr(doctor,'edad'))#muestra si tiene edad o un dato booleano
setattr(doctor,'nombre','hector')#para hacer cambios lo que hay dentro del atributo
print(doctor.nombre)
delattr(Persona, 'pais')#elimina el atributo
#contruccion de constructores
#   __init()__
# (constructor)
print()
class Personas:
    pass
    def __init__(self,nombre,año):#para incertar datos a la clase
        self.nombre = nombre #base del constructor
        self.año =año
    def descripcion(self):
        return '{} tiene {} '.format(self.nombre, self.año)#format para darle sentido
    def comentario(self,frase):
        return '{} dice: {}'.format(self.nombre,frase)
docto = Personas('david',26)
print(docto.descripcion())
print(docto.comentario('hola barrio'))
print()
#modificar un atributo
class Email:
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado =True
mi_correo =Email()
print('Adentro de la clase',mi_correo.enviado)
mi_correo.enviar_correo()
print('Adentro de la funcion',mi_correo.enviado)
print()
#Herencia
#permite crar una nueva clase a artir de una o mas clases existentes.
class Pokemon:
    pass
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo
    def descripcion(self):
        return '{} es un pokemon de tipo:{}'.format(self.nombre,self.tipo)

class Pikachu (Pokemon):#clase hijo de la clase Pokemon
    def ataque(self,tipoataque):
        return '{} tipo de ataque: {}'.format(self.nombre, tipoataque)

class Charmander(Pokemon):#clase hijo de la clase Pokemon
    def ataque(self,tipoataque):
        return '{} tipo de ataque: {}'.format(self.nombre, tipoataque)

nuevo_pokemon = Pikachu('bob','Electrico')
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque('impacto trueno'))
print("------------------------------------------------------------------------")
#Herencia
#-----------------------------------------------------------------------------------------------------------
class Calculadora:
    pass
    def __init__(self,numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]

    def ingresardato(self):
        self.datos = [int(input(f"Ingresa dato {i+1}:")) for i in range(self.n)]

class Op_basicas(Calculadora):
    def __init__(self):
        Calculadora. __init__(self,2)#limita a dos valores
    def suma(self):
        a,b =self.datos #trabaja con ese atributo
        s =a+b
        print(f"El resultado es: {s}")

    def resta(self):
        a,b =self.datos #trabaja con ese atributo
        r =a-b
        print(f"El resultado es: {r}")

    def multiplicacion(self):
        a,b =self.datos #trabaja con ese atributo
        m =a*b
        print(f"El resultado es: {m}")

    def divicion(self):
        a,b =self.datos #trabaja con ese atributo
        d =a/b
        print(f"El resultado es: {d}")

class Raiz (Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)

    def Cuadrada(self):
        import math
        a, =self.datos
        print(f"El resultado es: {math.sqrt(a)}")

ejemplo = Raiz()
print(ejemplo.ingresardato())
print(ejemplo.Cuadrada())
print("----------------------------------------")
#prieva con funciones integradas
#para bereficar la herencia
objeto = Op_basicas()
print(isinstance(objeto,Op_basicas))#para saber con que clase trabaja el objeto
print(isinstance(objeto,Raiz))#isinstance (Objeto,class_con_la_que_trabaja)
print(issubclass(Op_basicas,Calculadora))#para esta manera saber si una clase hijo pertenece a una clase padre
#issubclass(Class_hijo,Class_Padre)
#----------------------------------------------------------------
print("-----------------HERENCIA MULTIPLE-----------------------")
'''
    la herencia multiple se refiere a la posivilidad de crear
    una clase a partir de multiples clases superiores
    ejemplo:
    
    class Base_uno:
        pass
    class Base_dos:
        pass
    class DerivadoMultiple(Base_uno,Base_dos):
        pass
'''
'''
    herencia multinivel, las caracteristicas de la clase base 
    y la clase derivada se heredan en la nueva clase derivada
    ejemplo:
    
    class Base:
        pass
    class Derivado-uno(Base):
        pass
    class Derivado-dos(Derivado-uno):
        pass
'''
class Telefono:
    def __init__(self):
        pass
    def llamar(self):
        print('llamando...')
    def ocupado(self):
        print('ocupado...')

class Camara:
    def __init__(self):
        pass
    def fotografia(self):
        print('tomando fotos...')

class Reproduccion:
    def __init__(self):
        pass
    def reproduciendomusica(self):
        print("Reproduciendo musica")
    def reproducirvideo(self):
        print("Reproduciendo un video...")

class Smartphone(Telefono,Camara,Reproduccion):
    def __del__(self):#para limpiar lo recursos
        print('telefono apagado')

movil = Smartphone()
#print(dir(movil)) <----directorio que se le pueden aplicar
print(movil.fotografia())
print(movil.llamar())
print(movil.reproducirvideo())
print()
#--------------------------------------------------------------------------
#------------------------f-STRING------------------------------------------
#f-strings
#str-format()
print("------------------------f-STRING----------------------------------")
curso ='python'
nombre = "David"
edad = 21
print("tutoriales de % s"%curso)
print("hola soy, %s y tengo %s años"%(nombre,edad))
print('que tal soy {} y mi edad es {} años.'.format(nombre,edad))
print(f"hola soy {nombre} y mi edad es {edad} años.")
print()
class Estudiante:
    def __init__(self,nombre,apellido,edad):
        self.nombre =nombre
        self.apellido=apellido
        self.edad = edad

    def __repr__(self):
        #__repr__ representacion formal
        #__str__ representacion de una cadena o un objeto debolviendo string
        return f"Hola soy {self.nombre} {self.apellido} y tengo {self.edad} años."

nuevo_estudiante=Estudiante('victor','flores',21)
print(f"{nuevo_estudiante !r}")
print()
#Como funciona los metodos de clase y los estaticos
'''
    clase :
        una clase es como una plantilla para crear objetos.
    
    instancia:
        Un objeto se crea usando el constructor de una clase.
        Una vez que el objeto es creado se le conoce como 
        una instancia de la clase
    
    tipos de metodos:
        metodos estaticos:
            @staticmethod
                pueden ser llamados sin tener una instancia de
                la clase, ademas este tipo de metodos no tienen
                acceso al exterior
                
        metodos clase:
            @classmethod
                este metodo puede ser llamado sin crear una
                instancia de la clase.
                
        metodos instancia:
'''
#metodo clase
class Pastel:
    def __init__(self,ingredientes):
        self.ingredientes=ingredientes

    def __repr__(self):
        return f'Pastel({self.ingredientes !r})'

    @classmethod
    def Pastel_chocolate(cls):
        return cls(['harina','leche','chocolate'])
    @classmethod
    def Pastel_vanilla(cls):
        return cls(['Harina','leche','vainilla'])

print(Pastel.Pastel_chocolate())
print()
import math
class Pastel2:
    def __init__(self,ingrediente,tamaño):
        self.ingrediente=ingrediente
        self.tamaño=tamaño

    def __repr__(self):
        return (f'Pastel({self.ingrediente}, ' f'{self.tamaño})')

    def area(self):
        return  self.tamaño_area(self.tamaño)

    @staticmethod
    def tamaños_area(A):
        return A ** 2 * math.pi

nuevo_pastel2 = Pastel2(['harina','azucar','leche','crema'],4)

print(nuevo_pastel2.ingrediente)
print(nuevo_pastel2.tamaño)
print(nuevo_pastel2.tamaños_area(12))
print()
#polimorfismo
'''
    polimorfismo: Munchas Formas
    es la cntidad que tiene los objetos en diferentes clase para 
    usar un comportamiento o atributo del mismo nombre con
    diferente valor
    
    ejemplo:
    
class Auto:
    rueda = 4
    def desplasamiento(self):
        print("El auto se esta desplasando sobre cuatro ruedas")

class Moto:
    rueda = 2
    def desplasamiento(self):
        print("La moto se esta despalasando sobre dos rudas")
'''

class Animales:
    def __init__(self,nombre):
        self.nombre =nombre
    def tipo_animal(self):
        pass

class Leon(Animales):
    def tipo_animal(self):
        print("animal salbaje")

class Perro(Animales):
    def tipo_animal(self):
        print('Animal domestico')

nuevo_animal = Leon('SIMBA')
nuevo_animal.tipo_animal()

nuevo_animal2 =Perro('REX')
nuevo_animal2.tipo_animal()
print()
#polimorfismo por funcion
class Tomate:
    def tipo(self):
        print('vegetal')
    def color(self):
        print('rojo')

class Manzana:
    def tipo(self):
        print('Fruta')
    def color(self):
        print('verde')

def funcion(objeto):
    objeto.tipo()
    objeto.color()

nuevo_tomate = Tomate()
funcion(nuevo_tomate)
print()
nuevo_Manzana =Manzana()
funcion(nuevo_Manzana)
print()
#polimorfismo por metodos
#se usa cundo hay mas de un objeto
class Colombia:
    def capital(self):
        print('Bogota')
    def idioma(self):
        print('Español')

class Francia:
    def capital(self):
        print('Paris')
    def idioma(self):
        print('frances')

colombiano = Colombia()
frances =Francia()
for pais in (colombiano,frances):#para barios objetos
    pais.capital()
    pais.idioma()
print()
#polimorfismo con herencia
class Aves:
    def volar(self):
        print('La malloria de las aves pueden volar pero algunas no')

class Aguila(Aves):
    def volar(self):
        print('Las aguilas pueden volar')

class Gallina(Aves):
    def volar(self):
        print('La gallina no puede volar')

obj_ave = Aves()
obj_aguila=Aguila()
obj_gallina=Gallina()
print()
obj_ave.volar()
obj_aguila.volar()
obj_gallina.volar()
