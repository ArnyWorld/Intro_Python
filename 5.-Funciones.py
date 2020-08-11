"""
Una función es un bloque de código diseñado para realizar
unaa ctividad, todos los lenguajes de programación tienen 
una gran cantidad de funciones ya escritas.
"""
#Función sin parámetros
def saludo():
    print("Hola Mundo")
    
saludo()

#Función con parámetros
def Datos(nombre,edad):
    print("Hola me llamo ",nombre)
    print("y tengo ",edad," años")
    
Datos("Arnaldo",25)

#Función con parámetros
def DatosPersonales(nombre,edad):
    print(f'Me llamo {nombre} y tengo {edad} años')
    
DatosPersonales("Arnaldo",25)

#Función con parámetros por defecto
def Profesion(profesion,experiencia='sin'):
    print(f'Mi profesión es {profesion}  {experiencia} experiencia')
    
Profesion("Informático","con")

Profesion("Contador")

#Función con retorno de valores
def informacion(nombre):
    return nombre

desarrolador= informacion("Arni")
print(desarrolador)

#Método vs Función
carrera = "Contaduria"
#Función
def funcion(carrera):
    print(f'Tu carrera es {carrera}')
    
funcion(carrera)

#método
print(carrera.upper())

#ejemplos
def suma(a, b):
    print(a + b)
    
suma(5,3)

def multiplicar(a,b):
    print(a*b)
    
multiplicar(5,4)
    

