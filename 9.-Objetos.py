#Los objetos son similares a los arrays, ya que almacena información de
#distinto tipo, para acceder a un elemento se ayuda de un KEY

persona = {
    'nombre' : 'Arni',
    'profesion': 'Informática',
    'edad': 25
}

print(persona['nombre'])

#recuperar información
nombre = persona['nombre']
print(nombre)

#Agregando nuevos valores
persona['estado-civil'] = 'Casado'
print(persona)

#elimnar valor
del persona['estado-civil']
print(persona)

####################### Otra forma de manipular objetos  DICCIONARIOS
jugador = {}
print(jugador)
jugador['nombre'] = 'Arni'
jugador['puntaje'] =100 
#incrementando puntaje
jugador['puntaje'] =200

print(jugador)
#acceder a un valor
print(jugador.get('vida','No existe ese valor'))

for llave, valor in jugador.items():
    print(valor)
    
#eliminar jugador
del jugador['nombre']
del jugador['puntaje']
print(jugador)