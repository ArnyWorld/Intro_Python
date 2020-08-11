#Una clase debe comenzar con una Mayúscula 
class Alumno:
    #Constructor
    def __init__(self, nombre, registro,sexo, semestre):
        self.nombre = nombre
        self.registro = registro
        self.sexo = sexo
        self.semestre = semestre
            
    def mostrar_informacion(self):
        print(f'Nombre :{self.nombre}, Registro: {self.registro}, Sexo: {self.sexo}, Semestre: {self.semestre}')
#Intanciando la clase



alumno = Alumno('Gary Nova','125456','Masculino','1er semestre')
alumno.mostrar_informacion()

alumno2 = Alumno('Sarai Blanco','125987','Femenino','8vo semestre')
alumno2.mostrar_informacion()
