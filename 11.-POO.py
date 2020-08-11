#Una clase debe comenzar con una Mayúscula 
class Alumno:
    def agregar_alumno(self, nombre):
        self.nombre = nombre
        print('Agregando...')
        
    def mostrar_informacion(self):
        print(f'Nombre :{self.nombre}')
#Intanciando la clase
alumno = Alumno()

print(alumno)
alumno.agregar_alumno('Gary Nova')
alumno.mostrar_informacion()

alumno2 = Alumno()
alumno2.agregar_alumno('Sarai Blanco')
alumno2.mostrar_informacion()
